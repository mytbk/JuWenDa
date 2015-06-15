import random, string, json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from usersystem.models import UserModel, Search, Answer
from usersystem.utils import call_api


def index(request):
	return render(request, "index.html", {})


def search(request):
	return render(request, "search.html")


def answerlist(request):
	return render(request, "answerlist.html", {})


@csrf_exempt
def create_user(request):
	"""
	创建一个用户：用户名为10位随机字母，密码为10位随机字母+数字，该函数不验证设备是否创建过账号
	前置条件
		该接口要求POST请求
	参数
		"imei": 设备的imei
	返回数据
		"username": 用户名<string>
		"password": 密码<string>
	"""
	letters = list(string.ascii_letters)
	digits = list(string.digits)
	imei = request.POST["imei"]
	while True:
		username = "".join(random.sample(letters, 10))
		password = "".join(random.sample(letters + digits, 10))
		if not User.objects.filter(username=username).exists():
			user = User.objects.create_user(username=username, password=password)
			user_model = UserModel(user=user, imei=imei)
			user_model.save()
			result = {"username": username, "password": password}
			return JsonResponse(result)


@csrf_exempt
def authenticate_user(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(username=username, password=password)
	# 密码输入错误
	if user is None:
		return render(request, "index.html", {"error": 1})
	# 验证成功
	login(request, user)
	return render(request, "search.html", {})


@csrf_exempt
@login_required(login_url='/web/login')
def set_password(request):
	"""
	更改指定用户的密码
	前置条件
		该接口要求POST请求
	参数
		"new_password": 新密码
	返回数据
		"status": 操作状态<int>
		0: 操作成功
		1: 用户输入的旧密码错误，操作失败
	"""
	new_password = request.POST["new_password"]
	request.user.set_password(new_password)
	request.user.save()
	return JsonResponse({"status": 0})


@csrf_exempt
def search_answer(request):
	title = request.POST["title"]
	if not request.user is None:
		user = request.user
		search = Search(title=title, user=user)
		search.save()
	answers = []
	page = 1
	while len(answers) <= 20 and page <= 10:
		result = call_api({
		"iw-apikey": 123,
		"iw-cmd": "search",
		"p": page,
		"q": title
		})
		data = json.loads(result)
		data = data["iw-response"]["iw-object"]["list"]
		for answer in data:
			print(answer)
			rep = [x for x in answers
			       if x["summary"].count(answer["summary"][:-12]) != 0 or answer["summary"].count(x["summary"][:-12]) != 0]
			print(len(rep))
			if len(rep) == 0:
				answers.append(answer)
		page += 1
	return render(request, "answerlist.html", {"answers": answers})


@csrf_exempt
def get_detail(request):
	"""
	获得详细结果页面
	前置条件
		该接口要求POST请求
	参数
		"link": 详细页面URL
	返回数据
		见燕风API
	"""
	link = request.POST["link"]
	result = call_api({
	"iw-apikey": 123,
	"iw-cmd": "resultcontent",
	"iw_ir_1": link
	})
	data = json.loads(result)
	print(data)
	return JsonResponse(data)


@csrf_exempt
@login_required(login_url='/web/login')
def ask_question(request):
	"""
	提出问题
	前置条件
		该接口要求POST请求
	参数
		"title": 问题标题
		"description": 问题描述
		"tag": 标签
	返回数据
		"status": 操作状态<int>
		0: 操作成功
		1: 操作失败
	"""
	title = request.POST["title"]
	description = request.POST["description"]
	tag = request.POST["tag"]
	if ask_question_at_csdn(title, description):
		return JsonResponse({"status": "0"})
	return JsonResponse({"status": "1"})


@csrf_exempt
@login_required(login_url='/web/login')
def up_vote(request):
	"""
	赞同或取消赞同答案。如果用户对该答案未点赞，则赞同；反之取消赞同。
	前置条件
		该接口要求POST请求
	参数
		"link": 答案的URL
		"username": 用户名
	返回数据
		无
	"""
	link = request.POST["link"]
	user = request.user
	userModel = user.usermodel
	try:
		answer = userModel.voteAnswers.get(link=link)
		answer.good = answer.good - 1
		userModel.voteAnswers.remove(answer)
		answer.save()
	except ObjectDoesNotExist:
		try:
			answer = Answer.objects.get(link=link)
			answer.good = answer.good + 1
			answer.save()
			userModel.voteAnswers.add(answer)
			userModel.save()
		except ObjectDoesNotExist:
			answer = Answer(link=link, good=1)
			answer.save()
			userModel.voteAnswers.add(answer)
			userModel.save()
	return JsonResponse({})


@csrf_exempt
def get_vote(request):
	"""
	获取答案赞同数
	前置条件
		该接口要求POST请求
	参数
		"link": 答案的URL
	返回数据
		"good": 答案的赞同数
	"""
	link = request.POST["link"]
	try:
		answer = Answer.objects.get(link=link)
		return JsonResponse({"good": answer.good})
	except ObjectDoesNotExist:
		return JsonResponse({"good": 0})


def ask_question_at_csdn(title, description):
	"""
	print("getlt")
	# 获取lt
	login_lt = call_api({
	"iw-apikey": 123,
	"iw-cmd": "getloginlt"
	})
	login_lt = json.loads(login_lt)
	login_lt = login_lt["iw-response"]["iw-object"]["lt"]
	# 登录
	result = call_api({
	"iw-apikey": 123,
	"iw-cmd": "login",
	"username": "ju_wen_da@163.com",
	"password": "ju_wen_da",
	"lt": login_lt
	})
	print("login result: " + result)
	"""
	# 提问
	result = call_api({
	"iw-apikey": 123,
	"iw-cmd": "question",
	"question[is_reward]": "false",
	"question[tag_list]": "",
	"question[body]": description,
	"question[title]": title,
	"question[from_type]": "ask.csdn.net"
	})
	print("Ask result: " + result)
	data = json.loads(result)
	data = data["iw-response"]["iw-object"]["responseResultStr"]
	return "添加问题成功" in data

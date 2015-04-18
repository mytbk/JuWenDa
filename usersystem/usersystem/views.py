import random, string, json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from usersystem.models import UserModel
from usersystem.utils import call_api, http_get


@csrf_exempt
def is_created(request):
	"""
	判断某用户设备是否创建过账户
	前置条件
		该接口要求POST请求
	参数
		"imei": 设备的imei
	返回数据
		"created": 该设备是否创建过账号<int>
		0: 未创建过
		1: 创建过
	"""
	imei = request.POST["imei"]
	if UserModel.objects.filter(imei=imei).exists():
		return JsonResponse({"created": 1})
	return JsonResponse({"created": 0})


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
	"""
	验证用户名和密码是否正确
	前置条件
		该接口要求POST请求
	参数
		"username": 用户名
		"password": 密码
	返回数据
		"status": 验证状态<int>
		0: 操作成功
		1: 用户输入的密码错误
	"""
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(username=username, password=password)
	# 密码输入错误
	if user is None:
		return JsonResponse({"status": 1})
	# 验证成功
	return JsonResponse({"status": 0})


@csrf_exempt
def set_password(request):
	"""
	更改指定用户的密码
	前置条件
		该接口要求POST请求
	参数
		"username": 用户名
		"old_password": 旧密码
		"new_password": 新密码
	返回数据
		"status": 操作状态<int>
		0: 操作成功
		1: 用户输入的旧密码错误，操作失败
	"""
	username = request.POST["username"]
	old_password = request.POST["old_password"]
	new_password = request.POST["new_password"]
	user = authenticate(username=username, password=old_password)
	# 密码输入错误
	if user is None:
		return JsonResponse({"status": 1})
	# 更改密码
	user.set_password(new_password)
	user.save()
	return JsonResponse({"status": 0})


@csrf_exempt
def set_username(request):
	"""
	更改指定用户的用户名
	前置条件
		该接口要求POST请求
	参数
		"old_username": 旧用户名
		"new_username": 新用户名
		"password": 密码
	返回数据
		"status": 操作状态<int>
		0: 操作成功
		1: 用户输入的旧密码错误，操作失败
		2: 用户输入的新用户名已存在或新用户名和旧用户名相同，操作失败
	"""
	old_username = request.POST["old_username"]
	new_username = request.POST["new_username"]
	password = request.POST["password"]
	user = authenticate(username=old_username, password=password)
	# 密码输入错误
	if user is None:
		return JsonResponse({"status": 1})
	# 新用户名已存在
	if User.objects.filter(username=new_username).exists():
		return JsonResponse({"status": 2})
	# 更改用户名
	user.username = new_username
	user.save()
	return JsonResponse({"status": 0})


@csrf_exempt
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
	ask_question_at_csdn("appcan获取imei失败", "appcan获取imei失败")
	return HttpResponse("")


def ask_question_at_csdn(title, description):
	print("getlt")
	# 获取lt
	login_lt = call_api({
	"iw-apikey": 123,
	"iw-cmd": "getloginlt"
	})
	print(login_lt)
	login_lt = json.loads(login_lt)
	print(login_lt)
	login_lt = login_lt["iw-response"]["iw-object"]["lt"]
	print(login_lt)
	# 登录
	result = http_get("http://app.internetware.cn/jwd/?iw-apikey=123&iw-cmd=login&username=ju_wen_da@163.com&password=ju_wen_da&lt=" + login_lt)
	print("login result: " + result)
	# 获取提交token
	token = http_get("http://app.internetware.cn/jwd/?iw-apikey=1234&iw-cmd=gettoken")
	print("get token result: " + token)
	# # 获取验证码key
	# captchas_key = call_api({
	# "iw-apikey": 1234,
	# "iw-cmd": "newcaptchas"
	# })
	# print("get captchas")
	# # 获取验证码
	# captcha = call_api({
	# "iw-apikey": 1234,
	# "iw-cmd": "getcaptchas",
	# "code": captchas_key
	# })
	# print("get catalogue")
	# # 获取板块信息
	# call_api({
	# "iw-apikey": 1234,
	# "iw-cmd": "getcatalogue"
	# })
	# print("post")
	# # 发布问题
	# post_url = call_api({
	# "iw-apikey": 1234,
	# "iw-cmd": "post",
	# "captcha_key": captchas_key,
	# "captcha": captcha,
	# "topic[forum_id]": "Enterprise_Other",
	# "topic[body]": description,
	# "topic[title]": title,
	# "topic[point]": 0,
	# "topic[cached_tag_list]": "",
	# "topic[invitation_usernames][]": "",
	# "authenticity_token": token
	# })
	# print(post_url)
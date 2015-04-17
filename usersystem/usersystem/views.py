
import random
import string
import httplib2
from urllib.parse import urlencode
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from usersystem.models import UserModel


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
	pass


def ask_question_at_csdn():
	pass
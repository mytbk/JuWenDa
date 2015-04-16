
import json
from django.contrib.auth import authenticate
from django.test import TestCase


def convert_json_response_to_dict(response):
	return json.loads(response.content.decode("utf-8"))


class UserTestCase(TestCase):
	def test_createUser(self):
		"""
		测试创建用户
			使用createUser创建一个用户
			验证返回的用户名和密码
			使用错误的用户名验证
			使用错误的密码验证
		"""
		response = self.client.post("/createUser",{"imei": ""})
		# 检查是否成功返回
		self.assertEqual(response.status_code, 200)
		result = json.loads(response.content.decode("utf-8"))
		username = result["username"]
		password = result["password"]
		# 检查是否可以使用返回的用户名和密码登录
		user = authenticate(username=username, password=password)
		self.assertIsNotNone(user)
		# 使用错误的用户名
		user = authenticate(username="", password=password)
		self.assertIsNone(user)
		# 使用错误的密码
		user = authenticate(username=username, password="")
		self.assertIsNone(user)

	def test_setPassword_success(self):
		"""
		测试更改密码，成功
			使用createUser创建一个用户
			使用setPassword更改密码，使用正确的密码操作成功
			尝试使用旧密码验证
			尝试使用新密码验证
		"""
		response = self.client.post("/createUser",{"imei": ""})
		result = convert_json_response_to_dict(response)
		# 检查是否成功返回
		self.assertEqual(response.status_code, 200)
		username = result["username"]
		password = result["password"]
		# 更改密码
		response = self.client.post("/setPassword", {
			"username": username,
			"old_password": password,
			"new_password": "test"
		})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["status"], 0)
		# 使用旧密码验证
		user = authenticate(username=username, password=password)
		self.assertIsNone(user)
		# 使用新密码验证
		user = authenticate(username=username, password="test")
		self.assertIsNotNone(user)

	def test_setPassword_fail(self):
		"""
		测试更改密码，失败（密码验证错误）
			使用createUser创建一个用户
			使用setPassword更改密码，使用错误的密码操作成功
			尝试使用旧密码验证
			尝试使用新密码验证
		"""
		response = self.client.post("/createUser",{"imei": ""})
		result = convert_json_response_to_dict(response)
		# 检查是否成功返回
		self.assertEqual(response.status_code, 200)
		username = result["username"]
		password = result["password"]
		# 更改密码
		response = self.client.post("/setPassword", {
			"username": username,
			"old_password": "",
			"new_password": "test"
		})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["status"], 1)
		# 使用旧密码验证
		user = authenticate(username=username, password=password)
		self.assertIsNotNone(user)
		# 使用新密码验证
		user = authenticate(username=username, password="test")
		self.assertIsNone(user)

	def test_setUsername_success(self):
		"""
		测试更改用户名，成功
			使用createUser创建一个用户
			更改该用户的用户名，使用正确的密码操作成功
			尝试使用旧用户名验证
			尝试使用新用户名验证
		"""
		response = self.client.post("/createUser",{"imei": ""})
		result = convert_json_response_to_dict(response)
		# 检查是否成功返回
		self.assertEqual(response.status_code, 200)
		username = result["username"]
		password = result["password"]
		# 更改用户名
		response = self.client.post("/setUsername", {
			"old_username": username,
			"new_username": "a new user",
			"password": password
		})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["status"], 0)
		# 使用旧用户名验证
		user = authenticate(username=username, password=password)
		self.assertIsNone(user)
		# 使用新用户名验证
		user = authenticate(username="a new user", password=password)
		self.assertIsNotNone(user)

	def test_setUsername_fail1(self):
		"""
		测试更改用户名，失败（密码验证错误）
			使用createUser创建一个用户
			更改该用户的用户名，使用错误的密码操作失败
			尝试使用旧用户名验证
			尝试使用新用户名验证
		"""
		response = self.client.post("/createUser",{"imei": ""})
		result = convert_json_response_to_dict(response)
		# 检查是否成功返回
		self.assertEqual(response.status_code, 200)
		username = result["username"]
		password = result["password"]
		# 更改用户名
		response = self.client.post("/setUsername", {
			"old_username": username,
			"new_username": "a new user",
			"password": ""
		})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["status"], 1)
		# 使用旧用户名验证
		user = authenticate(username=username, password=password)
		self.assertIsNotNone(user)
		# 使用新用户名验证
		user = authenticate(username="a new user", password=password)
		self.assertIsNone(user)

	def test_setUsername_fail2(self):
		"""
		测试更改用户名，失败（已存在的用户名）
			使用createUser创建两个用户
			更改第一个用户的用户名为第二个用户的用户名，操作失败
			尝试使用旧用户名验证第一个用户
			尝试使用新用户名验证第一个用户
		"""
		# 创建第一个用户
		response = self.client.post("/createUser",{"imei": ""})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		username1 = result["username"]
		password1 = result["password"]
		# 创建第二个用户
		response = self.client.post("/createUser",{"imei": ""})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		username2 = result["username"]
		# 更改用户名
		response = self.client.post("/setUsername", {
			"old_username": username1,
			"new_username": username2,
			"password": password1
		})
		result = convert_json_response_to_dict(response)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["status"], 2)
		# 使用旧用户名验证
		user = authenticate(username=username1, password=password1)
		self.assertIsNotNone(user)
		# 使用新用户名验证
		user = authenticate(username=username2, password=password1)
		self.assertIsNone(user)

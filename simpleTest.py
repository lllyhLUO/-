import requests

def main():
    response = requests.request(
        method='get',
        url='https://baidu.com',
        data={"a": 1, "b": 2, "c": 3}
    )
    print(response.status_code)
    print(response.headers)
    print(response.text)
    print(response.json())

    assert response.status_code == 200
    assert 'baidu' in response.text

# 测试表单
user_info = {
    'name': 'username',
    'password': '123456',
}
def test_api_form():

    resp = requests.request(
        method='post',
        url='https://httpbin.org/post', # 要保证这个网址是能够接受user_info字典格式的post请求才能通过
        data=user_info #就不用设置请求头了
    )
    assert resp.s

# 测试JSON
@pytest.mark.skip
def test_api_json():

    resp = requests.request(
        method='post',
        url='https://httpbin.org/post',
        json=user_info # json格式传参
    )
    assert resp.status_code == 200

# 测试文件上传
def test_file_upload():
    path = r"F:\codePython\autoTest\testPNG.png" # 没打开之前就是个字符串
    fileObj = open(path, 'rb') # 文件对象

    resp = requests.request(
        method= 'post',
        url = 'https://httpbin.org/post',
        files={'file': fileObj},
    )
    assert resp.status_code == 200

# 为什么要设置类？
class UserApi:
    # __init__ 是构造方法，创建实例时会自动执行，用来初始化属性
    def __init__(self, base_url):
        # 1.把传入的 base_url 绑定到 self（实例）上，成为实例属性
        self.base_url = base_url
        # 2.初始化 token 为 None, 后续登录后赋值
        self.token = None

    # 登录方法：给self.token 赋值
    def login(self, username, password):
        url = f"{self.base_url}/login"
        data = {"username": username, "password": password}
        resp = requests.post(url, json=data).json()
        # 登陆成功后，把token 存到self里面（共享给其他方法）
        self.token = resp.get("token")
        return resp

    # 登出方法：读取 self.token
    def logout(self):
        url = f"{self.base_url}/logout"
        # 直接通过 self.token 获取登录时保存的 token
        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.post(url, headers=headers).json()

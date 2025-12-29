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

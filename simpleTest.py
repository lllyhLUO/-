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

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

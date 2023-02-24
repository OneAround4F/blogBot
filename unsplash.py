import requests
import json


# https://unsplash.com/oauth/applications 에서 확인
access_key = 'YOUR_ACCESS_KEY'


def get_image():
    url = 'https://api.unsplash.com/photos/?' + 'client_id=' + access_key
    response = requests.get(url, verify=False)
    print(response.status_code)
    print(response.text)
    return response

# Test Code - 액세스 키 기반으로 이미지 뽑기
# get_image()


def random_image(query: str, count: str):  # 쿼리와 일치하는 랜덤 이미지 뽑기
    url = 'https://api.unsplash.com/photos/random?' + 'client_id=' + access_key
    parameters = {
        'query': query,
        'count': count,
    }
    response = requests.get(url, params=parameters, verify=False)
    print(response.status_code)
    print(response.text)
    json_object = json.loads(response.text)
    html_url = ''
    for i in range(int(count)):
        html_url += '<img src=' + json_object[i]['urls']['small'] + ' />\n'
    print(html_url)
    return html_url

# Test Code - 컴퓨터 사진 3개 랜덤 뽑기
# random_image('Computer', '3')

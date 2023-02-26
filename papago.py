import urllib.request
import json


client_key = [
    {'client_id': 'YOUR_CLIENT_ID_0', 'client_secret': 'YOUR_CLIENT_SECRET_0'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_2', 'client_secret': 'YOUR_CLIENT_SECRET_2'},
    {'client_id': 'YOUR_CLIENT_ID_3', 'client_secret': 'YOUR_CLIENT_SECRET_3'},
    {'client_id': 'YOUR_CLIENT_ID_4', 'client_secret': 'YOUR_CLIENT_SECRET_4'},
    {'client_id': 'YOUR_CLIENT_ID_5', 'client_secret': 'YOUR_CLIENT_SECRET_5'},
    {'client_id': 'YOUR_CLIENT_ID_6', 'client_secret': 'YOUR_CLIENT_SECRET_6'},
    {'client_id': 'YOUR_CLIENT_ID_7', 'client_secret': 'YOUR_CLIENT_SECRET_7'},
    {'client_id': 'YOUR_CLIENT_ID_8', 'client_secret': 'YOUR_CLIENT_SECRET_8'},
    {'client_id': 'YOUR_CLIENT_ID_9', 'client_secret': 'YOUR_CLIENT_SECRET_9'},
]


def run_translate(client_id: str, client_secret: str, english_text: str) -> str:  # 입력값 : CLIENT_ID, CLIENT_SECRET, 영어글
    print("영어글자수 : ", len(english_text))

    text = urllib.parse.quote(english_text)
    data = "source=en&target=ko&text=" + text  # 영어를 한글로 번역
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)

    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        response_decode = response_body.decode('utf-8')
        response_json = json.loads(response_decode)
        result = response_json['message']['result']['translatedText']
        print("한글글자수 : ", len(result))
        print(result)
        return result
    else:
        print("Error Code : " + rescode)

# Test Code - 영어 문장을 한글로 번역
# print(run_translate(client_key[0]['client_id'], client_key[0]['client_secret'], "I go to work every day."))

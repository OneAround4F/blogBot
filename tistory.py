import requests


# https://www.tistory.com/guide/api/manage/list > '설정' 클릭 > 아래에 각각 채워넣기
client_id = 'YOUR_APP_ID'  # APP ID 값
client_secret = 'YOUR_SECRET_KEY'  # Secret Key 값
redirect_uri = 'YOUR_SERVICE_URL'  # 서비스 URL 값


# Step1) 토큰을 받기 위한 code 알아내기
def get_auth_code():  # 인증코드를 받을 수 있는 URL 출력
    response_type = "code"
    state = "anything"
    url = 'https://www.tistory.com/oauth/authorize?' + \
          'client_id=' + client_id + '&' + \
          'redirect_uri=' + redirect_uri + '&' + \
          'response_type=' + response_type + '&' + \
          'state=' + state
    print(url)


# Test Code - 아래 코드 실행 후 나오는 URL을 크롬에서 접속 > '허가하기' 버튼 클릭 > 주소창에서 code 뒤에 보이는 값이 인증코드
# get_auth_code()


# Step2) 글쓰기에 필요한 토큰 발급받기
def get_access_token(code):  # 블로그 이름과 인증코드 기반으로 토큰 발급
    url = 'https://www.tistory.com/oauth/access_token?' + \
          'client_id=' + client_id + '&' + \
          'client_secret=' + client_secret + '&' + \
          'redirect_uri=' + redirect_uri + '&' + \
          'code=' + code + '&' + \
          'grant_type=authorization_code'
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        print("토큰 받기 성공")
    else:
        print("토큰 받기 실패")
    print(response.status_code)
    print(response.text)


# Test Code - 전 단계에서 알아낸 인증코드 기반으로 아래 코드 실행 > 출력 결과가 토큰 값
# get_access_token('YOUR_AUTH_CODE')


# Step3) 발급받은 토큰 값을 아래에 채워넣기
token = 'YOUR_TOKEN'


# Step4) 토큰 이용해서 티스토리에 글쓰기
def post_blog(title, content, tag, expose, blog_name):
    url = 'https://www.tistory.com/apis/post/write?'
    visibility = '3' if expose else '0'  # expose 값이 True: 공개(3), False: 비공개(0) 세팅
    parameters = {
        'access_token': token,
        'output': '{output-type}',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'tag': tag,
        'visibility': visibility,
    }
    response = requests.post(url, params=parameters, verify=False)

    if response.status_code == 200:
        print("글작성 성공")
    else:
        print("글작성 실패")
    print(response.status_code)
    print(response.text)


# Test Code - 입력값 : 제목, 내용, 태그, 노출 여부, 블로그 이름(https://YOUR_BLOG_NAME.tistory.com)
# post_blog("제목", "내용", "태그", False, 'YOUR_BLOG_NAME')

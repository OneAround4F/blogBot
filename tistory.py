import requests


# Step1) https://www.tistory.com/guide/api/manage/register 에서 확인해서 채워넣기 (여러 개의 티스토리 블로그 운영한다고 가정)
key = [
    {'blogName': 'YOUR_BLOG_NAME_1', 'app_id': 'YOUR_APP_ID_1', 'secret_key': 'YOUR_SECRET_KEY_1'},
    {'blogName': 'YOUR_BLOG_NAME_2', 'app_id': 'YOUR_APP_ID_2', 'secret_key': 'YOUR_SECRET_KEY_2'},
    {'blogName': 'YOUR_BLOG_NAME_3', 'app_id': 'YOUR_APP_ID_3', 'secret_key': 'YOUR_SECRET_KEY_3'},
]


def id_and_key(text: str) -> list:  # 블로그 이름과 일치하는 App ID, Secret Key 리스트 불러오는 함수
    for i in range(len(key)):
        blog_name = key[i]['blogName']
        li = []
        if blog_name == text:
            li.append(key[i]['app_id'])
            li.append(key[i]['secret_key'])
            print(li)
            return li

# Test Code - YOUR_BLOG_NAME_1 에 해당하는 블로그의 App ID, Secret Key 가져오기
# id_and_key('YOUR_BLOG_NAME_1')


# Step2) 토큰을 받기 위한 code 알아내기
def get_auth_code(blog_name: str):  # 블로그 이름과 App ID 기반으로 인증코드를 받을 수 있는 URL 출력
    response_type = "code"
    state = "anything"
    client_id = id_and_key(blog_name)[0]
    redirect_uri = 'https://' + blog_name + '.tistory.com'
    url = 'https://www.tistory.com/oauth/authorize?' + \
          'client_id=' + client_id + '&' + \
          'redirect_uri=' + redirect_uri + '&' + \
          'response_type=' + response_type + '&' + \
          'state=' + state
    print(url)


# Test Code - 아래 코드 실행 후 나오는 URL을 크롬에서 접속 > '허가하기' 버튼 클릭 > 주소창에서 code 뒤에 보이는 값이 인증코드
# get_auth_code('YOUR_BLOG_NAME_1')


# Step3) 글쓰기에 필요한 토큰 발급받기
def get_access_token(blog_name: str, code: str):  # 블로그 이름과 인증코드 기반으로 토큰 발급
    client_id = id_and_key(blog_name)[0]
    client_secret = id_and_key(blog_name)[1]
    redirect_uri = 'https://' + blog_name + '.tistory.com'
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


# Test Code - 2번 단계에서 알아낸 인증코드 기반으로 아래 코드 실행 > 출력 결과가 토큰 값
# code = 'GET_CODE_BY_AUTH'
# get_access_token('YOUR_BLOG_NAME_1', code)


# Step4) 발급받은 토큰 값을 아래 함수에 채워넣기
def token_value(text: str) -> str:
    if text == 'YOUR_BLOG_NAME_1':
        return 'YOUR_TOKEN_1'
    elif text == 'YOUR_BLOG_NAME_2':
        return 'YOUR_TOKEN_2'
    elif text == 'YOUR_BLOG_NAME_3':
        return 'YOUR_TOKEN_3'


# Step5) 토큰 이용해서 티스토리에 글쓰기
def post_blog(title: str, content: str, tag: str, expose: bool, blog_name: str):
    url = 'https://www.tistory.com/apis/post/write?'
    visibility = '3' if expose else '0'  # expose 값이 True면 '3' 세팅하고 False면 '0' 세팅
    parameters = {
        'access_token': token_value(blog_name),  # 토큰 값
        'output': '{output-type}',  # 선택 옵션
        'blogName': blog_name,  # 블로그 이름
        'title': title,  # 게시글 제목
        'content': content,  # 게시글 내용
        'tag': tag,  # 태그
        'visibility': visibility,  # 게시글 노출 여부(0:비공개, 3:공개)
    }
    response = requests.post(url, params=parameters, verify=False)

    if response.status_code == 200:
        print("글작성 성공")
    else:
        print("글작성 실패")
    print(response.status_code)
    print(response.text)

# Test Code - 입력값 : 제목, 내용, 태그, 노출 여부, 블로그 이름
# post_blog("제목", "내용", "태그", False, 'YOUR_BLOG_NAME_1')

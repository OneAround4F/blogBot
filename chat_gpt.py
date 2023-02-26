import openai


# https://platform.openai.com/account/api-keys 에서 확인
openai.api_key = 'YOUR_OPENAI_KEY'


def make_subject(keyword: str, count: str) -> list:  # 입력값 : 키워드, 개수
  question = f"I will make blog articles about {keyword}. Please make {count} topics without numbering. And separate it with commas with no new line."  # 주제 뽑을때 리스트 형식으로 요구
  print("질문 : ", question)
  response = openai.Completion.create(
    model="text-davinci-003",  # openAI의 모델 선택 (다빈치가 가장 발전한 모델)
    prompt=question,  # 질문할 텍스트
    temperature=0.7,  # 온도가 높을수록 창의적인 답변
    max_tokens=4000,  # 토큰 최대 사용 개수 (토큰은 사용한 금액을 의미)
    top_p=1.0,  # 샘플링 통계 확률
    frequency_penalty=0.0,  # 반복 패널티 (같은 얘기 반복 금지)
    presence_penalty=0.0  # 존재 패널티 (동일한 주제 반복 금지)
  )
  li = response['choices'][0]['text'].strip()  # 응답 결과 중 텍스트만 저장
  subject_list = list(li.replace(", ", ",").split(","))  # 문자열을 쉼표 기준으로 분리하여 리스트에 저장
  return subject_list

# Test Code - 음악 키워드로 주제 3개 뽑기
# print(make_subject("Music", '3'))


def make_article(subject: str, number: str) -> str:  # 입력값 : 주제, 글자수
  question = f"Write a long blog article about {subject} around {number} words in markdown format. And include subtitles and detail description."  # 주제에 관한 게시글을 마크다운 형식으로 요구
  print("질문 : ", question)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  article = response['choices'][0]['text']
  return article

# Test Code - 한국의 유명한 가수라는 주제로 2000자 내외 글쓰기
# print(make_article("Famous Singer in Korea", '2000'))


def make_tag(text: str, count: str) -> str:  # 입력값 : 텍스트, 개수
  question = f"I'm writing a blog article. And article's title is {text}. Please make {count} tags that goes well with this article. And separate it with comma. And leave out # symbol."  # 글 제목과 어울리는 태그 뽑기
  print("질문 : ", question)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  tag = response['choices'][0]['text']
  return tag

# Test Code - 한국의 유명한 가수와 어울리는 태그 5개 뽑기
# print(make_tag("Famous Singer in Korea", '5'))

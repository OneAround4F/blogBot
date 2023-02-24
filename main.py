import markdown
import tistory
import chat_gpt
import unsplash
import papago

# https://YOUR_BLOG_NAME.tistory.com
blog_name = 'YOUR_BLOG_NAME'  # 티스토리 블로그 이름


# 키워드 기반으로 자동 글쓰기
def post_blog_by_keyword(keyword: str, count: str, expose: bool, isKorean: bool):  # 입력값 : 주제, 작성 개수, 게시글 노출 여부, # 언어 설정

    # 키워드 기반으로 주제 n개 뽑기
    subject_keyword = keyword  # 키워드
    subject_number = count  # 뽑을 주제 개수
    subject_result = chat_gpt.make_subject(subject_keyword, subject_number)  # 키워드와 연관된 주제 뽑기
    print("주제 리스트 : ", subject_result)

    # 주제에 어울리는 글 작성
    article_list = []
    if isKorean:
        article_words = '400'  # 한글 블로그 글자수
    else:
        article_words = '2000'  # 영문 블로그 글자수

    for item in subject_result:
        article_result = chat_gpt.make_article(item, article_words)  # 주제 기반으로 게시글 작성
        article_list.append(article_result)
    print("게시글 리스트 : ", article_list)

    for i in range(len(subject_result)):
        title = subject_result[i]
        article = article_list[i]
        tag = chat_gpt.make_tag(title, '4')  # 태그 4개 생성
        img = unsplash.random_image(title, '5')  # 제목과 어울리는 이미지 찾기

        if isKorean:  # 한글을 선택한 경우
            title = papago.run_translate(papago.client_key[i]['client_id'], papago.client_key[i]['client_secret'], title)  # 제목 번역
            article = papago.run_translate(papago.client_key[i]['client_id'], papago.client_key[i]['client_secret'], article)  # 게시글 번역
            tag = ""  # 태그 미첨부 (요청 길이 제한)
            img = ""  # 이미지 미첨부 (요청 길이 제한)

            if len(article) > 1000:  # 한글 본문 길이가 길면 뒷부분 제거
                article_slice = article[:1000]
                article = article_slice
                print("After slicing : ", len(article))

        blog_sum = img + article  # 이미지와 게시글 내용을 합치기
        html = markdown.markdown(blog_sum)  # 마크다운 -> HTML
        print("length of html : ", len(html))
        tistory.post_blog(title, html, tag, expose, blog_name)  # 티스토리 글쓰기


if __name__ == '__main__':
    # '성공적인 투자 방법'이라는 키워드로 공개 게시글 영문으로 5개 작성
    post_blog_by_keyword(keyword='Successful investment method', count='5', expose=True, isKorean=False)

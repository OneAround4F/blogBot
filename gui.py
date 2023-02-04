import tkinter as tk
import main


def btn_start():  # 하단 버튼 눌렀을때 실행
    text = entry.get()
    main.post_blog_by_keyword(str(text), str(spin_value.get()), radio_expose(), radio_language())


def radio_expose():  # 라디오 버튼 - 공개 여부
    selected = radio_expose_var.get()
    return selected


def radio_language():  # 라디오 버튼 - 언어 설정
    selected = radio_language_var.get()
    return selected


root = tk.Tk()
root.title("blogBot v1.0")
root.geometry("300x400")

tk.Label(text="\n블로그 주제 (영어로 입력)").pack()
entry = tk.Entry(root, width=30)
entry.pack()

tk.Label(text="\n포스팅 개수").pack()
spin_value = tk.IntVar()
spin_value.set(3)
spin = tk.Spinbox(root, from_=1, to=50, width=10, textvariable=spin_value)
spin.pack()

tk.Label(text="\n포스팅 설정").pack()
radio_expose_var = tk.BooleanVar()
radio_expose_y = tk.Radiobutton(root, text="공개", variable=radio_expose_var, value=True, command=radio_expose)
radio_expose_y.pack()
radio_expose_n = tk.Radiobutton(root, text="비공개", variable=radio_expose_var, value=False, command=radio_expose)
radio_expose_n.pack()

tk.Label(text="\n언어 설정").pack()
radio_language_var = tk.BooleanVar()
radio_language_korean = tk.Radiobutton(root, text="한글", variable=radio_language_var, value=True, command=radio_language)
radio_language_korean.pack()
radio_language_english = tk.Radiobutton(root, text="영어", variable=radio_language_var, value=False, command=radio_language)
radio_language_english.pack()

tk.Label(text="\n").pack()
button = tk.Button(root, text="글쓰기 시작", command=btn_start)
button.pack()

root.mainloop()

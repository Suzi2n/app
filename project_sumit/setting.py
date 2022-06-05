import tkinter as tk

window=tk.Tk()
window.title("setting")

l1=tk.Label(window, text="장르를 선택하세요")
l1.pack()

genre_var = tk.IntVar()
button_genre0=tk.Radiobutton(window, text='발라드', value=0, variable=genre_var).pack()
button_genre1=tk.Radiobutton(window, text='아이돌(남자)', value=1, variable=genre_var).pack()
button_genre2=tk.Radiobutton(window, text='아이돌(여자)', value=2, variable=genre_var).pack()
button_genre3=tk.Radiobutton(window, text='OST(국내)', value=3, variable=genre_var).pack()
button_genre4=tk.Radiobutton(window, text='OST(국외)', value=4, variable=genre_var).pack()
button_genre5=tk.Radiobutton(window, text='J-POP', value=5, variable=genre_var).pack()
button_genre6=tk.Radiobutton(window, text='댄스', value=6, variable=genre_var).pack()
button_genre7=tk.Radiobutton(window, text='클래식', value=7, variable=genre_var).pack()
button_genre8=tk.Radiobutton(window, text='POP', value=8, variable=genre_var).pack()
button_genre9=tk.Radiobutton(window, text='록/메탈(국내)', value=9, variable=genre_var).pack()
button_genre10=tk.Radiobutton(window, text='록/메탈(국외)', value=10, variable=genre_var).pack()
button_genre11=tk.Radiobutton(window, text='포크/블루스/컨트리', value=11, variable=genre_var).pack()
button_genre12=tk.Radiobutton(window, text='인디', value=12, variable=genre_var).pack()
button_genre13=tk.Radiobutton(window, text='뉴에이지', value=13, variable=genre_var).pack()
button_genre14=tk.Radiobutton(window, text='재즈', value=14, variable=genre_var).pack()

b1=tk.Button(window, text="선택")
b1.pack()

window.mainloop()

def get_taste():
    return genre_var.get()

taste=get_taste()

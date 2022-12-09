# Задание №4
# RLE алгоритм шифрования + небольшая формочка на tkinter
# пример для проверки: AAAAAAAAhtungG78

import tkinter as tk


def encode():
    user = text.get()
    text.delete(0, tk.END)
    result = ""
    preChar = ''
    count = 1
    for index, char in enumerate(user):
        if index == 0:
            preChar = char
            continue

        if preChar == char:
            count += 1
            if index == len(user) - 1:
                result += f"{count}{preChar}"
        else:
            if index != len(user) - 1:
                result += f"{count}{preChar}"
                count = 1
            else:
                result += f"{count}{preChar}1{char}"

        if count >= 10:
            result += f"9{preChar}"
            count -= 9

        preChar = char
    text.insert(0, result)


def decode():
    user = text.get()
    text.delete(0, tk.END)
    result = ""
    user = list(user)
    amounts = []
    chars = []
    for char in user[::2]:
        if char is not None:
            amounts.append(char)
    for char in user[1::2]:
        if char is not None:
            chars.append(char)
    for index, amount in enumerate(amounts):
        for i in range(int(amount)):
            result += chars[index]

    text.insert(0, result)


win = tk.Tk()
win.geometry(f'480x150+600+400')
win.title('Шифратор')

text = tk.Entry(win, font=('Arial', 14))

tk.Label(win, text="Поле для ввода текста", font=('Arial', 12), fg='red', pady=10).grid(row=0, column=0, columnspan=2)
btn1 = tk.Button(win, text="Зашифровать", command=encode, width=30, height=2)
btn2 = tk.Button(win, text="Расшифровать", command=decode, width=30, height=2)

text.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=10)
btn1.grid(row=2, column=0, padx=10, pady=5)
btn2.grid(row=2, column=1, padx=10, pady=5)

win.mainloop()

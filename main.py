import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os

def file_select():
    file_name = fd.askopenfilename(initialdir='/', title='Выберите файл',
                                   filetypes=(('Текстовый файл', '.txt'),
                                              ('Все файлы', '* ')))
    if file_name != '':
        ent_FileName.delete(0, last='end')
        ent_FileName.insert(0, file_name)
        os.startfile(file_name)

def window_close():
    window.destroy()

if __name__ == '__main__':
    window = tk.Tk()       # создаем экземпляр класса
    window.title('Проводник')
    window.iconbitmap(default='applications.ico')
    window.geometry('700x85')
    window.configure(bg='lightblue')

    main_menu = tk.Menu()

    file_menu = tk.Menu(tearoff=0)
    file_menu.add_command(label='Open file', command=file_select)
    file_menu.add_separator()
    file_menu.add_command(label='Close', command=window_close)


    main_menu.add_cascade(label='File', menu=file_menu)

    window.config(menu=main_menu)


    lbl_NameFile = ttk.Label(text="Имя файла:")
    lbl_NameFile.grid(row=0, column=0, padx=5, pady=10)

    ent_FileName = ttk.Entry(text='', width=100)
    ent_FileName.grid(row=0, column=1, columnspan=3, padx=5)

    btn_OpenFile = ttk.Button(window, text='Open File', width=15, command=file_select)
    btn_Close = ttk.Button(text = 'Close', width=15, command=window_close)

    btn_OpenFile.grid(row=1, column=3, padx=5, pady=10, sticky='w')
    btn_Close.grid(row=1, column=3, padx=5, pady=10, sticky='e')

    window.resizable(False, False)

    window.mainloop()           # цикл обновления окна
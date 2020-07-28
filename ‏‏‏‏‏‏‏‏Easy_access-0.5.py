import tkinter as tk
import tkinter.font
import os

PyCh = r"C:\Users\Owner\Desktop\PyCharm Community Edition 2020.1 x64"
spot = r"C:\Users\Owner\AppData\Roaming\Spotify\Spotify.exe"
new_file = r"C:\Users\Owner\Desktop\python\קובץ .py"
name_f_p = "new_file_in_new_project.py"
open_f = new_file + r"\new_file.py"

os.chdir(new_file)


def pyt_new_dir():
    string = txt_1.get()

    try:
        os.mkdir(string)
        os.chdir(r"C:\Users\Owner\Desktop\python\קובץ .py\%s" % string)
        txt_1.delete(0, tk.END)

    except:
        os.chdir(r"C:\Users\Owner\Desktop\python\קובץ .py\%s" % string)
        txt_1.delete(0, tk.END)
        os.system(r"explorer C:\Users\Owner\Desktop\python\קובץ .py\%s" % string)
        

def pyt_new_file():
    string = txt_1.get()

    if string == "" or string == "The project opened ":
        os.system("dir > %s" % f"new_file_in_new_project.py")


    else:
        os.system("dir > %s" % string + ".py")

    txt_1.delete(0, tk.END)


root = tk.Tk()
root.title("Easy access")

font_buttons = tkinter.font.Font(root, family='Arial', size=20, weight='bold')

for i in range(5):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

txt_1 = tk.Entry(root, fg="blue", font="Courier 40 bold", justify='right')
txt_1.grid(row=0, column=0, columnspan=5, sticky='NESW')

btn1 = tk.Button(root, text="New project", fg="blue", font=font_buttons, command=pyt_new_file)
btn1.grid(row=1, column=0, columnspan=2, sticky='NESW')

btn2 = tk.Button(root, text="New dir", fg="blue", font=font_buttons, command=pyt_new_dir)
btn2.grid(row=1, column=3, columnspan=2, sticky='NESW')

btn_3 = tk.Button(root, text="NEW", fg="green", font=font_buttons, command=lambda: txt_1.insert(tk.END, "new"))
btn_3.grid(row=1, column=2, sticky='NESW')


btn_c = tk.Button(root, text="clear", fg="red", font=font_buttons, command=lambda: txt_1.delete(0, tk.END))
btn_c.grid(row=2, column=0, columnspan=5, sticky='NESW')

root.mainloop()

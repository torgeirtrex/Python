import tkinter.simpledialog as tkSimpleDialog # python 3.x
import tkinter as teek

root = teek.Tk()

BookTitle = tkSimpleDialog.askstring("Select username","Please write in your emailadress")
if BookTitle is not None:
        bookTitle = '\n' + BookTitle
        books = open('users.txt', 'a')
        books.write(bookTitle)
        books.close()

SetPassword = tkSimpleDialog.askstring("Select password","Please write in your chosen password?")
if SetPassword is not None:
        chosepaasword = '\n' + SetPassword
        books = open('users.txt', 'a')
        books.write(chosepaasword)
        books.close()

frame = teek.Frame(root, bg='#80c1ff', bd=5)
#frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = teek.Entry(frame, font=40)
#entry.place(relwidth=0.65, relheight=1)


root.mainloop()
from tkinter import *

class MyWindow:
    def __init__(self, win):
        # widgets start from here
        self.lbl_title = Label(win, text="My Full Name", font=('Arial', 10,))
        self.lbl_title.place(x=200, y=20)

        self.lbl1 = Label(win, text="Enter Given Name:")
        self.lbl1.place(x=100, y=80)
        self.lbl2 = Label(win, text="Enter Middle Name:")
        self.lbl2.place(x=100, y=130)
        self.lbl3 = Label(win, text="Enter Last Name:")
        self.lbl3.place(x=100, y=180)

        self.lbl4 = Label(win, text="My Full Name is:")
        self.lbl4.place(x=100, y=230)

        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=300, y=80)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=300, y=130)
        self.txt3 = Entry(win, bd=1)
        self.txt3.place(x=300, y=180)

        self.txt4 = Entry(win, bd=3, width= 30)
        self.txt4.place(x=300, y=230)

        self.show_full_name()

        self.btnshow = Button(win, text="Show Full Name", command=self.show_full_name)
        self.btnshow.place(x=250, y=280, anchor=CENTER)

    # add event-handling /bind () method
    def show_full_name(self):
        full_name = "{} {} {}".format(self.txt1.get(), self.txt2.get(), self.txt3.get())
        self.txt4.delete(0, 'end')
        self.txt4.insert(END, full_name)

window = Tk()
mywin = MyWindow(window)
window.geometry("600x600+20+20")
window.title("Midterm Exam Problem 2")
window.mainloop()

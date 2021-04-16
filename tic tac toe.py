from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")
root.maxsize(width=410,height=420)
root.minsize(width=410,height=420)
bclick=True
flag=0
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def btnclick(button):
    global bclick,flag;
    if button['text']=="" and bclick==True:
        button["text"]="X"
        bclick=False
        checkForWin()
        flag+=1
    elif button['text']=="" and bclick==False:
        button["text"]="0"
        bclick=True
        checkForWin()
        flag+=1
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe","Button already clicked")
def checkForWin():
    if button1['text']=="X" and button2['text']=="X" and button3['text']=="X" or button4['text']=="X" and button5['text']=="X" and button6['text']=="X" or button7['text'] == "X" and button8['text'] == "X"and button9['text'] == "X" or button1['text']=="X" and button4['text']=="X" and button7['text']=="X" or button3['text']=="X" and button5['text']=="X" and button7['text']=="X" or button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X" or button3['text']=="X" and button6['text']=="X" and button9['text']=="X" or button1['text']=="X" and button5['text']=="X" and button9['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("Tic Tac Toe","Win")
    elif flag==8:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It's a Tie")
    elif button1['text']=="0" and button2['text']=="0" and button3['text']=="0" or button4['text']=="0" and button5['text']=="0" and button6['text']=="0" or button7['text'] == "0" and button8['text'] == "0"and button9['text'] == "0" or button1['text']=="0" and button4['text']=="0" and button7['text']=="0" or button3['text']=="0" and button5['text']=="0" and button7['text']=="0" or button2['text'] == "0" and button5['text'] == "0" and button8['text'] == "0" or button3['text']=="0" and button6['text']=="0" and button9['text']=="0" or button1['text']=="0" and button5['text']=="0" and button9['text']=="0":
        disableButton()
        tkinter.messagebox.showinfo("Tic Tac Toe", "Win")
button1=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button1))
button1.grid(row=3,column=0)
button2=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button2))
button2.grid(row=3,column=1)
button3=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button3))
button3.grid(row=3,column=2)
button4=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button4))
button4.grid(row=4,column=0)
button5=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button5))
button5.grid(row=4,column=1)
button6=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button6))
button6.grid(row=4,column=2)
button7=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button7))
button7.grid(row=5,column=0)
button8=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button8))
button8.grid(row=5,column=1)
button9=Button(root,text="",font=("Times",20,"bold"),bg="grey",fg="white",
               height=4 ,width=8,command=lambda:btnclick(button9))
button9.grid(row=5,column=2)
root.mainloop()



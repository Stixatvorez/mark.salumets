from tkinter import*
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
    aken.geometry(str(aken.winfo_width()+10)+"x"+str(aken.winfo_height()+10))
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
    aken.geometry(str(aken.winfo_width()-10)+"x"+str(aken.winfo_height()-10))
def txt_to_lbl(event):
    #pass
    text=txt.get()#From Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_) 
def vih(event):
    akno.destroy()
def callback(event):
    global Mousewheel
def popa(event):
    global klik 
    klik=0
    lbl.configure(text=klik)
#aken.destroy()

aken=Tk()
aken.title("welcome to the club buddy")
aken.geometry("400x600")
nupp=Button(aken,text="Mina olen nupp\nValjuta mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
nupp1=Button(aken,text="Sbros",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
nupp.bind("<Button-1>",klikker)#LKM
nupp.bind("<Button-3>",klikker_minus)#PKM
nupp1.bind("<Button-1>",popa)
nupp.bind("<MouseWheel>",callback)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightblue")
txt=Entry(aken,width=20,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
i1=PhotoImage(file="kish.png")
i2=PhotoImage(file="Homer.png")
i3=PhotoImage(file="spongebob.png")
var=StringVar()
var.set(1)
r1=Radiobutton(aken,image=i1,variable=var,value="1",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="2",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="3",command=valik)


lbl.pack()
nupp.pack()#side=LEFT,TOP,RIGHT
nupp1.pack()
txt.pack()
r1.pack()
r2.pack()
r3.pack()


aken.mainloop()

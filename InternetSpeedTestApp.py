from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downl=str( round(sp.download()/(10**6),3))+"Mbps"
    upl=str( round(sp.upload()/(10**6),3))+"Mbps"
    lab_downl.config(text=downl)
    lab_upl.config(text=upl)

sp=Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="indigo")

lab=Label(sp,text="Internet Speed",font=("Times New Roman",30,"bold"),bg="Blue",fg="Red")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="Download Speed",font=("Times New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_downl=Label(sp,text="00",font=("Times New Roman",30,"bold"),bg="yellow")
lab_downl.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="Upload Speed",font=("Times New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_upl=Label(sp,text="00",font=("Times New Roman",30,"bold"),bg="yellow")
lab_upl.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Times New Roman",30,"bold"),relief=RAISED,bg="cyan",command=speedCheck)
button.place(x=60,y=460,height=50,width=380)
sp.mainloop()

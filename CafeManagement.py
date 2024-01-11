from tkinter import *
import random
from datetime import datetime
from PIL import Image, ImageTk

root=Tk()
root.geometry("1200x650+100+20")
root.title("JECRC CAFE MANAGEMENT SYSTEM")

f= Frame(root,bd=10,relief=GROOVE)
f.pack(side=TOP)

f1=Frame(root ,bd=5,height=400,width=300,relief=RAISED)
f1.pack(side=LEFT,fill="both",expand=1)

f2=Frame(root,bd=5,height=400,width=300,relief=RAISED)

image=Image.open('logo2.png')
tk_image=ImageTk.PhotoImage(image.resize((150,120)))

lbl_info= Label(f,font=('aria',30,'bold'),text="JECRC CAFE MANAGEMENT SYSTEM",image=tk_image,fg="white",bg='light green',width=1150,compound='left')
lbl_info.grid(row=0,column=0)

now=datetime.now()
localtime= now.strftime("%d/%m/%Y %H:%M:%S")

tea=StringVar()
Cofee=StringVar()
Pasta=StringVar()
Sandwhich=StringVar()
Dosa=StringVar()
VegRoll=StringVar()
Noodles=StringVar()
rand=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Tax=StringVar()
cost=StringVar()
date=StringVar()


image=Image.open('tea.png')
tk_image1=ImageTk.PhotoImage(image.resize((40,40)))
image=Image.open('Cofee.png')
tk_image2=ImageTk.PhotoImage(image.resize((40,40)))
image=Image.open('Pasta.png')
tk_image3=ImageTk.PhotoImage(image.resize((40,40)))
image=Image.open('Dosa.png')
tk_image4=ImageTk.PhotoImage(image.resize((40,40)))
image=Image.open('Sandwhich.png')
tk_image5=ImageTk.PhotoImage(image.resize((40,40)))
image=Image.open('VegRoll.png')
tk_image6=ImageTk.PhotoImage(image.resize((40,40)))
image=Image.open('Noodles.png')
tk_image7=ImageTk.PhotoImage(image.resize((40,40)))



lbl_tea=Label(f1,font=('aria',20,'bold'),text='Tea',image=tk_image1,width=200,fg="Black",bg="white",compound='left')
lbl_tea.grid(row=1,column=0)
txt_tea=Entry(f1,font=('ariel',20,'bold'),textvariable=tea,bd=6,width=8,bg='misty rose')
txt_tea.grid(row=1,column=1)

lbl_Cofee=Label(f1,font=('aria',20,'bold'),text='Coffee',image=tk_image2,width=200,fg="Black",bg="white",compound='left')
lbl_Cofee.grid(row=2,column=0)
txt_Cofee=Entry(f1,font=('ariel',20,'bold'),textvariable=Cofee,bd=6,width=8,bg='misty rose')
txt_Cofee.grid(row=2,column=1)

lbl_Pasta=Label(f1,font=('aria',20,'bold'),text='Pasta',image=tk_image3,width=200,fg="Black",bg="white",compound='left')
lbl_Pasta.grid(row=3,column=0)
txt_Pasta=Entry(f1,font=('ariel',20,'bold'),textvariable=Pasta,bd=6,width=8,bg='misty rose')
txt_Pasta.grid(row=3,column=1)

lbl_Dosa=Label(f1,font=('aria',20,'bold'),text='Dosa',image=tk_image4,width=200,fg="Black",bg="white",compound='left')
lbl_Dosa.grid(row=4,column=0)
txt_Dosa=Entry(f1,font=('ariel',20,'bold'),textvariable=Dosa,bd=6,width=8,bg='misty rose')
txt_Dosa.grid(row=4,column=1)

lbl_Sandwhich=Label(f1,font=('aria',20,'bold'),text='Sandwich',image=tk_image5,width=200,fg="Black",bg="white",compound='left')
lbl_Sandwhich.grid(row=5,column=0)
txt_Sandwhich=Entry(f1,font=('ariel',20,'bold'),textvariable=Sandwhich,bd=6,width=8,bg='misty rose')
txt_Sandwhich.grid(row=5,column=1)

lbl_VegRoll=Label(f1,font=('aria',20,'bold'),text='Veg Roll',image=tk_image6,width=200,fg="Black",bg="white",compound='left')
lbl_VegRoll.grid(row=6,column=0)
txt_VegRoll=Entry(f1,font=('ariel',20,'bold'),textvariable=VegRoll,bd=6,width=8,bg='misty rose')
txt_VegRoll.grid(row=6,column=1)

lbl_Noodles=Label(f1,font=('aria',20,'bold'),text='Noodles',image=tk_image7,width=200,fg="Black",bg="white",compound='left')
lbl_Noodles.grid(row=7,column=0)
txt_Noodles=Entry(f1,font=('ariel',20,'bold'),textvariable=Noodles,bd=6,width=8,bg='misty rose')
txt_Noodles.grid(row=7,column=1)

def generate_bill():
     bill_no=str(random.randint(15000,50000))
     rand.set(bill_no)
     date.set(localtime)
     try: qt=int(tea.get())
     except:qt=0
     try: qc=int(Cofee.get())
     except:qc=0
     try: qp=int(Pasta.get())
     except:qp=0
     try: qd=int(Dosa.get())
     except:qd=0
     try: qs=int(Sandwhich.get())
     except:qs=0
     try: qv=int(VegRoll.get())
     except:qv=0
     try: qn=int(Noodles.get())
     except:qn=0


     costoftea= qt*10
     costofcofee= qc*50
     costofpasta= qp*90
     costofdosa= qd*80
     costofsandwhich= qs*40
     costofvegroll= qv*50
     costofnoodles= qn*60

     f2.pack(side=RIGHT,fill="both",expand=1)
     f2.configure(background="light yellow")

     lbl_bill=Label(f2,font=('aria',18,'bold'),text="Bill No.",bg="light yellow",width=12,bd=20)
     lbl_bill.grid(row=1,column=0)
     txt_bill=Entry(f2,font=('ariel',18,'bold'),textvariable=rand,bd=6,width=17,bg='misty rose')
     txt_bill.grid(row=1,column=1)

     lbl_date=Label(f2,font=('aria',18,'bold'),text="Date",bg="light yellow",width=12,bd=20)
     lbl_date.grid(row=2,column=0)
     txt_date=Entry(f2,font=('ariel',18,'bold'),textvariable=date,bd=6,width=17,bg='misty rose')
     txt_date.grid(row=2,column=1)

     lbl_cost=Label(f2,font=('aria',18,'bold'),text="Cost", bg="light yellow",width=12,bd=20)
     lbl_cost.grid(row=3,column=0)
     txt_cost=Entry(f2,font=('ariel',18,'bold'),textvariable=cost,bd=6,width=17,bg='misty rose')
     txt_cost.grid(row=3,column=1)

     lbl_service=Label(f2,font=('aria',18,'bold'),text="Service Charge", bg="light yellow",width=12,bd=20)
     lbl_service.grid(row=4,column=0)
     txt_service=Entry(f2,font=('ariel',18,'bold'),textvariable=Service_Charge,bd=6,width=17,bg='misty rose')
     txt_service.grid(row=4,column=1)

     lbl_tax=Label(f2,font=('aria',18,'bold'),text="Tax", bg="light yellow",width=12,bd=20)
     lbl_tax.grid(row=5,column=0)
     txt_tax=Entry(f2,font=('ariel',18,'bold'),textvariable=Tax,bd=6,width=17,bg='misty rose')
     txt_tax.grid(row=5,column=1)

     lbl_total=Label(f2,font=('aria',18,'bold'),text="Total", bg="light yellow",width=12,bd=20)
     lbl_total.grid(row=6,column=0)
     txt_total=Entry(f2,font=('ariel',18,'bold'),textvariable=Total,bd=6,width=17,bg='misty rose')
     txt_total.grid(row=6,column=1)
     
     Totalcost= costoftea + costofcofee + costofpasta + costofdosa + costofsandwhich + costofvegroll + costofnoodles
     costofmeal= "Rs.",str('%.2f' %Totalcost)
     payTax=(Totalcost*0.18)
     paidTax="Rs.",str('%.2f' %payTax)
     ser_charge=(Totalcost*0.01)
     service="Rs.",str('%.2f' %ser_charge)
     overall= payTax + Totalcost + ser_charge
     total="Rs.",str('%.2f'%overall)

     Service_Charge.set(service)
     cost.set(costofmeal)
     Tax.set(paidTax)
     Total.set(total)


def qexit():
     root.destroy()



def reset():
     tea.set('')
     Cofee.set('')
     Pasta.set('')
     Dosa.set('')
     Sandwhich.set('')
     VegRoll.set('')
     Noodles.set('')    


def price():
    roo = Tk()
    roo.geometry("600x320+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="TEA", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="COFFEE ", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PASTA", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="90", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="DOSA ", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="80", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SANDWICH", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="VEGROLL", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="NOODLES", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)


    roo.mainloop()

btn_Total= Button(f1,bd=5,fg='black',font=('ariel',16,'bold'),width=14,text="CALCULATE BILL",bg="SteelBlue1",command=generate_bill)
btn_Total.grid(row=9,column=0,padx=10,pady=10)

btn_reset= Button(f1,bd=5,fg='black',font=('ariel',16,'bold'),width=10,text="RESET",bg="SteelBlue1",command=reset)
btn_reset.grid(row=9,column=1,padx=10,pady=10)

btn_exit= Button(f1,bd=5,fg='black',font=('ariel',16,'bold'),width=10,text="EXIT",bg="SteelBlue1",command=qexit)
btn_exit.grid(row=9,column=2,padx=10,pady=10)

btn_price= Button(f1,bd=5,fg='black',font=('ariel',16,'bold'),width=10,text="PRICE",bg="SteelBlue1",command=price)
btn_price.grid(row=9,column=3,padx=10,pady=10)

root.mainloop()
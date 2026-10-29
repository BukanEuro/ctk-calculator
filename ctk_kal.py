import customtkinter as ctk
from asteval import Interpreter

aeval = Interpreter()

app = ctk.CTk()
app.geometry("400x600")
app.title("CTK_KALKULATOR")

nomor = ""

def satu():
    global nomor
    nomor += "1"
    layar.configure(text=nomor)

def dua():
    global nomor
    nomor += "2"
    layar.configure(text=nomor)

def tiga():
    global nomor
    nomor += "3"
    layar.configure(text=nomor)

def empat():
    global nomor
    nomor += "4"
    layar.configure(text=nomor)

def lima():
    global nomor
    nomor += "5"
    layar.configure(text=nomor)

def enam():
    global nomor
    nomor += "6"
    layar.configure(text=nomor)

def tujuh():
    global nomor
    nomor += "7"
    layar.configure(text=nomor)

def delapan():
    global nomor
    nomor += "8"
    layar.configure(text=nomor)

def sembilan():
    global nomor
    nomor += "9"
    layar.configure(text=nomor)

def nolnol():
    global nomor
    nomor += "00"
    layar.configure(text=nomor)

def nol():
    global nomor
    nomor += "0"
    layar.configure(text=nomor)

def tambah():
    global nomor
    if nomor == "":
        print("masukan nomor dulu")
    elif nomor and nomor[-1] in {"+","-","=","*","/","%"}:
        print("ada fungsi lain !!!")
    else:
        nomor += "+"
        layar.configure(text=nomor)

def kurang():
    global nomor
    if nomor == "":
        print("masukan nomor dulu")
    elif nomor and nomor[-1] in {"+","-","=","*","/","%"}:
        print("ada fungsi lain !!!")
    else:
        nomor += "-"
        layar.configure(text=nomor)

def kali():
    global nomor
    if nomor == "":
        print("masukan nomor dulu")
    elif nomor and nomor[-1] in {"+","-","=","*","/","%"}:
        print("ada fungsi lain !!!")
    else:
        nomor += "*"
        layar.configure(text=nomor)

def bagi():
    global nomor
    if nomor == "":
        print("masukan nomor dulu")
    elif nomor and nomor[-1] in {"+","-","=","*","/","%"}:
        print("ada fungsi lain !!!")
    else:
        nomor += "/"
        layar.configure(text=nomor)

def titik():
    global nomor
    if nomor == "":
        print("masukan nomor dulu")
    elif nomor and nomor[-1] in {"+","-","=","*","/","%"}:
        print("ada fungsi lain !!!")
    else:
        nomor += "."
        layar.configure(text=nomor)

def persen():
    global nomor
    if nomor == "":
        print("masukan nomor dulu")
    elif nomor and nomor[-1] in {"+","-","=","*","/","%"}:
        print("ada fungsi lain !!!")
    else:
        nomor += "/100"
        layar.configure(text=nomor)

def ac():
    global nomor 
    nomor = ""
    layar.configure(text=nomor)

def hapus():
    global nomor
    if nomor[-4:] == "/100":
        nomor = nomor[:-4]
        layar.configure(text=nomor)
    else:
        nomor = nomor[:-1]
        layar.configure(text=nomor)

def sama_dengan():
    global nomor
    nomor = aeval(nomor)
    layar.configure(text=nomor)
    nomor = str(nomor)



layar = ctk.CTkLabel(app,text=nomor,font=("Arial",50))
layar.pack(expand=True,fill="both",padx=(50,50),pady=50)

frame1 = ctk.CTkFrame(app,fg_color="transparent")
frame1.pack(expand=True,fill="both",)

tombol_ac = ctk.CTkButton(frame1,text="AC",height=80,width=80,fg_color="#303030",command=ac)
tombol_ac.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_persen = ctk.CTkButton(frame1,text="%",height=80,width=80,fg_color="#303030",command=persen)
tombol_persen.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_hapus = ctk.CTkButton(frame1,text="<",height=80,width=80,fg_color="#303030",command=hapus)
tombol_hapus.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_bagi = ctk.CTkButton(frame1,text="/",height=80,width=80,fg_color="#303030",command=bagi)
tombol_bagi.pack(expand=True,fill="both",side="left",padx=10,pady=5)

frame2 = ctk.CTkFrame(app,fg_color="transparent")
frame2.pack(expand=True,fill="both",)

tombol_7 = ctk.CTkButton(frame2,text="7",height=80,width=80,fg_color="#404040",command=tujuh)
tombol_7.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_8 = ctk.CTkButton(frame2,text="8",height=80,width=80,fg_color="#404040",command=delapan)
tombol_8.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_9 = ctk.CTkButton(frame2,text="9",height=80,width=80,fg_color="#404040",command=sembilan)
tombol_9.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_kali = ctk.CTkButton(frame2,text="x",height=80,width=80,fg_color="#303030",command=kali)
tombol_kali.pack(expand=True,fill="both",side="left",padx=10,pady=5)

frame3 = ctk.CTkFrame(app,fg_color="transparent")
frame3.pack(expand=True,fill="both",)

tombol_4 = ctk.CTkButton(frame3,text="4",height=80,width=80,fg_color="#404040",command=empat)
tombol_4.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_5 = ctk.CTkButton(frame3,text="5",height=80,width=80,fg_color="#404040",command=lima)
tombol_5.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_6 = ctk.CTkButton(frame3,text="6",height=80,width=80,fg_color="#404040",command=enam)
tombol_6.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_kurang = ctk.CTkButton(frame3,text="-",height=80,width=80,fg_color="#303030",command=kurang)
tombol_kurang.pack(expand=True,fill="both",side="left",padx=10,pady=5)

frame4 = ctk.CTkFrame(app,fg_color="transparent")
frame4.pack(expand=True,fill="both",)

tombol_1 = ctk.CTkButton(frame4,text="1",height=80,width=80,fg_color="#404040",command=satu)
tombol_1.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_2 = ctk.CTkButton(frame4,text="2",height=80,width=80,fg_color="#404040",command=dua)
tombol_2.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_3 = ctk.CTkButton(frame4,text="3",height=80,width=80,fg_color="#404040",command=tiga)
tombol_3.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_tambah = ctk.CTkButton(frame4,text="+",height=80,width=80,fg_color="#303030",command=tambah)
tombol_tambah.pack(expand=True,fill="both",side="left",padx=10,pady=5)

frame5 = ctk.CTkFrame(app,fg_color="transparent")
frame5.pack(expand=True,fill="both",)

tombol_00 = ctk.CTkButton(frame5,text="00",height=80,width=80,fg_color="#404040",command=nolnol)
tombol_00.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_0 = ctk.CTkButton(frame5,text="0",height=80,width=80,fg_color="#404040",command=nol)
tombol_0.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_titik = ctk.CTkButton(frame5,text=".",height=80,width=80,fg_color="#404040",command=titik)
tombol_titik.pack(expand=True,fill="both",side="left",padx=10,pady=5)

tombol_samadengan = ctk.CTkButton(frame5,text="=",height=80,width=80,fg_color="#ff8c00",command=sama_dengan)
tombol_samadengan.pack(expand=True,fill="both",side="left",padx=10,pady=5)



app.mainloop()


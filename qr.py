import tkinter as tk 
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode 
#temel kodlar

def qr_kodu_oluştur():
    url=url_girdi.get()
    
    if url:
        qr_url=pyqrcode.create(url)
        dosya_yolu=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG dosyaları","*.svg")]) 

        if dosya_yolu:
            with open(dosya_yolu,"wb") as f:
                qr_url.svg(f, scale=8 )
            durum_etiketi.config(text="QR oluşturuldu ve kaydedildi")
    
#tasarım

uygulama_pencere=tk.Tk()
uygulama_pencere.title("QR kodu oluşturucu")

etiket=tk.Label(uygulama_pencere,text=("URL'yi giriniz:"))
url_girdi=tk.Entry(uygulama_pencere,width=40)
qrkodu_oluştur_butonu=tk.Button(uygulama_pencere,text="QR Kodu oluştur",command=qr_kodu_oluştur)
durum_etiketi=tk.Label(uygulama_pencere,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
qrkodu_oluştur_butonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

uygulama_pencere.mainloop()
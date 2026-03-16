import PyPDF2
from gtts import gTTS 
import os
import tkinter as tk 
from tkinter import filedialog

def pdf_metni_cikart(pdf_yolu):
    metin=""
    pdf_okuyucu=PyPDF2.PdfReader(open(pdf_yolu,"rb"))
    for page_no in range(len(pdf_okuyucu.pages)):
        metin+=pdf_okuyucu.pages[page_no].extract_text()
    return metin

#metni sesli hale getiren fonksiyon,

def metni_sese_cevir(metin,çikti_dosyasi):
    sesli_cevirici=gTTS(text=metin,lang="tr")
    sesli_cevirici.save(çikti_dosyasi)

#dosya seçme fonksiyonu

def dosya_seç():
    dosya_yolu=filedialog.askopenfilename(filetypes=[("PDF Dosyaları","*pdf")])
    if dosya_yolu:
        pdf_metin=pdf_metni_cikart(dosya_yolu)
        metni_sese_cevir(pdf_metin,"kaydet.mp3")
        os.system("start kaydet.mp3")

#tkinter ara yüzü
app=tk.Tk()
app.title("sesli kitap uygulaması")
app.geometry("250x150")

seçim_butonu=tk.Button(app,text="PDF seç",command=dosya_seç,padx=20,pady=20)
seçim_butonu.pack(pady=20)


app.mainloop()





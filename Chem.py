from customtkinter import *
from PIL import Image
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
import periodictable

def sonuc():
    element_adi = entry1.get().capitalize()  # Kullanıcının girdiği elementi al
    try:
        element = getattr(periodictable.elements, element_adi)  # Elementi getir
        bilgi = f"""
        Element: {element.name}
        Sembol: {element.symbol}
        Atom Numarası: {element.number}
        Atom Kütlesi: {element.mass} g/mol
        Yoğunluk: {element.density} g/cm³
        """
        messagebox.showinfo("Element Bilgisi", bilgi)  # Mesaj kutusunda göster
    except AttributeError:
        messagebox.showerror("Hata", "Geçerli bir element adı giriniz!")  # Hata mesajı
window = CTk()
window.title("Element Analizi")
window.geometry("400x400")
window.resizable(0,0)
canvas = CTkCanvas(master=window, width=400, height=401)
canvas.grid(row=0, column=0)
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/Adsız tasarım.png")
canvas.create_image(0, 0, image=background_image, anchor="nw")
entry1= CTkEntry(master=window, 
                 placeholder_text="Element Sembolü yazınız", placeholder_text_color="grey",
                 width=200, height=30, corner_radius=15
                 ,fg_color="lightgrey",bg_color="#404040",border_width=4,
                 border_color="black",text_color="black")
entry1.place(rely=0.450, relx=0.515, anchor="center")
btn=CTkButton(master=window,text="göster", fg_color="#404040",
bg_color="#404040", corner_radius=15, border_color="black",
border_width=3,
hover_color="grey",
font=("bold",13,"bold"),command=sonuc)
btn.place(rely=0.6, relx=0.5, anchor="center")
window.mainloop()
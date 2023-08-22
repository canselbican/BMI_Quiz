import tkinter

window= tkinter.Tk()
window.title("Vücut kitle indeksi hesaplama")

def body_mass_index():
   boy=boy_giris.get()
   kilo=kilo_giris.get()

   if boy == "" or kilo == "":
      sonuç_label.config(text="kilonuzu ve boyunuzu girin")
   else:
      try:
       bmi =int(kilo) / ((int(boy) /100) ** 2)
       sonuç_string=write_sonuç(bmi)
       sonuç_label.config(text=sonuç_string)
      except:
       sonuç_label.config(text="değer girin")



kilo_label =tkinter.Label(text="kilonuzu girin:")
kilo_label.pack()
kilo_giris=tkinter.Entry(width=15)
kilo_giris.pack()

boy_label=tkinter.Label(text="boyunuzu girin:")
boy_label.pack()
boy_giris=tkinter.Entry(width=15)
boy_giris.pack()

hesaplama_button=tkinter.Button(text="Hesaplama",command=body_mass_index)
hesaplama_button.pack()

sonuç_label=tkinter.Label()
sonuç_label.pack()

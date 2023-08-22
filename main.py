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

def write_sonuç(bmi):
   sonuç_string = f"vücut kitle indeksiniz {round(bmi, 2)}. "
   if bmi <= 16:
      sonuç_string += "son derece zayıfsınız!"
   elif 16 < bmi <= 17:
      sonuç_string += "orta derecede zayıfsınız!"
   elif 17 < bmi <= 18.5:
      sonuç_string += "hafif zayıfsınız!"
   elif 18.5 < bmi <= 25:
      sonuç_string += "normal kilodasınız"
   elif 25 < bmi <= 30:
      sonuç_string += "kilolusunuz"
   elif 30 < bmi <= 35:
      sonuç_string += "1.derece obezsiniz"
   elif 35 < bmi <= 40:
      sonuç_string += "2.derece obezsiniz"
   else:
      sonuç_string += "3.derece obezsiniz"
   return sonuç_string


window.mainloop()

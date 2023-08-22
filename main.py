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
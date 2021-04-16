from tkinter import *
root = Tk()

# Menanmpilkan text
theLabel = Label(root, text = "Belajar GUI Python")
theLabel.pack()

# Membuat tombol
tombol = Frame(root)
tombol.pack()
tombolFrame = Frame(root)
tombolFrame.pack()
tombol.pack(side = TOP)

Button1 = Button(tombol, text = "Ini adalah tombol 1", fg = "red")
Button1.pack()

root.mainloop()
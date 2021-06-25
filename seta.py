import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("1000x1000")
root.title("瀬田")

seta = ImageTk.PhotoImage(file=r"C:\OneDriveNext\OneDrive - Nagasaki University\takapath\pic\seta2.jpg")
can = tk.Canvas(bg = "black", width = 367, height = 550)
can.place(x=0, y=0)
can.create_image(0,0, image=seta, anchor=tk.NW)

root.mainloop()
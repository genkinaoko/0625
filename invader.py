import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")

image2 = tk.PhotoImage(file = r"C:\OneDriveNext\OneDrive - Nagasaki University\takapath\pic\bassho-2.jpg")
push_button = tk.Button(root, text = "Push", image = image2, compound = tk.LEFT, width = 100, height = 30)
push_button.place(x=30, y=30)

root.mainloop()
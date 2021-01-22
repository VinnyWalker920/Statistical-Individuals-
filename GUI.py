import tkinter as tk
from subject import GeneticCode

gene = GeneticCode()

window = tk.Tk()
frame = tk.Frame(window)

frame.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], minsize=50)
frame.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], minsize=50)



for x,i in enumerate(gene):
    for y,j in enumerate(i):
        label = tk.Label(master=frame,text=str(j), borderwidth=5, relief="raised")
        label.config(font=("Courier", 20))
        label.grid(row=y, column=x, sticky="e")


frame.pack(side=tk.RIGHT)

window.mainloop()

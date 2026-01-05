import tkinter as tk

def button_clicked():
    print("Button clicked")
    #my_label.config(text="Button clicked")
    my_label.config(text=input.get())

#Creating a new window and configurations
window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
my_label.grid(column=0, row=0)

#Button
button = tk.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#Entry
input = tk.Entry(width=10)
#input.pack()
input.grid(column=3, row=2)
# print(input.get())

window.mainloop()



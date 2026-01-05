import tkinter as tk

#Creating a new window and configurations
window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Functions 
def miles_to_km ():
    #print("Button clicked")
    #my_label.config(text="Button clicked")
    km = float(input.get()) * 1.60934
    my_label4.config(text=f"{km}")

#Label
my_label1 = tk.Label(text="Miles", font=("Arial", 24, "bold"))
#my_label.pack()
my_label1.grid(column=2, row=0)

my_label2 = tk.Label(text="is equal to", font=("Arial", 24, "bold"))
#my_label.pack()
my_label2.grid(column=0, row=1)

my_label3 = tk.Label(text="Km", font=("Arial", 24, "bold"))
#my_label.pack()
my_label3.grid(column=2, row=1)

my_label4 = tk.Label(text=" ", font=("Arial", 24, "bold"))
#my_label.pack()
my_label4.grid(column=1, row=1)

#Button
button = tk.Button(text="Calculate", command=miles_to_km)
#button.pack()
button.grid(column=1, row=2)

#Entry
input = tk.Entry(width=7)
#input.pack()
input.grid(column=1, row=0)
#print(input.get())

window.mainloop()

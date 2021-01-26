import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Assembly Line PT XYZ Version 0.1')
window.geometry('900x800')

# TEXTBOX
text_box_main = tk.Text(window,height="10",width="30")
text_box_main.grid(column=4, row=6, rowspan=3)

text_box_op1= tk.Text(window,height="3", width="14")
text_box_op1.grid(column=1, row=7,padx=15)

text_box_op2 = tk.Text(window,height="3", width="14")
text_box_op2.grid(column=2, row=7)

text_box_op3 = tk.Text(window,height="3", width="14")
text_box_op3.grid(column=3, row=7,sticky='w',padx=10)

text_box_ws1 = tk.Text(window,height="5", width="14")
text_box_ws1.grid(column=1, row=21)

text_box_ws2 = tk.Text(window,height="5", width="14")
text_box_ws2.grid(column=2, row=21)

text_box_ws3 = tk.Text(window,height="5", width="14")
text_box_ws3.grid(column=3, row=21,pady=10,sticky='w',padx=15)

text_box_stock1 = tk.Text(window,height="2", width="14")
text_box_stock1.grid(column=1, row=12,sticky='w',padx=15)

text_box_stock2 = tk.Text(window,height="2", width="14")
text_box_stock2.grid(column=1, row=17,pady=10,sticky='w',padx=15)

text_box_stock3 = tk.Text(window,height="2", width="14")
text_box_stock3.grid(column=2, row=17,pady=10,sticky='w',padx=15)

text_box_stock4 = tk.Text(window,height="2", width="14")
text_box_stock4.grid(column=3, row=17,pady=10,sticky='w',padx=15)




# LABEL

ttk.Label(text = 'Operator List', font =('arial', 11)).grid(column=2,row=5)
ttk.Label(text = 'Work Station List', font =('arial', 11)).grid(column=2,row=18,pady=10,ipady=10)
ttk.Label(text = 'Information', font =('arial', 11)).grid(column=4,row=5,pady=20)
ttk.Label(text = 'Process Simulation', font =('arial', 11)).grid(column=2,row=8)


# INFO WORK STATION
def work_station1_info():
    text_box_ws1.delete("1.0", tk.END)
    text_box_ws1.insert(tk.INSERT, info_ws1)

def  work_station2_info():
    text_box_ws2.delete("1.0", tk.END)
    text_box_ws2.insert(tk.INSERT, info_ws2)
    return

def  work_station3_info():
    text_box_ws3.delete("1.0", tk.END)
    text_box_ws3.insert(tk.INSERT, info_ws3)
    return

# INFO OPERATOR
def operator1_info():
    text_box_op1.delete("1.0",tk.END)
    text_box_op1.insert(tk.INSERT, info_operator1)
    return

def operator2_info():
    text_box_op2.delete("1.0",tk.END)
    text_box_op2.insert(tk.INSERT, info_operator2)
    return

def operator3_info():
    text_box_op3.delete("1.0",tk.END)
    text_box_op3.insert(tk.INSERT, info_operator3)
    return

# INFO PRODUCT
def product1_info():
    text_box_main.delete("1.0",tk.END)
    text_box_main.insert(tk.INSERT,info_product1)
    return

def product2_info():
    text_box_main.delete("1.0",tk.END)
    text_box_main.insert(tk.INSERT,info_product2)
    return

def product3_info():
    text_box_main.delete("1.0",tk.END)
    text_box_main.insert(tk.INSERT,info_product3)
    return

# DICTIONARY
product_color ={
    -1: "gray",
    0: "gray",
    1: "blue",
    2: "red",
    3: "yellow",
    4: "gray",
    5: "gray",
    6: "gray",
    7: "gray",
    8: "gray",
}

global counter
counter = 0


# BUTTON START
def start_button():
    global counter
    counter += 1
    if counter <= 8:
        product1.configure(bg=product_color[0+counter])
        product2.configure(bg=product_color[-1+counter])
        product3.configure(bg=product_color[-2+counter])
    elif counter > 8:
        counter = -1


def reset_button():
    product1.configure(bg='gray')
    product2.configure(bg='gray')
    product3.configure(bg='gray')
    product3.configure(bg='gray')
    text_box_main.delete("1.0", tk.END)
    system_reset = 'The system has been reset'
    text_box_main.insert(tk.INSERT, system_reset)
    return ()


# GAMBAR
img_px = tk.PhotoImage(file="img_px.png")
operator = tk.PhotoImage(file="operator.png")
tools = tk.PhotoImage(file="tools.png")

# CONVEYOR
conveyor = tk.Button(window, image = img_px)
conveyor.grid(column=1, row=15, columnspan=3,sticky='we',padx=20)
conveyor.config(height=10, width=400, bg="gray", state = "disable")

# START BUTTON
start_button = tk.Button(window,image=img_px, text="START", compound = "center",
                     command=start_button)
start_button.grid(column=4, row=12,columnspan=2,sticky='w')

# RESET BUTTON
reset_button = tk.Button(window,image=img_px, text="RESET", compound = "center",
                     command=reset_button)
reset_button.grid(column=4, row=12,columnspan=2,sticky='e')


# WORKSTATION
work_station1 = tk.Button(image =tools, compound = 'center', command = lambda : work_station1_info())
work_station1.grid(column=1, row=19)
work_station1.config(height=42, width=42)

work_station2 = tk.Button(image =tools , compound = 'center', command = lambda : work_station2_info())
work_station2.grid(column=2, row=19)
work_station2.config(height=42, width=42)

work_station3=tk.Button(image =tools, compound = 'center', command = lambda : work_station3_info())
work_station3.grid(column=3, row=19,sticky='w',padx=50)
work_station3.config(height=42, width=42)

# OPERATOR
operator1=tk.Button(image = operator, compound = 'center', command = lambda : operator1_info())
operator1.grid(column=1, row=6)
operator1.config(height=42, width=42)

operator2 = tk.Button(image = operator, compound = 'center', command = lambda : operator2_info())
operator2.grid(column=2, row=6)
operator2.config(height=42, width=42)

operator3=tk.Button(image = operator, compound = 'center', command = lambda : operator3_info())
operator3.grid(column=3, row=6,sticky='w',padx=50)
operator3.config(height=42, width=42)


# PRODUCT
frame_product1 = tk.Frame(window, height="20", width="20")
product1 = tk.Button(frame_product1, image = img_px, command = lambda : product1_info())
frame_product1.grid(column=1, row=13,pady=20)
product1.grid(column=1, row=2)
product1.config(height=20, width=20, bg="gray")


frame_product2 = tk.Frame(window, height="50", width="50")
product2 = tk.Button(frame_product2, image = img_px, command = lambda : product2_info())
frame_product2.grid(column=2, row=13)
product2.grid(column=1, row=2)
product2.config(height=20, width=20, bg="gray")

frame_product3 = tk.Frame(window, height="50", width="50")
product3 = tk.Button(frame_product3, image = img_px, command = lambda : product3_info())
frame_product3.grid(column=3, row=13,sticky='w',padx=60)
product3.grid(column=2, row=2)
product3.config(height=20, width=20, bg="gray")


# DATABASE
info_ws1 = """Work Station 1

Engine 
Mounting
"""

info_ws2 = """Work Station 2

Door
Assembly
"""

info_ws3 = """Work Station 3

Windshield 
Assembly
"""

# INFO OPERATOR
info_operator1 = """Operator 1
ID A1234
Grade : AAA     
"""

info_operator2 = """Operator 2
ID A4567
Grade AA    
"""

info_operator3 = """Operator 3
ID A7890
Grade A   
"""

# INFO PRODUCT
info_product1 = """
Chassis with engine installed
"""

info_product2="""
Chassis with engine and door installed
"""

info_product3="""
Chassis with engine, door, and windshield installed
"""

window.mainloop()
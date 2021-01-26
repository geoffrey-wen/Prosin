#IMPORT
import tkinter as tk
from tkinter import *

# DATABASE
from Workstation import Workstation
from Product import Product
from Material import Material
from Display import displaytime

#WINDOW STANDARD
window=tk.Tk()
window.title('Assembly Line Simulation 0.1')
window.geometry('700x500')
window.resizable(0, 0)

#WINDOW CONFIG

kumpulan_entry=[]
input_data=["Name of Production Line", "Process at Assembly 1", "Process at Assembly 2", "Process at Assembly 3"]

def buat_window():
    window_New = tk.Toplevel(window)
    window_New.title("New Configuration Huyu")

    for isi_input_data in input_data:
        a = StringVar()
        frame_New1=tk.Frame(window_New)
        label_New1=tk.Label(frame_New1,text=isi_input_data,width=30,anchor="w")
        entry_New1=tk.Entry(frame_New1,width=50, textvariable=a)
        frame_New1.pack(side=TOP,expand=YES,fill=BOTH)
        label_New1.pack(side=LEFT,expand=YES,fill=BOTH)
        entry_New1.pack(side=RIGHT,expand=YES,fill=BOTH)
        kumpulan_entry.append(entry_New1)
        print(kumpulan_entry)
    frame_New2=tk.Frame(window_New)
    button_New=tk.Button(frame_New2,text="Done",anchor="center",
                         command=lambda:[command_menu_pabrik_baru(),window_New.destroy()]).pack(side=BOTTOM)
    frame_New2.pack(side=BOTTOM,expand=YES,fill=BOTH)


#GAMBAR
img_px = tk.PhotoImage(file="img_px.png")


#MENU BAR
menubar=Menu(window)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New Configuration Hayuuu", command=buat_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Menuyuyuyu", menu=filemenu)

window.config(menu=menubar)

workstation_name_list=[]
workstation_buffer_list=[]
workstation_list = []

#MENU CONFIG FULL
def command_menu_pabrik_baru():

    for isi_kumpulan_entry in kumpulan_entry:
        window.title(kumpulan_entry[0].get())

    workstation_name_satu = str(kumpulan_entry[1].get())
    workstation_name_dua = str(kumpulan_entry[2].get())
    workstation_name_tiga = str(kumpulan_entry[3].get())
    workstation_name_list = [workstation_name_satu, workstation_name_dua, workstation_name_tiga]

    #WORKSTATION LIST
    global workstation_list
    temp = Workstation("endinventory", None)
    workstation_list.append(temp)
    for i in range(len(workstation_name_list) - 1, -1, -1):
        temp = Workstation(workstation_name_list[i], temp)
        workstation_list.insert(0, temp)


    # MAKING WORKSTAION'S INVENTORY
    global workstation_buffer_life
    for i in range(len(workstation_name_list)):
        buffername = f"Buffer-{workstation_name_list[i]}"
        temp = Workstation(buffername, workstation_list[i])
        workstation_buffer_list.append(temp)

#INTERFACE
# TEXTBOX
information_box = tk.Text(window,height="10",width="30")
information_box.grid(column=9, row=9, rowspan=3)


# LABEL

tk.Label(text = 'Operator List', font =('times new roman', 11)).grid(column=2,row=5)
tk.Label(text = 'Inventory List', font =('times new roman', 11)).grid(column=2,row=12,pady=10,ipady=10)
tk.Label(text = 'Information', font =('times new roman', 11)).grid(column=9,row=8,pady=20)
tk.Label(text = 'Process Simulation', font =('times new roman', 11)).grid(column=2,row=9)
tk.Label(text = 'Cargo Ready', font =('times new roman', 11)).grid(column=5,row=9)


# DICTIONARY
product_color ={
    -1: "gray",
    0: "gray",
    1: "blue",
    2: "red",
    3: "yellow",
    4: "blue",
    5: "red",
    6: "yellow",

}

#COUNTER
counter = 0
global time
time = 0


# BUTTON START
global product
product = [[], [], []]
def start_pencet():
    global counter
    counter += 1
    if counter <= 6:
        product[0].configure(bg=product_color[0+counter])
        product[1].configure(bg=product_color[-1+counter])
        product[2].configure(bg=product_color[-2+counter])
    elif counter > 6:
        counter = 2
    return(counter)


clicks = 0

def addClick():
  global clicks #this will use the variable to count
  clicks = clicks + 1
  if clicks < 0:
      lbl.configure(text=0)
  if clicks > 3:
      lbl.configure(text=clicks - 3 )

def reset_button():
    product[0].configure(bg='gray')
    product[1].configure(bg='gray')
    product[2].configure(bg='gray')
    system_reset = 'The system has been reset'
    global counter
    counter = 0
    global clicks
    clicks = 0
    lbl.configure(text=clicks)
    return ()

# GAMBAR
img_px = tk.PhotoImage(file="img_px.png")
operator = tk.PhotoImage(file="operator.png")
tools = tk.PhotoImage(file="inventory.png")
picproduct =  tk.PhotoImage(file="product.png")

# CONVEYOR
conveyor = tk.Button(window, image = img_px)
conveyor.grid(column=1, row=10, columnspan=3 ,padx=0)
conveyor.config(height=10, width=150, bg="green", state = "disable")

# START BUTTON
start_click = tk.Button(window,image=img_px, text="START CYCLE", compound = "center",
                     command=lambda:[start_pencet(), addClick()])
start_click.grid(column=9, row=12,columnspan=2,sticky='w')

# RESET BUTTON
reset_button = tk.Button(window,image=img_px, text="RESET", compound = "center",
                     command=reset_button)
reset_button.grid(column=9, row=12,columnspan=2,sticky='e')

# INFO WORK STATION
def inventory_info(i):
    information_box.delete(1.0, tk.END)
    information_box.insert(tk.INSERT, workstation_buffer_list[i].id)

# INFO OPERATOR
def operator_info(i):
    information_box.delete(1.0,tk.END)
    information_box.insert(tk.INSERT, info_operator[i])
    return

# INFO PRODUCT
def product_info(i):
    information_box.delete(1.0,tk.END)
    information_box.insert(tk.INSERT,info_product[i])
    return

# INVENTORY
for i in range(3):
    inventory1 = tk.Button(image=tools, compound='center', command=lambda i=i : inventory_info(i))
    inventory1.grid(column=i+1, row=19)
    inventory1.config(height=42, width=42)

# OPERATOR
for i in range(3):
    operator1=tk.Button(image = operator, compound = 'center', command = lambda i=i: operator_info(i))
    operator1.grid(column=1+i, row=6)
    operator1.config(height=42, width=42)

# PRODUCT
for i in range(3):
    frame_product1 = tk.Frame(window, height="20", width="20")
    product[i] = tk.Button(frame_product1, image=img_px, command=lambda i=i: product_info(i))
    frame_product1.grid(column=i+1, row=10, pady=20)
    product[i].grid(column=1, row=2)
    product[i].config(height=20, width=20, bg="gray")

#CARGO READY
lbl= tk.Label(image = img_px, compound = 'center', text = clicks)
lbl.grid(column=5, row=10)
lbl.config(height=42, width=42)

#SPACER
frame_kosong=tk.Frame(window, width="50")
frame_kosong.grid(column=4, row=0)
frame_kosong=tk.Frame(window, width="50")
frame_kosong.grid(column=8, row=0)

# DATABASE
info_ws1 = """Config your process in the menu
"""

info_ws2 = """Config your process in the menu
"""

info_ws3 = """Config your process in the menu
"""

# INFO OPERATOR
info_operator = []
for i in range(3):
    info_operator.append(f"""Operator {i+1}
    ID A{i}{i}{i}
    Grade A""")

# INFO PRODUCT
info_product = [[], [], []]
if product[0].configure(bg="grey"):
    info_product[0] = """There is no process yet"""
else:
    info_product[0] = """Engine is being installed"""
if product[1].configure(bg="gray"):
    info_product[1] = """There is no process yet"""
else:
    info_product[1] = """Cabin is being installed"""
if product[2].configure(bg="gray"):
    info_product[2] = """There is no process yet"""
else:
    info_product[2] = """Door is being installed"""

#-----------------------------------------------------------------------------------------------------------------------
window.mainloop()


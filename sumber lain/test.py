from Workstation import Workstation
from Product import Product
from Material import Material
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from Display import displaytime


#_______________________________________________________________________________________________________________________
# CONFIG + DISPLAY
def pre_config_menu():
    pre_config = Toplevel(main_window)
    pre_config.title("Config Line")
    frame1 = Frame(pre_config)
    label1 = Label(frame1, text = "Number of worksation").pack(side = LEFT, padx = 10, pady = 5)
    entry1 = Entry(frame1)
    entry1.pack(side=RIGHT, padx = 10, pady = 5)
    frame1.pack(fill = X)
    frame2 = Frame(pre_config)
    label2 = Label(frame2, text = "Long of timespan").pack(side = LEFT, padx = 10, pady = 5)
    entry2 = Entry(frame2)
    entry2.pack(side=RIGHT, padx = 10, pady = 5)
    frame2.pack(fill = X)
    button = Button(pre_config, text = "OK", command=lambda:[config_menu(entry1, entry2), pre_config.destroy()])
    button.pack(pady = 10)

def config_menu(num, timesp):
    # DEFINING WORKSTATION NUMBER
    global number_of_workstation
    number_of_workstation = int(num.get())

    # DEFINING PRODUCT
    global product_list
    product_list = []

    # DEFINING TIME VECTOR
    global timespan
    timespan = int(timesp.get())
    global time
    time = 0

    # START WINDOW
    start_window = Tk()
    start_window.title('Config Line')
    #main_window.resizable(0, 0)

    label1 = Label(start_window, text = "Workstation Name").grid(column = 1, row = 0)
    label2 = Label(start_window, text = "Resource Type").grid(column = 2, row = 0)
    label2 = Label(start_window, text = "Resource Formula").grid(column = 3, row = 0)

    global workstation_list
    workstation_list = []
    global workstation_buffer_list
    workstation_buffer_list = []

    global material_type_list
    material_type_list = []
    global material_list
    material_list = []
    global resource_formula
    resource_formula = []

    list1 = []
    list2 = []
    list3 = []

    for i in range(number_of_workstation):
        label = Label(start_window, text = f" Workstation {i+1} ").grid(column = 0, row = i+1)
        entry1 = Entry(start_window)
        entry1.grid(column = 1, row = i+1)
        entry2 = Entry(start_window)
        entry2.grid(column = 2, row = i+1)
        entry3 = Entry(start_window)
        entry3.grid(column = 3, row = i+1)
        list1.append(entry1)
        list2.append(entry2)
        list3.append(entry3)
    button = Button(start_window, text = "OK", command = lambda : [basic_info(list1, list2, list3), start_window.destroy()])
    button.grid(column = 0, row = 0)

def basic_info(list1, list2, list3):
    # MAKING WORKSTATION
    workstation_name_list = []
    for i in range(number_of_workstation):
         workstation_name_list.append(list1[i].get())

    temp = Workstation("endinventory", None)
    workstation_list.append(temp)
    for i in range(number_of_workstation - 1, -1, -1):
        temp = Workstation(workstation_name_list[i], temp)
        workstation_list.insert(0, temp)

    # MAKING WORKSTATION'S BUFFERS
    for i in range(number_of_workstation):
        buffername = f"Buffer-{workstation_name_list[i]}"
        temp = Workstation(buffername, workstation_list[i])
        workstation_buffer_list.append(temp)

    # SUPPLYING MATERIAL TO THE BUFFERS
    for i in range(number_of_workstation):
        material_type_list.append(list2[i].get())
        material_list.append([])

    # DETERMINE RESOURCES NEEDED BY EACH WORKSTATION
    for i in range(number_of_workstation):
        temp = int(list3[i].get())
        resource_formula.append(temp)

    clear_display_top(20)
    clear_display_bottom(20, 20)
    display_basic_info()

def clear_display_top(numcol):
    for i in range(numcol):
        for j in range(9):
            label = Label(main_window, text = " ").grid(column = i, row = j, sticky = W+E+N+S)

def clear_display_bottom(numcol, numrow):
    for i in range(numcol):
        for j in range(numrow):
            label = Label(main_window, text = " ").grid(column = i, row = j+9, sticky = W+E+N+S)

def display_basic_info():
    for i in range(len(workstation_list)):
        label = Label(main_window, text=workstation_list[i].id).grid(column=i * 2, row=5)
        button = Button(main_window, text=" ").grid(column=i * 2, row=6, sticky = W+E)
        if i + 1 != len(workstation_list):
            image1 = tk.Label(main_window, image=arrowright, compound='center')
            image1.grid(column=i * 2 + 1, row=6)
            image1.config(height=30, width=30)
            image2 = tk.Label(main_window, image=arrowup, compound='center')
            image2.grid(column=i * 2, row=7)
        else:
            image2 = tk.Label(main_window, image=arrowdown, compound='center')
            image2.grid(column=i * 2, row=7)
        image2.config(height=30, width=30)

    for i in range(len(material_list)):
        print_type = Label(main_window, text=f"{material_type_list[i]}:").grid(column=i * 2, row=8)
        num = 0
        print_type = Label(main_window, text=f"            ").grid(column=i * 2 + 1, row=8)
        if i + 1 == len(material_list):
            print_type = Label(main_window, text=f"finished_goods:").grid(column=i * 2 + 2, row=8)

    global quick_add
    add_mat.delete(2)
    quick_add = Menu(add_mat, tearoff=0)
    for i in range(number_of_workstation):
        quick_add.add_command(label=f"Add a/an {material_type_list[i]}", command=lambda i=i : define_material_id(1, i))
    add_mat.add_cascade(label = "Quick addition", menu = quick_add)

    global history_ws
    history.delete(1)
    history_ws = Menu(history, tearoff=0)
    for i in range(len(workstation_list)):
        history_ws.add_command(label=f"{workstation_list[i].id}", command=lambda i=i: history_workstation(i))
    history.add_cascade(label="Workstation", menu=history_ws)

    timedisplay1 = Label(main_window, text = f"Time : {displaytime(time, timespan)[:5]}").grid(column=0, row=0, sticky = W)

    run_button = Button(main_window, text = "Run", command = lambda : [timeflow()]).grid(column = 0, row = 1)


def display_material():
    clear_display_bottom(len(workstation_list)*2+2, 15)

    for i in range(len(material_list)):
        print_type = Label(main_window, text=f"{material_type_list[i]} :").grid(column = i*2, row = 8)
        num = 0
        for j in range(len(workstation_buffer_list[i].products)):
            num += 1
            print_item = Label(main_window, text=f"{num}. {workstation_buffer_list[i].products[j].id}").grid(column = i*2, row = j + 9)

    num = 0
    for i in range(len(workstation_list[-1].products)):
        num += 1
        temp = ""
        for j in range(len(workstation_list[-1].products[i].component)):
            for k in range(len(workstation_list[-1].products[i].component[j])):
                temp += f"{workstation_list[-1].products[i].component[j][k].id}, "
        print_item = Label(main_window, text=f"{num}. {workstation_list[-1].products[i].id} → {temp[:-2]}")
        print_item.grid(column=2 * len(workstation_list)-2, row=i + 9, columnspan = 3, sticky = W+E)


def display_status():
    for i in range(len(workstation_list)*2+2):
        label = Label(main_window, text = " ").grid(column = i, row = 4, sticky = W+E+N+S)

    for i in range(len(workstation_list)-1):
        if len(workstation_list[i].products) == 0:
            label = Label(main_window, text = " ").grid(column = i*2-1, row = 4)
        else:
            label = Label(main_window, text = f"{len(workstation_list[i].products[0].component[i])}/{resource_formula[i]}").grid(column = i*2, row = 4)


def timeflow():
    global time
    time += 1
    print(time)
    # MOVING PRODUCT
    if len(product_list) > 0:
        for i in range(len(product_list)):
            index = -1
            for j in range(len(workstation_list) - 1):
                if str(product_list[i].location.id) == str(workstation_list[j].id):
                    index = j
            if index >= 0:
                product_list[i].move(index, resource_formula[index])
            else:
                product_list[i].history[2].append("Done")
    # MAKING NEW PRODUCT
    if len(workstation_list[0].products) == 0:
        productid = "#" + "0" * (3 - len(str(len(product_list)))) + str(len(product_list) + 1)
        temp = Product(productid, workstation_list[0])
        temp.history[0].append(temp.location.id)
        for i in range(len(workstation_buffer_list)):
            dummy = []
            temp.component.append(dummy)
        temp.history[1].append([])
        temp.history[2].append("Created")
        product_list.append(temp)
        workstation_list[0].products.append(temp)
    # PROCESSING MATERIALS
    for i in range(len(workstation_list)-1):
        label = Label(main_window, text = " ").grid(column=(len(workstation_list)+1)*2, row=i + 1, sticky = W+E+N+S)
    for i in range(len(workstation_buffer_list)):
        show = ""
        for j in range(resource_formula[i]):
            if len(workstation_list[i].products) > 0:
                if (len(workstation_buffer_list[i].products) == 0):
                    label = Label(main_window, text=f"There is no {material_type_list[i]} for Station {workstation_list[i].id}").grid(column=(len(workstation_list)+1)*2, row=i + 1, sticky = W)
                    workstation_list[i].fromworkstationtoproduct(product_list, 1)
                else:
                    for k in range(len(material_list[i])):
                        if material_list[i][k].id == workstation_buffer_list[i].products[0].id:
                            index = k
                    loc = workstation_buffer_list[i].products[0].process(i, resource_formula[i])
                    material_list[i][index].location = loc
                    workstation_list[i].fromworkstationtoproduct(product_list, 0)
    # WRITING WORKSTATION'S HISTORY
    for i in range(len(workstation_list)):
        workstation_list[i].writeworkstationhistory()
    # WRITING WORKSTATION'S BUFFER'S HISTORY
    for i in range(len(workstation_buffer_list)):
        workstation_buffer_list[i].writeworkstationhistory()
    # WRITING PRODUCT'S HISTORY
    for i in range(len(product_list)):
        product_list[i].writeproducthistory()

    for i in range(len(workstation_list)-1):
        if len(workstation_list[i].products) > 0:
            button = Button(main_window, text=f"{workstation_list[i].products[-1].id}").grid(column=i * 2, row=6, sticky = W + E)
        else:
            button = Button(main_window, text=f" ").grid(column=i * 2, row=6, sticky=W + E)

    button = Button(main_window, text=f"Sum = {len(workstation_list[-1].products)}").grid(column=2*len(workstation_list)-2, row=6, sticky=W + E)

    timedisplay1 = Label(main_window, text = f"Time : {displaytime(time, timespan)[:5]}").grid(column=0, row=0, sticky = W)

    display_material()

    display_status()

#_______________________________________________________________________________________________________________________
# MATERIAL ADDITION
def find_material_type_index(item):
    index = -1
    for i in range(len(material_type_list)):
        if str(item) == str(material_type_list[i]):
            index = i
    return index


def more_addition():
    more_add = Toplevel(main_window)
    more_add.title("More Addition")
    frame1 = Frame(more_add)
    label1 = Label(frame1, text = "Material to be added").pack(side = LEFT, padx = 10, pady = 5)
    combobox = Combobox(frame1, values = material_type_list)
    combobox.pack(side = RIGHT, padx = 10, pady = 5)
    frame1.pack(fill = X)
    frame2 = Frame(more_add)
    label2 = Label(frame2, text = "Number of material").pack(side = LEFT, padx = 10, pady = 5)
    entry = Entry(frame2)
    entry.pack(side=RIGHT, padx = 10, pady = 5)
    frame2.pack(fill = X)
    button = Button(more_add, text = "OK", command=lambda:[define_material_id(entry.get(), find_material_type_index(combobox.get())), more_add.destroy()])
    button.pack(pady = 10)


def smart_addition():
    smart_add = Toplevel(main_window)
    smart_add.title("Smart Addition")
    frame = Frame(smart_add)
    label = Label(frame, text = "Number of product").pack(side = LEFT, padx = 10, pady = 5)
    entry = Entry(frame)
    entry.pack(side=RIGHT, padx = 10, pady = 5)
    frame.pack(fill = X)
    button = Button(smart_add, text = "OK", command=lambda:[smart_addition2(entry.get()), smart_add.destroy()])
    button.pack(pady = 10)


def smart_addition2(num):
    for i in range(len(resource_formula)):
        temp = int(num) * resource_formula[i]
        define_material_id(temp, i)


def define_material_id(num, index):
    def_mat_id = Toplevel(main_window)
    def_mat_id.title("Define Material ID")
    list = []
    for i in range(int(num)):
        frame = Frame(def_mat_id)
        label = Label(frame, text = f"{material_type_list[index]} ID #{len(material_list[index])+1+i}").pack(side = LEFT, padx = 10, pady = 5)
        entry = Entry(frame)
        entry.pack(side = RIGHT, padx = 10, pady = 5)
        frame.pack()
        list.append(entry)
    button = Button(def_mat_id, text = "OK", command=lambda:[fill_material_list(index, list), def_mat_id.destroy()])
    button.pack(pady = 10)


def fill_material_list(index, list):
    for i in range(len(list)):
        material_list[index].append(Material(list[i].get(), workstation_buffer_list[index], material_type_list[index]))
        workstation_buffer_list[index].products.append(Material(list[i].get(), workstation_buffer_list[index], material_type_list[index]))

    display_material()


#_______________________________________________________________________________________________________________________
# DISPLAY HISTORY
def history_workstation(index):
    hist_ws = Toplevel(main_window)
    hist_ws.title(f"History {workstation_list[index].id} @ {displaytime(time, timespan)[9:]}")
    labela = Label(hist_ws, text = "Time").grid(column = 0, row = 0)
    labelb = Label(hist_ws, text = "Product").grid(column = 1, row = 0)
    for i in range(len(workstation_list[index].history)):
        label1 = Label(hist_ws, text = displaytime(i, timespan)).grid(column = 0, row = i+1)
        if len(workstation_list[index].history[i]) > 1:
            show = f"{workstation_list[index].history[i][0]}"
            for j in range(1, len(workstation_list[index].history[i])):
                show += f", {workstation_list[index].history[i][j]}"
        elif len(workstation_list[index].history[i]) == 1:
            show = f"{workstation_list[index].history[i][0]}"
        else:
            show = "None"
        label2 = Label(hist_ws, text = show).grid(column = 1, row = i+1)

def history_product():
    hist_prod = Toplevel(main_window)
    hist_prod.title(f"Product History")
    frame1 = Frame(hist_prod)
    label1 = Label(frame1, text = "Product").pack(side = LEFT, padx = 10, pady = 5)
    product_id_list = []
    for i in range(len(product_list)):
        product_id_list.append(product_list[i].id)
    combobox = Combobox(frame1, values = product_id_list)
    combobox.pack(side = RIGHT, padx = 10, pady = 5)
    frame1.pack(fill = X)
    button = Button(hist_prod, text = "OK", command=lambda:[history_product_display(find_product_index((combobox.get()))), hist_prod.destroy()])
    button.pack(pady = 10)

def history_product_display(index):
    locktarget = int(index)
    hist_prod_disp = Toplevel(main_window)
    hist_prod_disp.title(f"History {product_list[index].id} @ {displaytime(time, timespan)[9:]}")
    labela = Label(hist_prod_disp, text = "Time").grid(column = 0, row = 0)
    labelb = Label(hist_prod_disp, text = "Location").grid(column = 1, row = 0)
    labelc = Label(hist_prod_disp, text = "Status").grid(column = 2, row = 0)
    labeld = Label(hist_prod_disp, text = "Component").grid(column = 3, row = 0)
    for i in range(len(product_list[locktarget].history[0])):
        if i == 0:
            label1 = Label(hist_prod_disp, text=displaytime(locktarget, timespan)[:5]).grid(column=0, row=i+1)
        else:
            a = i - 1 + locktarget
            label1 = Label(hist_prod_disp, text=displaytime(a, timespan)).grid(column=0, row=i+1)
        label2 = Label(hist_prod_disp, text=product_list[locktarget].history[0][i]).grid(column=1, row=i + 1)
        if i + 1 < len(product_list[locktarget].history[0]):
            stat = product_list[locktarget].history[2][i]
        else:
            if product_list[locktarget].location.id == workstation_list[-1].id:
                stat = "Done"
            elif product_list[locktarget].history[0][-1] != product_list[locktarget].history[0][-2]:
                if product_list[locktarget].empty == 1:
                    stat = "Lack of component"
                else:
                    stat = "In progress"
            elif product_list[locktarget].history[2][-1] == "Waiting":
                stat = "Waiting"
            elif product_list[locktarget].empty == 1:
                stat = "Lack of component"
            elif product_list[locktarget].empty == 0:
                stat = "In progress"
        label3 = Label(hist_prod_disp, text=stat).grid(column=2, row=i + 1)
        if len(product_list[locktarget].history[1][i]) == 0:
            show = "None  "
        else:
            show = ""
            for j in range(len(product_list[locktarget].history[1][i])):
                show += f"{product_list[locktarget].history[1][i][j]}, "
        label4 = Label(hist_prod_disp, text=show[:-2]).grid(column=3, row=i + 1)


def find_product_index(item):
    index = -1
    for i in range(len(product_list)):
        if str(item) == str(product_list[i].id):
            index = i
    return index

#_______________________________________________________________________________________________________________________
# MAIN WINDOW
main_window = Tk()
main_window.title('Line 404')
main_window.geometry('1000x1000')


blanc = PhotoImage(file = "img_px.png")
arrowright = PhotoImage(file = "right.png")
arrowup = PhotoImage(file = "up.png")
arrowdown = PhotoImage(file = "down.png")


menubar = Menu(main_window)

main = Menu(menubar, tearoff = 0)
main.add_command(label = "Reset Config", command = lambda : pre_config_menu())
main.add_command(label = "Exit", command = main_window.quit)
menubar.add_cascade(label = "Menu", menu = main)

history = Menu(menubar, tearoff = 0)
history.add_command(label = "Product", command = lambda : history_product())
global history_ws
history_ws = Menu(history, tearoff = 0)
history.add_cascade(label = "Workstation", menu = history_ws)
menubar.add_cascade(label = "History", menu = history)

add_mat = Menu(menubar, tearoff = 0)
add_mat.add_command(label = f"Manual addition", command = lambda : more_addition())
add_mat.add_command(label = f"Smart addition", command = lambda : smart_addition())
global quick_add
quick_add = Menu(add_mat, tearoff = 0)
add_mat.add_cascade(label = "Quick addition", menu = quick_add)
menubar.add_cascade(label = "Add Material", menu = add_mat)

main_window.config(menu = menubar)

main_window.mainloop()
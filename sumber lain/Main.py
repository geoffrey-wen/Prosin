from Workstation import Workstation
from Product import Product
from Material import Material
from Display import displaytime

# MAKING WORKSTATIONS
number_of_workstation = int(input("Number of Process Workstation = "))

workstation_name_list = []
for i in range(number_of_workstation):
    workstation_name_list.append(input(f"Workstation {i+1} name: "))

workstation_list = []
temp = Workstation("endinventory", None)
workstation_list.append(temp)
for i in range(len(workstation_name_list) - 1, -1, -1):
    temp = Workstation(workstation_name_list[i], temp)
    workstation_list.insert(0, temp)

# MAKING WORKSTAION'S BUFFERS
workstation_buffer_list = []
for i in range(len(workstation_name_list)):
    buffername = f"Buffer-{workstation_name_list[i]}"
    temp = Workstation(buffername, workstation_list[i])
    workstation_buffer_list.append(temp)

# SUPPLYING MATERIAL TO THE BUFFERS
material_list = []
material_type_list = []
for i in range(len(workstation_buffer_list)):
    print(" ")
    number_of_material = int(input(f"Number of Supply for {workstation_list[i].id} =  "))
    material_type = input(f"Supply type for {workstation_list[i].id}: ")
    material_list_in_buffer = []
    for j in range(number_of_material):
        id = input(f"#{j+1} material id for {workstation_list[i].id} : ")
        material_list_in_buffer.append(Material(id, workstation_buffer_list[i], material_type))
        workstation_buffer_list[i].products.append(Material(id, workstation_buffer_list[i], material_type))
    material_list.append(material_list_in_buffer)
    material_type_list.append(material_type)

# DETERMINE RESOURCES NEEDED BY EACH WORKSTATION
resource_formula = []
print(" ")
print("Resources needed to make a product")
for i in range(len(workstation_buffer_list)):
    temp = int(input(f"Number of {material_type_list[i]} needed: "))
    resource_formula.append(temp)

# DEFINING TIME VECTOR
print(" ")
timespan = int(input("Timespan : "))
time = 0

# DEFINING PRODUCT
product_list = []

# MAINLOOP
while True:
    print(f"""
________________________________________________________________________________________________________________________

Time : {displaytime(time,timespan)[:5]}
Menu
t: Time flow a timespan
c: Print current condition
h: Print history
a: Add material
x: End loop""")
    task = input(">> ")
    # TIME FLOW
    if task.lower() == "t":
        time += 1
        # MOVING PRODUCT
        if len(product_list) > 0:
            for i in range(len(product_list)):
                index = -1
                for j in range(len(workstation_list)-1):
                    if str(product_list[i].location.id) == str(workstation_list[j].id):
                        index = j
                if index >= 0:
                    product_list[i].move(index, resource_formula[index])
                else :
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
        for i in range(len(workstation_buffer_list)):
            show = ""
            for j in range(resource_formula[i]):
                if len(workstation_list[i].products) > 0:
                    if (len(workstation_buffer_list[i].products) == 0):
                        show = (f"There is no {material_type_list[i]} for Station {workstation_list[i].id}")
                        workstation_list[i].fromworkstationtoproduct(product_list, 1)
                    else:
                        for k in range(len(material_list[i])):
                            if material_list[i][k].id == workstation_buffer_list[i].products[0].id:
                                index = k
                        loc = workstation_buffer_list[i].products[0].process(i, resource_formula[i])
                        material_list[i][index].location = loc
                        workstation_list[i].fromworkstationtoproduct(product_list, 0)
            if len(show) > 0:
                print(show)
        # WRITING WORKSTATION'S HISTORY
        for i in range(len(workstation_list)):
            workstation_list[i].writeworkstationhistory()
        # WRITING WORKSTATION'S BUFFER'S HISTORY
        for i in range(len(workstation_buffer_list)):
            workstation_buffer_list[i].writeworkstationhistory()
        # WRITING PRODUCT'S HISTORY
        for i in range(len(product_list)):
            product_list[i].writeproducthistory()
    # PRINT CURRENT CONDITION
    elif task.lower() == "c":
        print("""
Print current condition     
p: product
w: workstation
m: material""")
        taskp = input(">> c/")
        # PRINT CURRENT PRODUCT CONDITION
        if taskp.lower() == "p":
            for i in range(len(product_list)):
                show = [[],[],[],[]]
                show[0] = f"{i+1}. Product: {product_list[i].id}"
                show[0] += " " * (10 - len(product_list[i].id))
                show[0] += f"Station: {product_list[i].location.id}"
                print(show[0])
                tab = " " * (len(str(i+1))+2)
                temp = tab + f"Component: "
                sum = 0
                for j in range(len(product_list[i].component)):
                    for k in range(len(product_list[i].component[j])):
                        sum += 1
                if sum == 0:
                    temp += "None"
                else:
                    for j in range(len(product_list[i].component)):
                        if len(product_list[i].component[j]) > 0:
                            for k in range(len(product_list[i].component[j])):
                                temp += product_list[i].component[j][k].id + ", "
                    temp = temp[:-2]
                show[1] = temp[0:120]
                print(show[1])
                if len(temp) > 120:
                    a = 240-len(tab)
                    show[2] = tab + temp[0:a]
                    print(show[2])
                    if len(temp) > a:
                        b = 360-2*len(tab)
                        if len(temp) <= b:
                            show[3] = tab + temp[a:b]
                            print(show[3])
                        else:
                            c = 360-2*len(tab)-4
                            show[3] = tab + temp[a:c] + " ..."
                            print(show[3])
        # PRINT CURRENT WORKSTATION CONDITION
        elif taskp.lower() == "w":
            print("Workstation :")
            for i in range(len(workstation_list)):
                show = f"{i + 1}. Station: {workstation_list[i].id}"
                show += " " * (30 - len(workstation_list[i].id))
                if len(workstation_list[i].products) > 0:
                    show += f"Product: "
                    for j in range(len(workstation_list[i].products)):
                        show += f"{workstation_list[i].products[j].id}, "
                    show = show[:-2]
                else:
                    show += "Product: None"
                print(show)
            print("Buffer :")
            for i in range(len(workstation_buffer_list)):
                show = f"{i + 1}. Station: {workstation_buffer_list[i].id}"
                show += " " * (30 - len(workstation_buffer_list[i].id))
                if len(workstation_buffer_list[i].products) > 0:
                    show += f"Material: "
                    for j in range(len(workstation_buffer_list[i].products)):
                        show += f"{workstation_buffer_list[i].products[j].id}, "
                    show = show[:-2]
                else:
                    show += "Material: None"
                print(show)
        # PRINT CURRENT MATERIAL CONDITION
        elif taskp.lower() == "m":
            for i in range(len(material_list)):
                print(f"Type : {material_list[i][0].type}")
                count = 1
                for j in range(len(material_list[i])):
                    show = f"{count}. Material: {material_list[i][j].id}"
                    show += " " * (30 - len(material_list[i][j].id))
                    show += f"Location: {material_list[i][j].location.id}"
                    print(show)
                    count += 1
        else:
            print("""
Command not found""")
    # PRINT HISTORY
    elif task.lower() == "h":
        print("""
Print history     
p: product
w: workstation""")
        taskh = input(">> h/")
        # PRINT PRODUCT HISTORY
        if taskh.lower() == "p":
            target = input("Product ID: ")
            locktarget = -1
            for i in range(len(product_list)):
                if str(target.lower()) == str(product_list[i].id.lower()):
                    locktarget = i
            if locktarget >= 0:
                print(f"History: {product_list[locktarget].id}")
                for i in range(len(product_list[locktarget].history[0])):
                    if i == 0:
                        display = displaytime(locktarget, timespan)
                        display = display[:5] + "        "
                    else :
                        a = i-1+locktarget
                        display = displaytime(a, timespan)
                    show = f"{display}    Loc: {product_list[locktarget].history[0][i]}"
                    show += " " * (25 - len(product_list[locktarget].history[0][i]))
                    if i+1 < len(product_list[locktarget].history[0]):
                        a = product_list[locktarget].history[2][i]
                    else:
                        if product_list[locktarget].location.id == workstation_list[-1].id:
                            a = "Done"
                        elif product_list[locktarget].history[0][-1] != product_list[locktarget].history[0][-2]:
                            if product_list[locktarget].empty == 1:
                                a = "Lack of component"
                            else:
                                a = "In progress"
                        elif product_list[locktarget].history[2][-1] == "Waiting":
                            a = "Waiting"
                        elif product_list[locktarget].empty == 1:
                            a = "Lack of component"
                        elif product_list[locktarget].empty == 0:
                            a = "In progress"
                    show += f"Stat: {a}"
                    show += " " * (20 - len(a))
                    show += f"Comp: "
                    if len(product_list[locktarget].history[1][i]) == 0:
                        show += "None  "
                    else:
                        for j in range(len(product_list[locktarget].history[1][i])):
                            show += f"{product_list[locktarget].history[1][i][j]}, "
                    print(show[:-2])
            else:
                print("Product not found")
        # PRINT WORKSTATION HISTORY
        elif taskh.lower() == "w":
            target = input("Workstation name: ")
            locktarget = -1
            for i in range(len(workstation_list)):
                if str(target.lower()) == str(workstation_list[i].id.lower()):
                    locktarget = i
            if locktarget>=0:
                print(f"History: {workstation_list[locktarget].id}")
                for i in range(len(workstation_list[locktarget].history)):
                    show = f"{displaytime(i, timespan)}    "
                    if len(workstation_list[locktarget].history[i]) > 1:
                        show += f"{workstation_list[locktarget].history[i][0]}"
                        for j in range(1, len(workstation_list[locktarget].history[i])):
                            show += f", {workstation_list[locktarget].history[i][j]}"
                    elif len(workstation_list[locktarget].history[i]) == 1:
                        show += f"{workstation_list[locktarget].history[i][0]}"
                    else:
                        show += "None"
                    print(show)
            else:
                print("Workstation not found")
        else:
            print("""
Command not found""")
    # ADD MATERIAL
    elif task.lower() == "a":
        target = input("Supplied workstation: ")
        locktarget = -1
        for i in range(len(workstation_list)):
            if str(target.lower()) == str(workstation_list[i].id.lower()):
                locktarget = i
        if locktarget >= 0:
            number_of_material = int(input(f"Number of Supply for {workstation_list[locktarget].id} =  "))
            material_type = material_list[locktarget][0].type
            material_list_in_buffer = []
            for j in range(number_of_material):
                id = input(f"#{len(material_list[locktarget]) + 1} material id for {workstation_list[i].id} : ")
                temp = Material(id, workstation_buffer_list[locktarget], material_type)
                workstation_buffer_list[locktarget].products.append(temp)
                material_list[locktarget].append(temp)
        else:
            print("Workstation not found")
    # EXIT LOOP
    elif task.lower() == "x":
        print("""
Thank You""")
        break
    else:
        print("""
Command not found""")

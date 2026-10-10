import garage

flag = True
garage.create_table_cars()
garage.create_table_spareParts()

while(flag):
    print("\n --- Welcome to the Vehicle Garage Management System --- \n")

    print("1. Insert Cars\n2. Display Cars\n3. Insert Spare Parts\n4. Display Spare Parts\n5. Exit\n")
    choice = int(input("Enter your Choice: "))

    match choice:
        case 1:
            print("\n --- Insert Cars --- \n")
            make = input("Enter Make: ")
            model = input("Enter Model: ")
            year = int(input("Enter Year: "))
            color = input("Enter Color: ")
            license = input("Enter License Plate: ")
            owner_name = input("Enter Owner Name: ")
            garage.insert_data_into_cars(make, model, year, color, license, owner_name)
        case 2:
            print("\n --- Cars in the Garage. ---")
            garage.display_cars()
        case 3:
            print("\n --- Insert Spare Parts --- \n")
            part_name = input("Enter Part Name: ")
            part_number = input("Enter Part Number: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            garage.insert_data_into_spareParts(part_name, part_number, price, quantity)
        case 4:
            print("\n --- Spare Parts in the Garage. --- \n")
            garage.display_spareParts()
        case 5:
            print("Exiting the program.")
            flag = False
        case _:
            print("Wrong Choice!")
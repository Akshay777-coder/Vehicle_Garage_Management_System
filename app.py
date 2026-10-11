from unittest import case, main
import sys
import garage

garage.create_table_cars()
garage.create_table_spareParts()

def cars():
    flag = True
    while(flag):
        print("\n *** Welcome to the Cars Section *** \n")
        print("1. Insert Cars\n2. Display Cars\n3. Update Cars\n4. Delete Cars\n5. Back to Main Menu\n6. Exit\n")
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
                garage.display_cars()
            case 3:
                print("\n --- Update Cars --- \n")
                car_id = int(input("Enter Car ID: "))
                new_make = input("Enter New Make: ")
                new_model = input("Enter New Model: ")
                new_year = int(input("Enter New Year: "))
                new_color = input("Enter New Color: ")
                license = input("Enter License Plate: ")
                owner_name = input("Enter Owner Name: ")
                garage.update_cars(car_id, new_make, new_model, new_year, new_color, license, owner_name)
            case 4:
                print("\n --- Delete Cars --- \n")
                car_id = int(input("Enter Car ID: "))
                print(f"Are you sure you want to delete the car with ID {car_id}? (yes/no)", end="")
                confirmation = input().strip().lower()
                if confirmation == "yes":
                    garage.delete_cars(car_id)
                else:
                    print("Deletion cancelled.")
            case 5:
                print("\nReturning to Main Menu...")
                flag = False
            case 6:
                print("Exiting the program.")
                sys.exit(0)
            case _:
                print("Wrong Choice!")

def spare_parts():
    flag = True
    while(flag):
        print("\n *** Welcome to the Spare Parts Section *** \n")
        print("1. Insert Spare Parts\n2. Display Spare Parts\n3. Update Spare Parts\n4. Delete Spare Parts\n5. Back to Main Menu\n6. Exit\n")
        choice = int(input("Enter your Choice: "))
        match choice:
            case 1:
                print("\n --- Insert Spare Parts --- \n")
                part_name = input("Enter Part Name: ")
                part_number = input("Enter Part Number: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                garage.insert_data_into_spareParts(part_name, part_number, price, quantity)
            case 2:
                garage.display_spareParts()
            case 3:
                print("\n --- Update Spare Parts --- \n")
                part_id = int(input("Enter part Id: "))
                new_part_name = input("Enter New Part Name: ")
                new_part_number = input("Enter Part Number: ")
                new_price = float(input("Enter New Price: "))
                new_quantity = int(input("Enter New Quantity: "))
                garage.update_spareParts(part_id, new_part_name, new_part_number, new_price, new_quantity)
            case 4:
                print("\n --- Delete Spare Parts --- \n")
                part_id = int(input("Enter Part ID: "))
                print(f"Are you sure you want to delete the spare part with ID {part_id}? (yes/no)", end="")
                confirmation = input().strip().lower()
                if confirmation == "yes":
                    garage.delete_spareParts(part_id)
                else:
                    print("Deletion cancelled.")
            case 5:
                print("\nReturning to Main Menu...")
                flag = False
            case 6:
                print("\nExiting the program...")
                sys.exit(0)
            case _:
                print("Wrong Choice!")
def main():
    flag = True
    while(flag):
        print("\n *** Welcome to the Vehicle Garage Management System *** \n")
        print("1. Cars\n2. Spare Parts\n3. Exit\n")
        choice = int(input("Enter your Choice: "))
        match choice:
            case 1:
                cars()
            case 2:
                spare_parts()
            case 3:
                print("\nExiting the program...")
                flag = False
            case _:
                print("Wrong Choice!")

main()
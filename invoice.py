import sqlite3
import garage
import datetime

def total():
    conn = garage.create_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(price) FROM spare_parts")

    sums = cursor.fetchall()

    for sum in sums:
        total_amount = sum[0]

    conn.commit()
    conn.close()

    return total_amount


def create_invoice(car_id, owner_name):
    horizontal_line = 92
    print("*" * horizontal_line)
    print(" " * 21,"____ Vehicle Garage Management System ___")
    print("\n  Owner Name: ", owner_name)
    print("  Car ID: ", car_id)
    print("  Invoice Date:", datetime.datetime.now().strftime("%d-%m-%Y"))
    print("  Invoice Time:", datetime.datetime.now().strftime("%H:%M"), "\n")

    conn = garage.create_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM spare_parts WHERE car_id = ?", (car_id,))

    rows = cursor.fetchall()

    print(" " * 21,f"{'Spare Part':<15} | {'Quantity':<10} | {'Price':<10}")
    print(" " * 21,"-" * 40)

    if rows:
        for row in rows:
            print(" " * 21,f"{row[1]:<15} | {row[2]:<10} | ${row[3]:<10}")
            print(" " * 21,"-" * 40)
    else:
        print(" " * 21,"No spare parts found for this car.")

    
    conn.commit()
    conn.close()

    print("\n  Total Amount: ", total(), "$", "\n")

    print("*" * horizontal_line)
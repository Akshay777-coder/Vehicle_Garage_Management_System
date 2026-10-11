import sqlite3
import os

# Database directory
database_name = 'database'

# current worling dir path
path = os.path.join(os.getcwd(), database_name)

# Check if dir exists
if not os.path.exists(path):
    os.mkdir(path)

# Database file name
Database = 'database\\vehicle_garage.db'

# Create a connection to the SQLite database
def create_db():
    conn = sqlite3.connect(Database)
    return conn

# Create the cars table if it doesn't exist
def create_table_cars():
    conn = create_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            color TEXT NOT NULL,
            license_plate TEXT NOT NULL UNIQUE,
            owner_name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Delete row from cars
def delete_car(car_id):
    conn = create_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cars WHERE car_id = ?",(car_id,))
    
    conn.commit()

    print(f"Successfully deleted row where car id was {car_id}")

    conn.close()

# Create the spareParts table if it doesn't exist
def create_table_spareParts():
    conn = create_db()
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS spare_parts (
                part_id INTEGER PRIMARY KEY AUTOINCREMENT,
                part_name TEXT NOT NULL,
                part_number TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)
    
    conn.commit()
    conn.close()

# Delete row from cars
def delete_car(car_id):
    conn = create_db()
    cursor = conn.cursor()
                                                  cursor.execute("DELETE FROM spare_parts WHERE part_id = ?",(part_id,))

    conn.commit()                             
    print(f"Successfully deleted row where part id was {car_id}")
                                                  conn.close()

# insert data into cars table
def insert_data_into_cars(make, model, year, color, licence_plate, owner_name):
    conn = create_db()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO cars (make, model, year, color, license_plate, owner_name)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (make, model, year, color, licence_plate, owner_name))

        conn.commit()
        print(f"Car inserted successfully! Car ID: {cursor.lastrowid}\n")

    except sqlite3.Error as e:
        print(f"Error inserting data into cars table: {e}")
    finally:
        conn.close()

# Insert data into spareParts table
def insert_data_into_spareParts(part_name, part_number, price, quantity):
    conn = create_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO spare_parts (part_name, part_number, price, quantity)
            VALUES (?, ?, ?, ?)
        """, (part_name, part_number, price, quantity))

        conn.commit()
        print(f"Spare part inserted successfully! Part ID: {cursor.lastrowid}\n")
    except sqlite3.Error as e:
        print(f"Error inserting data into spare parts table: {e}")
    finally:
        conn.close()

# Display all cars
def display_cars():
    conn = create_db()

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM cars")

        rows = cursor.fetchall()

        if not rows:
            print("No cars found in the garage.")
            return

        print("\nCarId\tMake\tModel\tYear\tColor\tLicencePlate\tOwnerName")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t\t{row[6]}")
        print("--- End of Cars List ---\n")
    except sqlite3.Error as e:
        print(f"Error displaying cars: {e}")
    finally:
        conn.close()

# Display all spare parts
def display_spareParts():
    conn = create_db()

    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM spare_parts")
    
        rows = cursor.fetchall()
        
        print("\nPartId\tPartName\tPartNumber\tPrice\tQuantity")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t\t{row[6]}")
        print("--- End of Spare Parts List ---\n")
    except sqlite3.Error as e:
        print(f"Error displaying spare parts: {e}")
    finally:
        conn.close()

import sqlite3
import datetime
from datetime import datetime
def create_table():
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_name TEXT NOT NULL,
            vehicle_number TEXT NOT NULL,
            vehicle_type TEXT NOT NULL,
            in_time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_vehicle():
    owner_name = input("Enter Owner Name: ")
    vehicle_number = input("Enter Vehicle Number: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike): ")
    in_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO vehicles (owner_name, vehicle_number, vehicle_type, in_time)
        VALUES (?, ?, ?, ?)
    ''', (owner_name, vehicle_number, vehicle_type, in_time))
    conn.commit()
    conn.close()
    print("🚗 Vehicle inserted successfully!\n")

def view_vehicles():
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("\n--- All Vehicles ---")
        for row in rows:
            print(f"ID: {row[0]}, Owner: {row[1]}, Number: {row[2]}, Type: {row[3]}, In-Time: {row[4]}")
        print()
    else:
        print("No vehicles found.\n")

def main():
    create_table()

vehicles = []

while True:
    print("====== Parking Management System ======")
    print("1. Add Vehicle")
    print("2. View All Vehicles")
    print("3. Exit")
    print("4. Delete Vehicle")
    choice = input("Enter your choice: ")

    if choice == '1':
        owner = input("Enter Owner Name: ")
        number = input("Enter Vehicle Number: ")
        vtype = input("Enter Vehicle Type (Car/Bike): ")
        in_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vehicles.append({
            "owner": owner,
            "number": number,
            "type": vtype,
            "in_time": in_time
        })
        print("🚗 Vehicle inserted successfully!\n")

    elif choice == '2':
        if not vehicles:
            print("🚫 No vehicles found.\n")
        else:
            print("--- All Vehicles ---")
            for i, v in enumerate(vehicles, start=1):
                in_time_str = v["in_time"]
                in_time = datetime.strptime(in_time_str, "%Y-%m-%d %H:%M:%S")
                now = datetime.now()
                duration = now - in_time
                minutes = int(duration.total_seconds() // 60)
                print(f"ID: {i}, Owner: {v['owner']}, Number: {v['number']}, Type: {v['type']}, Parked for: {minutes} minutes")
            print()

    elif choice == '4':
        vehicle_number = input("Enter vehicle number to delete: ").strip().lower()
        found = False
        for vehicle in vehicles:
            if vehicle["number"].strip().lower() == vehicle_number:
                vehicles.remove(vehicle)
                print("🚮 Vehicle deleted successfully!\n")
                found = True
                break
        if not found:
            print("⚠️ Vehicle not found.\n")

    elif choice == '3':
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice. Please try again.\n")  
import csv
import os.path

def write_user(addr, name):
    with open("users.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow((addr, name))

def check_user(addr):
    with open("users.csv", "r", encoding="utf-8", newline="") as file: 
            reader = csv.reader(file)
            for row in reader:
                if addr in row:
                    print(f"Hello, {row[1]}!")
                    break
            else:
                write_user(addr, input("Input your name: "))

def exists_user_csv(file):
    return  os.path.isfile(file)





from pathlib import Path
from csv import DictWriter

file_name = "phonebook.csv"
file_current_folder = Path(__file__).resolve().parent
file = open(f"{file_current_folder}/{file_name}", "a")

name = input("Name: ")
number = input("Number: ")

DictWriter(file, fieldnames=["name", "number"]).writerow({"name": name, "number": number})

file.close()

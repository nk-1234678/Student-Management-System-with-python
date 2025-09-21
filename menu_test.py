# # menu_fancy.py
# import json
# from tabulate import tabulate
# from colorama import Fore, Style, init
# import os

# init(autoreset=True)  # for colored text

# DATA_FILE = "student_data.json"

# # ------------------ Load/Save Data ------------------
# if os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "r") as f:
#         data_store = json.load(f)
# else:
#     data_store = {
#         "students": [],
#         "marks": [],
#         "fees": []
#     }

# # ------------------ Helper Functions ------------------
# def save_data():
#     with open(DATA_FILE, "w") as f:
#         json.dump(data_store, f, indent=4)

# def generate_id(list_name, key_name):
#     if not data_store[list_name]:
#         return 1
#     return max(item[key_name] for item in data_store[list_name]) + 1

# # ------------------ Menu Functions ------------------
# def show_students():
#     if not data_store["students"]:
#         print(Fore.YELLOW + "No students found!")
#         return
#     table = [[s["ID"], s["Name"], s["DOB"], s["Phone"], s["City"], s["Class"]] for s in data_store["students"]]
#     print(tabulate(table, headers=["ID", "Name", "DOB", "Phone", "City", "Class"], tablefmt="fancy_grid"))

# def add_student():
#     new_id = generate_id("students", "ID")
#     name = input("Enter name: ")
#     dob = input("Enter DOB (yyyy-mm-dd): ")
#     phone = input("Enter phone: ")
#     city = input("Enter city: ")
#     clas = int(input("Enter class: "))
#     data_store["students"].append({"ID": new_id, "Name": name, "DOB": dob, "Phone": phone, "City": city, "Class": clas})
#     save_data()
#     print(Fore.GREEN + f"✅ Student '{name}' added with ID {new_id}!")

# def show_marks():
#     if not data_store["marks"]:
#         print(Fore.YELLOW + "No marks recorded!")
#         return
#     table = [[m["MarksID"], m["StudentID"], m["PassingYear"], m["Class"], m["RollNo"], m["TotalMarks"]] for m in data_store["marks"]]
#     print(tabulate(table, headers=["Marks ID", "Student ID", "Year", "Class", "Roll No", "Total Marks"], tablefmt="fancy_grid"))

# def add_marks():
#     new_id = generate_id("marks", "MarksID")
#     student_id = int(input("Enter student ID: "))
#     passing_year = int(input("Enter passing year: "))
#     clas = int(input("Enter class: "))
#     roll_no = generate_id("marks", "RollNo")  # auto roll number
#     total_marks = int(input("Enter total marks: "))
#     data_store["marks"].append({
#         "MarksID": new_id,
#         "StudentID": student_id,
#         "PassingYear": passing_year,
#         "Class": clas,
#         "RollNo": roll_no,
#         "TotalMarks": total_marks
#     })
#     save_data()
#     print(Fore.GREEN + f"✅ Marks added for student ID {student_id}, Roll No {roll_no}!")

# def show_fees():
#     if not data_store["fees"]:
#         print(Fore.YELLOW + "No fees recorded!")
#         return
#     table = [[f["PaymentID"], f["StudentID"], f["Amount"], f["PayDate"], f["Mode"]] for f in data_store["fees"]]
#     print(tabulate(table, headers=["Payment ID", "Student ID", "Amount", "Date", "Mode"], tablefmt="fancy_grid"))

# def take_fees():
#     new_id = generate_id("fees", "PaymentID")
#     student_id = int(input("Enter student ID: "))
#     amount = float(input("Enter amount: "))
#     pay_date = input("Enter payment date (yyyy-mm-dd): ")
#     mode = input("Enter payment mode: ")
#     data_store["fees"].append({"PaymentID": new_id, "StudentID": student_id, "Amount": amount, "PayDate": pay_date, "Mode": mode})
#     save_data()
#     print(Fore.GREEN + f"✅ Fee of {amount} recorded for student ID {student_id}!")

# # ------------------ Main Menu Loop ------------------
# while True:
#     print(Fore.CYAN + "\n====== Student Management System ======")
#     print("1. Show student details")
#     print("2. Add student")
#     print("3. Show student marks")
#     print("4. Add student marks")
#     print("5. Show fees details")
#     print("6. Take fees")
#     print("7. Exit")

#     try:
#         choice = int(input("Enter your choice: "))
#     except:
#         print(Fore.RED + "❌ Invalid input! Enter a number 1-7.")
#         continue

#     if choice == 1:
#         show_students()
#     elif choice == 2:
#         add_student()
#     elif choice == 3:
#         show_marks()
#     elif choice == 4:
#         add_marks()
#     elif choice == 5:
#         show_fees()
#     elif choice == 6:
#         take_fees()
#     elif choice == 7:
#         print(Fore.CYAN + "Exiting program...")
#         break
#     else:
#         print(Fore.RED + "❌ Enter a valid number 1-7")



# student_gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

# ------------------ Data Storage ------------------
DATA_FILE = "student_data.json"

# Load or initialize data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data_store = json.load(f)
else:
    data_store = {"students": [], "marks": [], "fees": []}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data_store, f, indent=4)

# ------------------ ID Generator ------------------
def generate_id(section, key):
    if not data_store[section]:
        return 1
    else:
        return max(item[key] for item in data_store[section]) + 1

# ------------------ GUI Functions ------------------
def add_student():
    name = simpledialog.askstring("Student Name", "Enter student name:")
    dob = simpledialog.askstring("DOB", "Enter DOB (yyyy-mm-dd):")
    phone = simpledialog.askstring("Phone", "Enter phone number:")
    city = simpledialog.askstring("City", "Enter city:")
    clas = simpledialog.askinteger("Class", "Enter class:")
    
    if not (name and dob and phone and city and clas):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    new_id = generate_id("students", "ID")
    data_store["students"].append({"ID": new_id, "Name": name, "DOB": dob, "Phone": phone, "City": city, "Class": clas})
    save_data()
    messagebox.showinfo("Success", f"Student '{name}' added with ID {new_id}")

def show_students():
    window = tk.Toplevel(root)
    window.title("Student Details")
    
    cols = ["ID", "Name", "DOB", "Phone", "City", "Class"]
    tree = ttk.Treeview(window, columns=cols, show='headings')
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for student in data_store["students"]:
        tree.insert("", "end", values=[student[c] for c in cols])
    
    tree.pack(expand=True, fill="both")

def add_marks():
    if not data_store["students"]:
        messagebox.showwarning("Warning", "No students available. Add students first!")
        return
    
    sid = simpledialog.askinteger("Student ID", "Enter Student ID:")
    pyear = simpledialog.askinteger("Passing Year", "Enter passing year:")
    sroll = simpledialog.askinteger("Roll Number", "Enter roll number:")
    tmarks = simpledialog.askinteger("Total Marks", "Enter total marks:")
    clas = simpledialog.askinteger("Class", "Enter class:")
    
    new_id = generate_id("marks", "ID")
    data_store["marks"].append({"ID": new_id, "SID": sid, "PassingYear": pyear, "Roll": sroll, "TotalMarks": tmarks, "Class": clas})
    save_data()
    messagebox.showinfo("Success", f"Marks added for Student ID {sid}")

def show_marks():
    window = tk.Toplevel(root)
    window.title("Student Marks")
    
    cols = ["ID", "SID", "PassingYear", "Class", "Roll", "TotalMarks"]
    tree = ttk.Treeview(window, columns=cols, show='headings')
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for mark in data_store["marks"]:
        tree.insert("", "end", values=[mark[c] for c in cols])
    
    tree.pack(expand=True, fill="both")

def take_fees():
    if not data_store["students"]:
        messagebox.showwarning("Warning", "No students available. Add students first!")
        return
    
    sid = simpledialog.askinteger("Student ID", "Enter Student ID:")
    amount = simpledialog.askfloat("Amount", "Enter amount paid:")
    mop = simpledialog.askstring("Mode of Payment", "Enter mode of payment:")
    
    new_id = generate_id("fees", "ID")
    data_store["fees"].append({"ID": new_id, "SID": sid, "Amount": amount, "Mode": mop})
    save_data()
    messagebox.showinfo("Success", f"Fees recorded for Student ID {sid}")

def show_fees():
    window = tk.Toplevel(root)
    window.title("Fees Details")
    
    cols = ["ID", "SID", "Amount", "Mode"]
    tree = ttk.Treeview(window, columns=cols, show='headings')
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for fee in data_store["fees"]:
        tree.insert("", "end", values=[fee[c] for c in cols])
    
    tree.pack(expand=True, fill="both")

# ------------------ Main Window ------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x450")

tk.Label(root, text="📚 Student Management System", font=("Helvetica", 16, "bold")).pack(pady=20)

tk.Button(root, text="Add Student", width=25, command=add_student).pack(pady=5)
tk.Button(root, text="Show Students", width=25, command=show_students).pack(pady=5)
tk.Button(root, text="Add Marks", width=25, command=add_marks).pack(pady=5)
tk.Button(root, text="Show Marks", width=25, command=show_marks).pack(pady=5)
tk.Button(root, text="Take Fees", width=25, command=take_fees).pack(pady=5)
tk.Button(root, text="Show Fees", width=25, command=show_fees).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

root.mainloop()

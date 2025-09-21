import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

# ------------------ Data Storage ------------------
DATA_FILE = "student_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data_store = json.load(f)
else:
    data_store = {"students": [], "marks": [], "fees": []}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data_store, f, indent=4)

def generate_id(section, key):
    if not data_store[section]:
        return 1
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
    window.geometry("700x400")
    window.config(bg="#e0f7fa")
    
    cols = ["ID", "Name", "DOB", "Phone", "City", "Class"]
    tree = ttk.Treeview(window, columns=cols, show='headings', height=15)
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fieldbackground="#f1f8e9")
    style.map('Treeview', background=[('selected', '#4fc3f7')])
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    
    for student in data_store["students"]:
        tree.insert("", "end", values=[student[c] for c in cols])

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
    window.geometry("700x400")
    window.config(bg="#fff3e0")
    
    cols = ["ID", "SID", "PassingYear", "Class", "Roll", "TotalMarks"]
    tree = ttk.Treeview(window, columns=cols, show='headings', height=15)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fieldbackground="#fff9c4")
    style.map('Treeview', background=[('selected', '#ffb74d')])
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    
    for mark in data_store["marks"]:
        tree.insert("", "end", values=[mark[c] for c in cols])

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
    window.geometry("500x400")
    window.config(bg="#f3e5f5")
    
    cols = ["ID", "SID", "Amount", "Mode"]
    tree = ttk.Treeview(window, columns=cols, show='headings', height=15)
    scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fieldbackground="#fce4ec")
    style.map('Treeview', background=[('selected', '#f06292')])
    
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    
    for fee in data_store["fees"]:
        tree.insert("", "end", values=[fee[c] for c in cols])

# ------------------ Main Window ------------------
root = tk.Tk()
root.title("📚 Student Management System")
root.geometry("420x520")
root.config(bg="#e0f7fa")

tk.Label(root, text="📚 Student Management System", font=("Helvetica", 18, "bold"), bg="#e0f7fa").pack(pady=20)

# Fancy Buttons
button_specs = [
    ("Add Student", add_student, "#4caf50"),
    ("Show Students", show_students, "#2196f3"),
    ("Add Marks", add_marks, "#ff9800"),
    ("Show Marks", show_marks, "#ff5722"),
    ("Take Fees", take_fees, "#9c27b0"),
    ("Show Fees", show_fees, "#e91e63"),
    ("Exit", root.destroy, "#f44336")
]

for text, func, color in button_specs:
    tk.Button(root, text=text, width=30, height=2, bg=color, fg="white",
              font=("Helvetica", 12, "bold"), activebackground="#555555",
              command=func).pack(pady=5)

root.mainloop()

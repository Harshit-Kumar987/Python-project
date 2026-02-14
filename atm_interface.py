import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# ---------- MySQL Connection ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",  # change if needed
    database="atm_project"
)
cursor = db.cursor(dictionary=True)

# ---------- Helper Functions ----------
def create_account():
    name = name_entry.get()
    dob = dob_entry.get()
    gender = gender_combo.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    acc_type = acc_type_combo.get()
    pin = pin_entry.get()
    deposit = deposit_entry.get()

    if not (name and dob and gender and mobile and email and address and acc_type and pin and deposit):
        messagebox.showerror("Error", "All fields are required!")
        return

    if len(pin) != 4 or not pin.isdigit():
        messagebox.showerror("Error", "PIN must be 4 digits.")
        return

    try:
        deposit = float(deposit)
    except:
        messagebox.showerror("Error", "Deposit must be a number.")
        return

    cursor.execute("""
        INSERT INTO users (name, dob, gender, mobile, email, address, acc_type, pin, balance)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (name, dob, gender, mobile, email, address, acc_type, pin, deposit))
    db.commit()

    acc_no = cursor.lastrowid
    messagebox.showinfo("Success", f"Account Created Successfully!\nYour Account No: {acc_no}")
    register_window.destroy()

def open_register():
    global register_window, name_entry, dob_entry, gender_combo, mobile_entry, email_entry, address_entry, acc_type_combo, pin_entry, deposit_entry
    register_window = tk.Toplevel(root)
    register_window.title("Register Account")
    register_window.geometry("400x500")
    register_window.configure(bg="lightyellow")

    tk.Label(register_window, text="--- Register New Account ---", font=("Arial", 14, "bold"), bg="lightyellow").pack(pady=10)

    tk.Label(register_window, text="Full Name:", bg="lightyellow").pack()
    name_entry = tk.Entry(register_window)
    name_entry.pack()

    tk.Label(register_window, text="Date of Birth (YYYY-MM-DD):", bg="lightyellow").pack()
    dob_entry = tk.Entry(register_window)
    dob_entry.pack()

    tk.Label(register_window, text="Gender:", bg="lightyellow").pack()
    gender_combo = ttk.Combobox(register_window, values=["Male", "Female", "Other"])
    gender_combo.pack()

    tk.Label(register_window, text="Mobile No:", bg="lightyellow").pack()
    mobile_entry = tk.Entry(register_window)
    mobile_entry.pack()

    tk.Label(register_window, text="Email ID:", bg="lightyellow").pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()

    tk.Label(register_window, text="Address:", bg="lightyellow").pack()
    address_entry = tk.Entry(register_window)
    address_entry.pack()

    tk.Label(register_window, text="Account Type:", bg="lightyellow").pack()
    acc_type_combo = ttk.Combobox(register_window, values=["Saving", "Current"])
    acc_type_combo.pack()

    tk.Label(register_window, text="4-digit PIN:", bg="lightyellow").pack()
    pin_entry = tk.Entry(register_window, show="*")
    pin_entry.pack()

    tk.Label(register_window, text="Initial Deposit:", bg="lightyellow").pack()
    deposit_entry = tk.Entry(register_window)
    deposit_entry.pack()

    tk.Button(register_window, text="Create Account", command=create_account, bg="green", fg="white").pack(pady=15)

# ---------- Login ----------
def login_user():
    acc_no = acc_entry.get()
    pin = pin_entry_login.get()

    cursor.execute("SELECT * FROM users WHERE acc_no=%s AND pin=%s", (acc_no, pin))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login", f"Welcome {user['name']}!")
        login_window.destroy()
        user_dashboard(user)
    else:
        messagebox.showerror("Error", "Invalid Account Number or PIN")

def open_login():
    global login_window, acc_entry, pin_entry_login
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x250")
    login_window.configure(bg="lightblue")

    tk.Label(login_window, text="--- User Login ---", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(login_window, text="Account No:", bg="lightblue").pack()
    acc_entry = tk.Entry(login_window)
    acc_entry.pack()

    tk.Label(login_window, text="PIN:", bg="lightblue").pack()
    pin_entry_login = tk.Entry(login_window, show="*")
    pin_entry_login.pack()

    tk.Button(login_window, text="Login", command=login_user, bg="green", fg="white").pack(pady=15)

# ---------- Dashboard ----------
def user_dashboard(user):
    dash = tk.Toplevel(root)
    dash.title(f"Dashboard - {user['name']}")
    dash.geometry("400x400")
    dash.configure(bg="lightcyan")

    tk.Label(dash, text=f"Welcome, {user['name']}", font=("Arial", 16, "bold"), bg="lightcyan").pack(pady=10)
    bal_label = tk.Label(dash, text=f"Balance: ₹{user['balance']}", font=("Arial", 14), bg="lightcyan")
    bal_label.pack()

    def deposit_func():
        amount = float(simple_input("Deposit Amount"))
        if amount > 0:
            new_bal = user['balance'] + amount
            cursor.execute("UPDATE users SET balance=%s WHERE acc_no=%s", (new_bal, user['acc_no']))
            cursor.execute("INSERT INTO user_transactions (acc_no, trans_type, amount, balance, trans_time) VALUES (%s,%s,%s,%s,%s)",
                           (user['acc_no'], "Deposit", amount, new_bal, datetime.now()))
            db.commit()
            user['balance'] = new_bal
            bal_label.config(text=f"Balance: ₹{new_bal}")
            messagebox.showinfo("Success", f"Deposited ₹{amount}")

    def withdraw_func():
        amount = float(simple_input("Withdraw Amount"))
        if amount > user['balance']:
            messagebox.showerror("Error", "Insufficient Balance")
            return
        new_bal = user['balance'] - amount
        cursor.execute("UPDATE users SET balance=%s WHERE acc_no=%s", (new_bal, user['acc_no']))
        cursor.execute("INSERT INTO user_transactions (acc_no, trans_type, amount, balance, trans_time) VALUES (%s,%s,%s,%s,%s)",
                       (user['acc_no'], "Withdrawal", amount, new_bal, datetime.now()))
        db.commit()
        user['balance'] = new_bal
        bal_label.config(text=f"Balance: ₹{new_bal}")
        messagebox.showinfo("Success", f"Withdrawn ₹{amount}")

    def show_history_func():
        cursor.execute("SELECT * FROM user_transactions WHERE acc_no=%s ORDER BY trans_time DESC", (user['acc_no'],))
        data = cursor.fetchall()
        hist = tk.Toplevel(dash)
        hist.title("Transaction History")
        hist.geometry("500x300")
        tk.Label(hist, text="Date & Time\tType\tAmount\tBalance", font=("Arial", 10, "bold")).pack()
        for r in data:
            tk.Label(hist, text=f"{r['trans_time']}\t{r['trans_type']}\t₹{r['amount']}\t₹{r['balance']}").pack()

    tk.Button(dash, text="Deposit", command=deposit_func, bg="green", fg="white", width=20).pack(pady=5)
    tk.Button(dash, text="Withdraw", command=withdraw_func, bg="red", fg="white", width=20).pack(pady=5)
    tk.Button(dash, text="View Transactions", command=show_history_func, bg="blue", fg="white", width=20).pack(pady=5)

def simple_input(title):
    top = tk.Toplevel(root)
    top.title(title)
    top.geometry("250x120")
    tk.Label(top, text=title).pack(pady=5)
    entry = tk.Entry(top)
    entry.pack()
    value = []

    def submit():
        value.append(entry.get())
        top.destroy()

    tk.Button(top, text="OK", command=submit).pack(pady=5)
    top.wait_window()
    return float(value[0]) if value else 0

# ---------- Main Window ----------
root = tk.Tk()
root.title("ATM Management System")
root.geometry("400x300")
root.configure(bg="lightgray")

tk.Label(root, text="🏦 Welcome to My Bank 🏦", font=("Arial", 16, "bold"), bg="lightgray").pack(pady=20)
tk.Button(root, text="Register New Account", command=open_register, bg="green", fg="white", width=25).pack(pady=10)
tk.Button(root, text="Login to Account", command=open_login, bg="blue", fg="white", width=25).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=25).pack(pady=10)

root.mainloop()

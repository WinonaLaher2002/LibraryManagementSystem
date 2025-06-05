import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
import subprocess

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="pma",
        password="@Winonalaher2002",
        database="library_management"
    )

class LoginRegisterSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login/Register")
        self.geometry("1920x1080")
        self.configure(bg="#E3FEF7")
        self.role_var = tk.StringVar(value="User")

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()
        container = tk.Frame(self, bg="#E3FEF7")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Login", font=("Arial", 30, "bold"), bg="#E3FEF7", fg="#003C43").pack(pady=20)

        tk.Label(container, text="Role:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43").pack(pady=5)
        self.role_combobox = ttk.Combobox(container, textvariable=self.role_var, values=["User", "Admin"], state="readonly", font=("Arial", 20))
        self.role_combobox.pack(pady=5)

        self.username_label = tk.Label(container, text="Username:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(container, font=("Arial", 20))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(container, text="Password:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(container, show="*", font=("Arial", 20))
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(container, text="Login", command=self.login, bg="#135D66", fg="white", font=("Arial", 20))
        self.login_button.pack(pady=20)

        self.register_button = tk.Button(container, text="Register", command=self.create_register_frame, bg="#135D66", fg="white", font=("Arial", 20))
        self.register_button.pack(pady=10)

    def create_register_frame(self):
        self.clear_frame()
        container = tk.Frame(self, bg="#E3FEF7")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Register", font=("Arial", 30, "bold"), bg="#E3FEF7", fg="#003C43").pack(pady=20)

        tk.Label(container, text="Role:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43").pack(pady=5)
        self.role_combobox = ttk.Combobox(container, textvariable=self.role_var, values=["User", "Admin"], state="readonly", font=("Arial", 20))
        self.role_combobox.pack(pady=5)

        self.username_label = tk.Label(container, text="Username:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(container, font=("Arial", 20))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(container, text="Password:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(container, show="*", font=("Arial", 20))
        self.password_entry.pack(pady=5)

        self.confirm_password_label = tk.Label(container, text="Confirm Password:", font=("Arial", 20), bg="#E3FEF7", fg="#003C43")
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry = tk.Entry(container, show="*", font=("Arial", 20))
        self.confirm_password_entry.pack(pady=5)

        self.register_button = tk.Button(container, text="Register", command=self.register, bg="#135D66", fg="white", font=("Arial", 20))
        self.register_button.pack(pady=20)

        self.back_button = tk.Button(container, text="Back", command=self.create_login_frame, bg="#135D66", fg="white", font=("Arial", 20))
        self.back_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        role = self.role_var.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = connect_db()
        cursor = conn.cursor()

        if role == "User":
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        else:
            cursor.execute("SELECT * FROM admins WHERE admin_username = %s AND admin_password = %s", (username, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            if role == "User":
                messagebox.showinfo("Login Successful", "Welcome, User!")
                self.open_user_view()
            else:
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                self.open_admin_panel()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")           

    def register(self):
        role = self.role_var.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not (username and password and confirm_password):
            messagebox.showerror("Registration Error", "Please fill in all fields.")
        elif password != confirm_password:
            messagebox.showerror("Registration Error", "Passwords do not match.")
        else:
            conn = connect_db()
            cursor = conn.cursor()

            try:
                if role == "User":
                    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                else:
                    cursor.execute("INSERT INTO admins (admin_username, admin_password) VALUES (%s, %s)", (username, password))

                conn.commit()
                messagebox.showinfo("Registration Successful", "Registered successfully!")
                self.create_login_frame()
            except mysql.connector.Error as err:
                messagebox.showerror("Registration Error", f"Error: {err}")
            finally:
                conn.close()

    def open_admin_panel(self):
        subprocess.run(["python", "adminview.py"])        

    def open_user_view(self):
        subprocess.run(["python", "userview.py"])

if __name__ == "__main__":
    app = LoginRegisterSystem()
    app.mainloop()

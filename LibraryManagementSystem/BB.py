import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import subprocess

def borrow_book():
    book_id = book_id_entry.get()
    borrowed_time = borrowed_time_entry.get()

    if book_id and borrowed_time:
        try:
            cursor.execute("SELECT quantity FROM books WHERE book_id = %s", (book_id,))
            result = cursor.fetchone()
            
            if result:
                quantity = result[0]
                if quantity == 0:
                    messagebox.showerror("Error", "The book is already borrowed. Please return it before borrowing again.")
                    return

                borrowed_time_dt = datetime.strptime(borrowed_time, "%m/%d/%Y")
                cursor.execute(
                    "UPDATE books SET quantity = quantity - 1, borrowed_time = %s WHERE book_id = %s",
                    (borrowed_time_dt, book_id)
                )
                conn.commit()
                messagebox.showinfo("Success", "Book borrowed successfully!")
            else:
                messagebox.showerror("Error", "Book ID not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def back_to_admin_panel():
    root.destroy()  # Close the borrow book window
    subprocess.Popen(["python", "adminview.py"])  # Open adminview.py

conn = mysql.connector.connect(host="localhost", user="pma", password="@Winonalaher2002", database="library_management")
cursor = conn.cursor()

root = tk.Tk()
root.title("Borrow Book")
root.configure(bg="#E3FEF7")

header_label = tk.Label(root, text="Borrow Book", font=("Arial", 18, "bold"), bg="#E3FEF7", fg="#003C43")
header_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

labels = ["Book ID", "Borrowed Date (MM/DD/YYYY)"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text + ":", bg="#E3FEF7", fg="#003C43")
    label.grid(row=i+1, column=0, padx=10, pady=3, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=3, sticky="ew")
    entries.append(entry)

book_id_entry, borrowed_time_entry = entries

buttons = [("Borrow Book", borrow_book), ("Back to Admin Panel", back_to_admin_panel)]

for i, (button_text, command) in enumerate(buttons):
    button = tk.Button(root, text=button_text, command=command, fg="white", bg="#135D66")
    button.grid(row=i+len(labels)+1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

root.geometry("390x300")
root.mainloop()

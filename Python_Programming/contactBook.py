import tkinter as tk 
from tkinter import messagebox, simpledialog 
import csv 
import os 
 
FILENAME = 'contacts.csv' 
 
# Initialize file if not exists 
if not os.path.exists(FILENAME): 
    with open(FILENAME, mode='w', newline='') as file: 
        writer = csv.writer(file) 
        writer.writerow(['Name', 'Phone', 'Email', 'Address']) 
 
def add_contact(): 
    name = name_entry.get() 
    phone = phone_entry.get() 
    email = email_entry.get() 
    address = address_entry.get() 
 
    if name and phone: 
        with open(FILENAME, mode='a', newline='') as file: 
            writer = csv.writer(file) 
            writer.writerow([name, phone, email, address]) 
        messagebox.showinfo("Success", "Contact added successfully!") 
        clear_fields() 
    else: 
        messagebox.showerror("Error", "Name and Phone are required.") 
 
def view_contacts(): 
    listbox.delete(0, tk.END) 
    with open(FILENAME, mode='r') as file: 
        reader = csv.reader(file) 
        next(reader) 
        for row in reader: 
            listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}") 
 
def search_contact(): 
    keyword = search_entry.get().lower() 
    listbox.delete(0, tk.END) 
    with open(FILENAME, mode='r') as file: 
        reader = csv.reader(file) 
        next(reader) 
        for row in reader: 
            if keyword in row[0].lower() or keyword in row[1]: 
                listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}") 
 
def delete_contact(): 
    selected = listbox.curselection() 
    if not selected: 
        messagebox.showerror("Error", "Select a contact to delete.") 
        return 
 
    data = [] 
    with open(FILENAME, mode='r') as file: 
        reader = csv.reader(file) 
        header = next(reader) 
        for row in reader: 
            data.append(row) 
 
    contact_text = listbox.get(selected[0]) 
    to_delete = contact_text.split(" | ") 
    updated_data = [row for row in data if row[:2] != to_delete[:2]] 
 
    with open(FILENAME, mode='w', newline='') as file: 
        writer = csv.writer(file) 
        writer.writerow(header) 
        writer.writerows(updated_data) 
 
    messagebox.showinfo("Deleted", "Contact deleted successfully!") 
    view_contacts() 
 
def update_contact(): 
    selected = listbox.curselection() 
    if not selected: 
        messagebox.showerror("Error", "Select a contact to update.") 
        return 
 
    contact_text = listbox.get(selected[0]) 
    old_data = contact_text.split(" | ") 
 
    name = simpledialog.askstring("Update", "Enter new name:", initialvalue=old_data[0]) 
    phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=old_data[1]) 
    email = simpledialog.askstring("Update", "Enter new email:", initialvalue=old_data[2]) 
    address = simpledialog.askstring("Update", "Enter new address:", initialvalue=old_data[3]) 
 
    updated_data = [] 
    with open(FILENAME, mode='r') as file: 
        reader = csv.reader(file) 
        header = next(reader) 
        for row in reader: 
            if row[:2] == old_data[:2]: 
                updated_data.append([name, phone, email, address]) 
            else: 
                updated_data.append(row) 
 
    with open(FILENAME, mode='w', newline='') as file: 
        writer = csv.writer(file) 
        writer.writerow(header) 
        writer.writerows(updated_data) 
 
    messagebox.showinfo("Updated", "Contact updated successfully!") 
    view_contacts() 
 
def clear_fields(): 
    name_entry.delete(0, tk.END) 
    phone_entry.delete(0, tk.END) 
    email_entry.delete(0, tk.END) 
    address_entry.delete(0, tk.END) 
 
# GUI Setup 
root = tk.Tk() 
root.title("Contact Book") 
root.geometry("650x550") 
root.configure(bg="#f0f8ff") 
 
title = tk.Label(root, text="Contact Book", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#003366") 
title.pack(pady=10) 
 
frame = tk.Frame(root, bg="#f0f8ff") 
frame.pack(pady=5) 
 
# Input Fields 
labels = ["Name", "Phone", "Email", "Address"] 
entries = [] 
for i, text in enumerate(labels): 
    label = tk.Label(frame, text=text + ":", bg="#f0f8ff", font=("Arial", 12)) 
    label.grid(row=i, column=0, sticky="e", pady=5) 
    entry = tk.Entry(frame, width=40) 
    entry.grid(row=i, column=1, pady=5, padx=10) 
    entries.append(entry) 
name_entry, phone_entry, email_entry, address_entry = entries 
# Buttons 
btn_frame = tk.Frame(root, bg="#f0f8ff") 
btn_frame.pack(pady=10) 
tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, 
padx=5) 
tk.Button(btn_frame, text="View All", width=10, command=view_contacts).grid(row=0, column=1, 
padx=5) 
tk.Button(btn_frame, text="Update", width=10, command=update_contact).grid(row=0, column=2, 
padx=5) 
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=3, 
padx=5) 
# Search 
search_entry = tk.Entry(root, width=40) 
search_entry.pack(pady=5) 
tk.Button(root, text="Search by Name or Phone", command=search_contact).pack() 
# Display List 
listbox = tk.Listbox(root, width=80, height=10) 
listbox.pack(pady=10) 
root.mainloop() 
 
 
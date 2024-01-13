import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

class ShoppingBillGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping Bill Calculator")

        self.items = {}

        self.label_item = Label(master, text="Item:")
        self.label_item.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_item = Entry(master)
        self.entry_item.grid(row=0, column=1, padx=10, pady=10)

        self.label_price = Label(master, text="Price per unit:")
        self.label_price.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_price = Entry(master)
        self.entry_price.grid(row=1, column=1, padx=10, pady=10)

        self.label_quantity = Label(master, text="Quantity:")
        self.label_quantity.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_quantity = Entry(master)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=10)

        self.button_add_item = Button(master, text="Add Item", command=self.add_item)
        self.button_add_item.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_calculate_bill = Button(master, text="Calculate Bill", command=self.calculate_bill)
        self.button_calculate_bill.grid(row=4, column=0, columnspan=2, pady=10)

    def add_item(self):
        item_name = self.entry_item.get().strip().lower()

        if not item_name:
            messagebox.showwarning("Invalid Input", "Please enter a valid item name.")
            return

        try:
            price = float(self.entry_price.get())
            quantity = int(self.entry_quantity.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric values for price and quantity.")
            return

        self.items[item_name] = {'price': price, 'quantity': quantity}

        # Clear the entry fields
        self.entry_item.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def calculate_bill(self):
        total = 0

        if not self.items:
            messagebox.showwarning("No Items", "Please add items before calculating the bill.")
            return

        output = "\n*** Shopping Bill ***\n"
        output += "{:<15} {:<10} {:<10} {:<10}\n".format("Item", "Price", "Quantity", "Total")

        for item, details in self.items.items():
            price = details['price']
            quantity = details['quantity']
            item_total = price * quantity
            total += item_total

            output += "{:<15} ₹{:<10.2f} {:<10} ₹{:<10.2f}\n".format(item, price, quantity, item_total)

        output += "\nTotal Bill: ₹{:.2f}\n".format(total)

        # Display the output in a messagebox
        messagebox.showinfo("Shopping Bill", output)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingBillGUI(root)
    root.mainloop()

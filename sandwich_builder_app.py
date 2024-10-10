import tkinter as tk
from tkinter import messagebox

class Sandwich:
    def __init__(self, bread, filling, name):
        self.bread = bread
        self.filling = filling
        self.name = name

    def __str__(self):
        return f"{self.name}'s Sandwich: {self.bread} with {self.filling}"

def validate_entry(entry):
    return bool(entry)

class SandwichBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sandwich Builder")

        # Create the main window
        self.create_main_window()

    def create_main_window(self):
        # Labels
        self.label1 = tk.Label(self.root, text="Select Your Bread:")
        self.label1.grid(row=0, column=0)

        self.label2 = tk.Label(self.root, text="Select Your Filling:")
        self.label2.grid(row=1, column=0)

        self.label3 = tk.Label(self.root, text="Enter Your Name:")
        self.label3.grid(row=2, column=0)

        # Entry for user's name
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=2, column=1)

        # Bread options
        self.bread_var = tk.StringVar(value="Whole Wheat")  # Default selection
        bread_options = ["Whole Wheat", "White", "Rye"]
        for i, bread in enumerate(bread_options):
            tk.Radiobutton(self.root, text=bread, variable=self.bread_var, value=bread).grid(row=0, column=i+1)

        # Filling options
        self.filling_var = tk.StringVar(value="Turkey")  # Default selection
        filling_options = ["Turkey", "Ham", "Veggie"]
        for i, filling in enumerate(filling_options):
            tk.Radiobutton(self.root, text=filling, variable=self.filling_var, value=filling).grid(row=1, column=i+1)

        # Buttons with callbacks
        self.submit_button = tk.Button(self.root, text="Submit", command=self.open_summary_window)
        self.submit_button.grid(row=3, column=0)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=3, column=1)

    def open_summary_window(self):
        # Validation for entry box
        user_name = self.name_entry.get()
        if not validate_entry(user_name):
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        # Create new window for summary
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Order Summary")

        # Create a Sandwich object
        sandwich = Sandwich(self.bread_var.get(), self.filling_var.get(), user_name)

        # Display the order summary
        summary_label = tk.Label(summary_window, text=f"Your sandwich order: {sandwich}")
        summary_label.pack()

        # Confirm button
        confirm_button = tk.Button(summary_window, text="Confirm", command=summary_window.destroy)
        confirm_button.pack()

        # Go back button
        back_button = tk.Button(summary_window, text="Back", command=summary_window.destroy)
        back_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SandwichBuilderApp(root)
    root.mainloop()

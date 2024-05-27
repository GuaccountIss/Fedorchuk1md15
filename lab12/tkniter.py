mport tkinter as tk
from tkinter import messagebox

class IceCreamStandApp:
    def init(self, root):
        self.stand = IceCreamStand("Ледяная радость", "Кафе-мороженое", 4.5, ["Ванильное", "Шоколадное"], "Центр города", "10:00 - 22:00")

        root.title("Ice Cream Stand")
        root.geometry("400x400")

        self.description_label = tk.Label(root, text=self.stand.describe_restaurant(), justify="left")
        self.description_label.pack(pady=10)

        self.flavors_label = tk.Label(root, text="Сорта мороженого:", justify="left")
        self.flavors_label.pack()

        self.flavors_listbox = tk.Listbox(root)
        self.flavors_listbox.pack(pady=10)
        self.update_flavors_listbox()

        self.new_flavor_entry = tk.Entry(root)
        self.new_flavor_entry.pack()

        self.add_button = tk.Button(root, text="Добавить сорт", command=self.add_flavor)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Удалить сорт", command=self.remove_flavor)
        self.remove_button.pack(pady=5)

    def update_flavors_listbox(self):
        self.flavors_listbox.delete(0, tk.END)
        for flavor in self.stand.flavors:
            self.flavors_listbox.insert(tk.END, flavor)

    def add_flavor(self):
        new_flavor = self.new_flavor_entry.get()
        if new_flavor:
            message = self.stand.add_flavor(new_flavor)
            messagebox.showinfo("Информация", message)
            self.update_flavors_listbox()
            self.new_flavor_entry.delete(0, tk.END)

    def remove_flavor(self):
        selected_flavor = self.flavors_listbox.get(tk.ACTIVE)
        if selected_flavor:
            message = self.stand.remove_flavor(selected_flavor)
            messagebox.showinfo("Информация", message)
            self.update_flavors_listbox()

if name == "main":
    root = tk.Tk()
    app = IceCreamStandApp(root)
    root.mainloop()
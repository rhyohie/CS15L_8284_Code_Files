#----------initialization and formatting of Variables----------#
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name:20} | Qty: {self.quantity:5} | Price: ₱{self.price:8.2f} | Total: ₱{self.total_price():10.2f}"

#----------Main Class Inventory Manager with submethods code----------#
class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        new_item = Item(name, quantity, price)
        self.items.append(new_item)

    def update_quantity(self, name, new_quantity):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.quantity = new_quantity
                return f"Updated {name} quantity to {new_quantity}"
        return f"Item '{name}' not found!"

    def display_items(self):
        if not self.items:
            return "Inventory is empty."
        return "\n".join(str(item) for item in self.items)

    def total_inventory_value(self):
        return sum(item.total_price() for item in self.items)

#----------Main Interface and if-else control structure----------#
def main():
    inventory = InventoryManager()

    while True:
        print("="*50)
        print("\nWelcome to Inventory Management System")
        print("1. Add New Item")
        print("2. Update Item Quantity")
        print("3. Display All Items")
        print("4. Show Total Inventory Value")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print("="*50)

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: ₱"))
            inventory.add_item(name, quantity, price)
            print(f"Item '{name}' added!")
        elif choice == '2':
            name = input("Enter item name: ")
            new_quantity = int(input("Enter new quantity: "))
            print(inventory.update_quantity(name, new_quantity))
        elif choice == '3':
            print(inventory.display_items())
        elif choice == '4':
            print(f"Total Inventory Value: ₱{inventory.total_inventory_value():.2f}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
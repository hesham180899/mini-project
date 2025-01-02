# Class definition for Product
class Product:
    def __init__(self, name, price, quantity):
        """Initialize the product with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Display information about the product."""
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity Available: {self.quantity}")

    def update_quantity(self, amount):
        """Update the quantity of the product (negative for selling, positive for restocking)."""
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0  # Prevent negative quantity
            print(f"Warning: Quantity of {self.name} cannot be negative. Set to 0.")
        print(f"Updated Quantity of {self.name}: {self.quantity}")

    def total_value(self):
        """Calculate and return the total value of the product (price * quantity)."""
        return self.price * self.quantity

# Class definition for Inventory
class Inventory:
    def __init__(self):
        """Initialize the inventory with an empty list of products."""
        self.products = []

    def add_product(self, product):
        """Add a new product to the inventory."""
        self.products.append(product)
        print(f"Product '{product.name}' added to the inventory.")

    def display_inventory(self):
        """Display all products in the inventory."""
        if not self.products:
            print("The inventory is empty.")
        else:
            print("\nInventory Details:")
            for product in self.products:
                product.display_info()
                print("-" * 40)

    def total_inventory_value(self):
        """Calculate and display the total value of the inventory."""
        total_value = sum(product.total_value() for product in self.products)
        print(f"\nTotal Inventory Value: ${total_value:.2f}")
        return total_value

# Main function to simulate the scenario
def main():
    # Create an instance of Inventory
    store_inventory = Inventory()

    # Create some products and add them to the inventory
    product1 = Product("Laptop", 1000.00, 10)
    product2 = Product("Smartphone", 600.00, 20)
    product3 = Product("Headphones", 150.00, 50)

    store_inventory.add_product(product1)
    store_inventory.add_product(product2)
    store_inventory.add_product(product3)

    # Display all products in the inventory
    store_inventory.display_inventory()

    # Update the quantity of some products
    print("\nSelling 3 Laptops...")
    product1.update_quantity(-3)

    print("\nRestocking 5 Smartphones...")
    product2.update_quantity(5)

    print("\nSelling 10 Headphones...")
    product3.update_quantity(-10)

    # Display updated inventory
    print("\nUpdated Inventory Details:")
    store_inventory.display_inventory()

    # Calculate and display the total inventory value
    store_inventory.total_inventory_value()

# Run the main function
if __name__ == "__main__":
    main()

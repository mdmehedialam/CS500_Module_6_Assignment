"CS 500"
"Md Mehedi Alam"
"Module 6 Protofolio"
"Online Shopping Cart. Build the ShoppingCart class with the  data attributes and related methods."


class ItemToPurchase:
    """Class to represent an item that can be purchased"""
    
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
    
    def print_item_cost(self):
        """Print the item cost in the format: item_name quantity @ $price = $total"""
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")
    
    def print_item_description(self):
        """Print the item description in the format: item_name: description"""
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """Class to represent a shopping cart"""
    
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, item):
        """Add an item to cart_items list"""
        self.cart_items.append(item)
    
    def remove_item(self, item_name):
        """Remove item from cart_items list by item name"""
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        
        if not found:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item):
        """Modify an item's description, price, and/or quantity"""
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                # Only modify if the new item has non-default values
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                found = True
                break
        
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        """Return the total quantity of all items in cart"""
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        """Return the total cost of all items in cart"""
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        """Output the total of objects in cart"""
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        
        for item in self.cart_items:
            item.print_item_cost()
        
        print(f"Total: ${self.get_cost_of_cart()}")
    
    def print_descriptions(self):
        """Output each item's description"""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    """Print the menu and handle user input"""
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
        choice = input("Choose an option: ").lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'a':
            add_item_to_cart(cart)
        elif choice == 'r':
            remove_item_from_cart(cart)
        elif choice == 'c':
            change_item_quantity(cart)
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        else:
            print("Invalid choice. Please try again.")


def add_item_to_cart(cart):
    """Helper function to add an item to cart"""
    print("\nADD ITEM TO CART")
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    description = input("Enter the item description: ")
    
    item = ItemToPurchase(name, price, quantity, description)
    cart.add_item(item)
    print(f"Added {quantity} {name}(s) to cart")


def remove_item_from_cart(cart):
    """Helper function to remove an item from cart"""
    print("\nREMOVE ITEM FROM CART")
    name = input("Enter name of item to remove: ")
    cart.remove_item(name)


def change_item_quantity(cart):
    """Helper function to change item quantity"""
    print("\nCHANGE ITEM QUANTITY")
    name = input("Enter the item name: ")
    quantity = int(input("Enter the new quantity: "))
    
    # Create a temporary item with just the name and new quantity
    temp_item = ItemToPurchase(name, 0, quantity, "none")
    cart.modify_item(temp_item)


def main():
    """Main function to run the shopping cart program"""
    print("Welcome to the Online Shopping Cart!")
    
    # Get customer information
    customer_name = input("Enter customer name: ")
    current_date = input("Enter today's date: ")
    
    # Create shopping cart
    cart = ShoppingCart(customer_name, current_date)
    
    # Run the menu
    print_menu(cart)


if __name__ == "__main__":
    main()
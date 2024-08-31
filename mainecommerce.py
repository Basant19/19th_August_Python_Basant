from ecommerce.product.productmaintain import Product, add_product
from ecommerce.orders.orderprocess import Order, create_order
from ecommerce.product.inventory import Inventory


product_list = []
order_list = []
inventory = Inventory()

def mainmenu():
    while True:
        print("\nMain Menu:")
        print("1. Add a Product")
        print("2. Check Inventory")
        print("3. Add Stock")
        print("4. Reduce Stock")
        print("5. Create an Order")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_product_menu()
        elif choice == '2':
            check_inventory_menu()
        elif choice == '3':
            add_stock_menu()
        elif choice == '4':
            reduce_stock_menu()
        elif choice == '5':
            create_order_menu()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_product_menu():
    print("\nAdd a Product:")
    product_id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Product Stock: "))
    
    product = Product(product_id, name, price, stock)
    add_product(product_list, product)
    inventory.add_stock(product.product_id, product.stock)
    print(f"Product '{name}' added successfully!")

def check_inventory_menu():
    print("\nCheck Inventory:")
    product_id = int(input("Enter Product ID to check: "))
    stock = inventory.check_stock(product_id)
    if stock >= 0:
        print(f"Stock for Product ID {product_id}: {stock} units")

def add_stock_menu():
    print("\nAdd Stock:")
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity to Add: "))
    inventory.add_stock(product_id, quantity)

def reduce_stock_menu():
    print("\nReduce Stock:")
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity to Reduce: "))
    inventory.reduce_stock(product_id, quantity)

def create_order_menu():
    print("\nCreate an Order:")
    order_id = int(input("Enter Order ID: "))
    customer_name = input("Enter Customer Name: ")

    ordered_products = []
    while True:
        product_id = int(input("Enter Product ID to add to the order (or 0 to stop): "))
        if product_id == 0:
            break
        product = next((p for p in product_list if p.product_id == product_id), None)
        if product and inventory.is_in_stock(product_id, 1):
            ordered_products.append(product)
            inventory.reduce_stock(product_id, 1)
        else:
            print(f"Product ID {product_id} not found or out of stock.")

    if ordered_products:
        order = Order(order_id, customer_name, ordered_products)
        create_order(order_list, order)
        print(f"Order ID {order_id} created successfully!")
    else:
        print("No products added to the order.")

mainmenu()

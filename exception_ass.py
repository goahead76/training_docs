products = [
    {"id":101,"name":"Laptop","price":75000.0,"stock":5},
    {"id":102,"name":"SmartPhone","price":45000.0,"stock":10},
    {"id":103,"name":"Headphones","price":3000.0,"stock":20},
    {"id":104,"name":"Keyboard","price":2000.0,"stock":15},
]
cart = {}
class InsufficientStockError(Exception):
    pass
class ProductNotFoundError(Exception):
    pass
# Assignment 1

def find_product(products,product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    raise ProductNotFoundError(f"Product not Found")

# Assignment 2
def validate_quantity(quantity):
    try:
        if quantity <= 0:
            raise ValueError(f"Quantity must be Greater than Zero")
    except ValueError as error:
        print("Invalid Quantity !!",error)           

# Assignment 3,4
def add_to_cart(product,quantity):
    validate_quantity(quantity)
    if quantity > product["stock"]:
        raise InsufficientStockError("Insufficient Stock")
    product_id = product["id"]
    if product_id in cart:
        cart[product_id]["quantity"] += quantity
    else:
        cart[product_id] = {
            "name":product["name"],
            "price":product["price"],
            "quantity":quantity
        }
    product["stock"] -= quantity

# Assignment 5
def get_quantity():
    try:
        quantity = int(input("Enter Quantity:"))
        return quantity
    except ValueError:
        print("Please Enter Valid Whole Number")
        return None

def shopping():
    try:
        product_id = int(input("Enter Product ID:"))
        product = find_product(products,product_id)
        quantity = get_quantity()
        if quantity is None :
            return
        add_to_cart(product,quantity)
    except ProductNotFoundError as e:
        print("Product Error:",e)
    except ValueError as e:
        print("Quantity error:",e)
    except InsufficientStockError as e:
        print("Stock error:",e)
    except (TypeError,KeyError) as e:
        print("Invalid Product Information")
    except Exception as e:
        print("Something wnet wrong . Please try again.")
    else:
        print("Product added to cart successfully")
    finally:
        print("Add - to-cart operation finished")
    
def view_cart():
    if not cart:
        print("Cart is Empty")
        return
    
    total = 0
    
    for product_id , item in cart.items():
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(
            product_id,
            item["name"],
            "Quantity:",item["quantity"],
            "Subtotal:",subtotal
        )
    print("Total:",total)
    
def checkout():
    if not cart:
        print("Cart is Empty")
        return
    total = sum(item["price"]*item["quantity"] for item in cart.values())
    print("Checkout Total:",total)
    
    cart.clear()
    print("Checkout Completed Successfully")
    
def read_inventort(filename):
    file = None
    try:
        file = open(filename,"r")
        inventory = []
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                raise ValueError()
            product_id, name, price, stock = parts

            inventory.append({
                "id": int(product_id),
                "name": name,
                "price": float(price),
                "stock": int(stock)
            })

        return inventory

    except FileNotFoundError:
        print("Inventory file is missing.")

    except ValueError:
        print("Inventory file contains invalid data.")

    finally:
        # Q20, Q35: File closes even if an exception occurs
        if file is not None:
            file.close()
            print("Inventory file closed.")


# Main menu
while True:

    print("\n========== SHOPPING CART ==========")
    print("1. Add product")
    print("2. View cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        shopping()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        checkout()

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")

    
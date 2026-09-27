product_price  = 2500
product_quantity = 4
discount = 10
stock  = 20
order_total = 5500
premium_customer = True
payment_ok = True
coupon = None

# ASSIGNMENT 1 : ARITHMETIC OPERATORS
print("\n1.ARIHMETIC OPERATORS")
print("\n1.1 Calculate Subtoral , Discounted Price and Final Amount")
subtotal = product_price * product_quantity
discount_amt = subtotal * discount // 100
final_amt = subtotal - discount_amt
print("Final Amount:",final_amt)

print("\n1.2 Calculate normal division , complete box and remaining products")
product_quantity = 17
box_capacity = 5
print("Normal division result :",product_quantity/box_capacity)
print("Complete Boxes :",product_quantity//box_capacity)
print("Remaining Products :",product_quantity%box_capacity)

# ASSIGNMENT 2 : COMPARISON OPERATORS
print("\n2.COMPARISON OPERATORS")
print("\n2.1 Check Stock")
if stock > 0 :
    print("Available Stock : ",stock)
else:
    print("No Available Stock please try again after some time")

print("\n2.2 Check requested quantity is < or = to available stock")
requested_stock = 2
available_stock = 10
if requested_stock <= available_stock:
    print("Proceed for Purchase")
else:
    print("Sorry !! Not Available Stock Please try again after some time !!")

print("\n2.3 check whether order qualifies for discount when order total is at least $5000")
cart_total = 2600
if cart_total >= 5000:
    print("Discount is Applied")
else:
    print("No Discount Applied")

print("\n2.4 compare customer rating with 4.5 and display the boolean result")
customer_rating = 3.0
if customer_rating == 4.5:
    result = True
else:
    result=False
print(result)

print("\n2.5 Use == and != for order and payment_status")
if payment_ok == True:
    print("Payment Successfully Done!!")
    order_status = True
else:
    print("Payment is Pending !!")
    order_status = False
print("Payment Status :",payment_ok)
if order_status != True:
    print("Order has not placed")
else:
    print("Order has been Placed Successfully !!")
print("Order Status :",order_status)

# ASSIGNMENT 3 : ASSIGNMENT OPERATORS
print("\n3.ASSIGNMENT OPERATORS")
print("\n3.1 Calculate Available Quantity Acoording to customer Purchase")
purchased_quantity = 3
available_quantity = 20
available_quantity -= purchased_quantity
print("Available Quantity:",available_quantity)

print("\n3.2 Calculate Available quantity After Receiving 15 units")
received_quantity = 15
available_quantity += received_quantity
print("Now Available Quantity:",available_quantity)

print("\n3.3 Increment cart count using +=")
cart = 0
cart_product = ["Laptop","Mouse","Keyboard"]
for items in cart_product:
    cart += 1
print("Product in cart :",cart_product)
print("Total Items in Cart :",cart)

print("\n3.4 Use -=,/=,//= and %= ")
#Customer buy 10 product
available_quantity -= 10
print("Available Quantity:",available_quantity)
# Apply 10 % discount
print("Original product price:",product_price)
product_price -= (product_price*10//100)
print("Applied 10% discount:",product_price)
#Divide total amount among 3 customer
product_price /= 3
print("After Dividing total amount among 3 customers per customer amount will be:",product_price)
# Number of completed boxes
items = 25
items // 5
print("Completed Boxes:",items)
# Number of Remaining Boxes
items = 25
items %= 5
print("Remaining Products:",items)

print("\n3.5 Multiple Assignment")
product_id , product_name , price = 101 , "Laptop" , 12000.0
print("Product ID:",product_id,"Product Name:",product_name,"Product Price:",price)

# ASSIGNMENT 4 : LOGICAL OPERATOR
print("\n4.1 Check availabillity of stock and payment and is_active status for checkout")
is_active = True
is_available = True
if is_available and payment_ok and is_active:
    print("Proceed for Checkout")
else:
    print("Sorry Please Try Againn !!")
    
print("\n4.2 Give Free Shipment if order price is atleast $5000 or customer is premium")
print("Cart Total Amount::",cart_total)
if cart_total >= 5000 or premium_customer:
    print("Congratulations You got Free Shippment")
else :
    print("₹50 delivery Charges")

print("\n4.3 Use not to allow a user to continue when sccount is not blocked")
is_blocked = False
if not is_blocked:
    print("Proceed for Signup")
else:
    print("Sorry You are blocked !")
    
print("\n4.4 Make a Ecommerc rule using and or not")
is_logged = True
is_active = True
payment_ok = True
premium_customer = False
if is_logged and is_active:
    print("Customer Sucessfully Logined and is Active")
    if cart_total > 5000 or premium_customer:
        print("Free Shipment")
        if not payment_ok:
            print("Payment Done Successfully Order Placed")
        else:
            print("Payment not done !!")
    else:
        print("No Free Shippment ")
else:
    print("User is not Logined and not active")

# ASSIGNMENT 5 : MEMBERSHIP OPERATOR
print("\n5.1 use in operator to check electronics in category")
categories = ["Electronics","Computers"]
print(categories)
if "Electronics" in categories:
    print("Element Found")
else:
    print("Element Not found")

print("\n5.2 Check Whether Furniture is not Present in Categories using not in")
if "Furniture" not in categories:
    print("Not Present in Categories")
else:
    print("Present in Categories")

print("\n5.3 create a set pf product tags and check whether premium exists")
product_tags = {'Business',"Normal","Premium"}
if 'Premium' in product_tags:
    print("Premium User")

print("\n5.4 create a dictionary for a product and demonstrate that in checks dictionary keys")
products = {
    'Laptop' : 500000,
    'Mouse' : 2000,
    'Keyboard':2500
}
product = input("Enter product name:")
if product in products:
    print("Product Name:",product,"Price:",products[product])
else:
    print("Product not Available !!")

# ASSIGNMENT 6 : IDENTITY OPERATORS
print("\n6.1 create discount_code = None and check it using is none")
discount_code = None
print("Discount code:",discount_code)
if discount_code is None:
    print("No Discount on this purchase")
else:
    print("Discount Applied")

print("\n6.2 create two separate list with same values compare them using == and is")
product_list_1 = ["Clothes","Electronics","Kids","Stationary"]
product_list_2 = ["Clothes","Electronics","Kids","Stationary"]
print(product_list_1,"\n",product_list_2)
print("Using == :")
if product_list_1 == product_list_2:
    print("Yes !! Both are having same values")
print("Using is :")
if product_list_1 is product_list_2:
    print("Refered to same Object")
else:
    print("Not Refered to same Object")
    
print("\n6.3 Create a list conatining none value and then remove the none value using not in")
emp_id = [101,102,None,203]
clean_id =[]
for emp in emp_id:
    if emp is not None:
        clean_id.append(emp)
print(clean_id)

# Walrus Operator
print("\n6.4 Accept a customer name and check whether the input is not empty")
if customer_name := input("Enter Your name :"):
    print("Customer Name::",customer_name)
else:
    print("Please enter name !!")
    
print("""\n6.5 create a cart list and use := with len() to display the no of cart items
when the count is greater then zero""")
cart = ["Electronics","CellPhone","Headphone","Laptop"]
if cart_size := len(cart)>0:
    print("Cart Items:",cart)
else:
    print("No items Found !!")
    
# Without Walrus Operator
# user_input = input("Enter your Name::")
# if user_input:
#     print("Valid !!")

# With Walrus Operator
# if user_input := input("Enter Your Name::"):
#     print("Valid !!")
    
# ASSIGNMENT 7 : INTEGRATED E-COMMERCE ORDER CALCULATOR
print("\n7.INTEGRATED E-COMMERCE ORDER CALCULATOR")
product_price = 15000.0
product_quantity = 5
discount = 10
subtotal = product_quantity * product_price
discount_amt = subtotal * discount // 100
cart_total = subtotal - discount_amt
print("Product Price:",product_price)
print("Product Quantity:",product_quantity)
print("Product discount:",discount)
print("SubTotal :",subtotal)
print("Discount amount :",discount_amt)
print("Cart Total :",cart_total)
stock = 10
customer_role = "premium"
print("Stock:",stock)
if product_quantity > stock:
    print("Sorry Not available please try again")
else:
    print("Product is Avaialable")
if cart_total > 5000 or customer_role == 'premium':
    print("Free Shippment")
else:
    print("Shipping Charges Applied : ₹50")
is_payment = True
if is_payment:
    print("Payment Done Succesfully !!")
    stock -= product_quantity
else:
    print("Please Pay the Amount")
coupon = None
if coupon is None:
    print("No Coupen Applied")
else:
    print("Coupon is Applied:",coupon)
categories = ["Electronics","Computers"]
user_category = "Electronics"
if user_category in categories:
    print("Available !!")
else:
    print("Not Available")


"""
******************OUTPUT *****************

1.ARIHMETIC OPERATORS

1.1 Calculate Subtoral , Discounted Price and Final Amount
Final Amount: 9000

1.2 Calculate normal division , complete box and remaining products
Normal division result : 3.4
Complete Boxes : 3
Remaining Products : 2

2.COMPARISON OPERATORS

2.1 Check Stock
Available Stock :  20

2.2 Check requested quantity is < or = to available stock
Proceed for Purchase

2.3 check whether order qualifies for discount when order total is at least $5000
No Discount Applied

2.4 compare customer rating with 4.5 and display the boolean result
False

2.5 Use == and != for order and payment_status
Payment Successfully Done!!
Payment Status : True
Order has been Placed Successfully !!
Order Status : True

3.ASSIGNMENT OPERATORS

3.1 Calculate Available Quantity Acoording to customer Purchase
Available Quantity: 17

3.2 Calculate Available quantity After Receiving 15 units
Now Available Quantity: 32

3.3 Increment cart count using +=
Product in cart : ['Laptop', 'Mouse', 'Keyboard']
Total Items in Cart : 3

3.4 Use -=,/=,//= and %= 
Available Quantity: 22
Original product price: 2500
Applied 10% discount: 2250
After Dividing total amount among 3 customers per customer amount will be: 750.0
Completed Boxes: 25
Remaining Products: 0

3.5 Multiple Assignment
Product ID: 101 Product Name: Laptop Product Price: 12000.0

4.1 Check availabillity of stock and payment and is_active status for checkout
Proceed for Checkout

4.2 Give Free Shipment if order price is atleast $5000 or customer is premium
Cart Total Amount:: 2600
Congratulations You got Free Shippment

4.3 Use not to allow a user to continue when sccount is not blocked
Proceed for Signup

4.4 Make a Ecommerc rule using and or not
Customer Sucessfully Logined and is Active
No Free Shippment 

5.1 use in operator to check electronics in category
['Electronics', 'Computers']
Element Found

5.2 Check Whether Furniture is not Present in Categories using not in
Not Present in Categories

5.3 create a set pf product tags and check whether premium exists
Premium User

5.4 create a dictionary for a product and demonstrate that in checks dictionary keys
Enter product name:Laptop
Product Name: Laptop Price: 500000

6.1 create discount_code = None and check it using is none
Discount code: None
No Discount on this purchase

6.2 create two separate list with same values compare them using == and is
['Clothes', 'Electronics', 'Kids', 'Stationary'] 
 ['Clothes', 'Electronics', 'Kids', 'Stationary']
Using == :
Yes !! Both are having same values
Using is :
Not Refered to same Object

6.3 Create a list conatining none value and then remove the none value using not in
[101, 102, 203]

6.4 Accept a customer name and check whether the input is not empty
Enter Your name :Anjali
Customer Name:: Anjali

6.5 create a cart list and use := with len() to display the no of cart items
when the count is greater then zero
Cart Items: ['Electronics', 'CellPhone', 'Headphone', 'Laptop']

7.INTEGRATED E-COMMERCE ORDER CALCULATOR
Product Price: 15000.0
Product Quantity: 5
Product discount: 10
SubTotal : 75000.0
Discount amount : 7500.0
Cart Total : 67500.0
Stock: 10
Product is Avaialable
Free Shippment
Payment Done Succesfully !!
"""
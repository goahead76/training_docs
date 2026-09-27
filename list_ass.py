# Assignment 1
print("\n Assignment 1")

cart = ["Laptop","Wireless-mouse","Keyboard","Monitor"]
prices =[75000,1200,2500,18000]
print("\nCreate Chechout copy of cart")
checkout_copy = cart.copy()
print("CheckOut Copy:",checkout_copy)
print("\nAppend Webcam")
cart.append("Webcam")
print("\nInsert Laptop Bag next to Laptop")
cart.insert(1,"Laptop Bag")
print("\nReplace keyboard with mechanical keyboard")
cart[3] = "Mechanical Keyboard"
print("\nRemove wireless Mouse")
cart.remove("Wireless-mouse")
print("Cart Items:",cart)
print("\nDisplay 1st Element")
print("First Element:",cart[0])
print("\nLast Element")
print("Last Element:",cart[-1])
print("\nSecond and Third Element")
print("Second and Third Element:",cart[1:3])
print("\nCheck Monitor Exists")
if "Monitor" in cart:
    print("Monitor Product Exists")
cart.append("Laptop")
print("\nCount of Laptop")
print("Count of Laptop:",cart.count("Laptop"))
print("\nSorting of Prices")
prices.sort()
print("\nSorted Prices:",prices)
new_price = [price for price in prices if price > 10000]
print("\nPrice above 10000:",new_price)
print("\nDisplay products in cart")
print("Products in Cart:")
for product in cart:
    print(product)
removed_value = cart.pop(0)
print("\nRemoved Value from pos 0",removed_value)
if "Monitor" in cart:
    cart.remove("Monitor")
    print("\nSuccesfully removed Monitor")
else:
    print("\nProduct not exist")
    
print(cart)

# Assignment 2
print("\nAssignment 3")
products = [
    {"name":"Laptop","price":75000},
    {"name":"Mouse","price":1200},
    {"name":"Monitor","price":18000},
    {"name":"Keyboard","price":2500}
]
ascending_product = products.copy()
ascending_product.sort(key = lambda p :p["price"])
for product in ascending_product:
    print(product["name"],product["price"])
descending_product = products.copy()
descending_product.sort(key=lambda p:p["price"] , reverse = True)
print("\nProduct in Descending Order:")
for product in descending_product:
    print(product["name"],product["price"])
print("\nExpensive Product:",descending_product[0])
print("\nCheapest Product:",ascending_product[0])

# Assignment 3
prices = [999,4500,1200,75000,2500,12000]
discounted = [price * 0.90 for price in prices]
print(discounted)
final_price = [price * 1.18 for price in discounted]
print(final_price)
filter_price = [price for price in final_price if price >= 10000]
print("price greter than 10000₹",filter_price)

# Assignment 4
order_items = [
    ("Laptop",1,75000),
    ("WIireles Mouse",2,1200),
    ("keyboard",1,2500)
]
item1,item2,item3 = order_items
print(item1)
print(item2)
print(item3)

for name,qty,price in order_items:
    subtotal = qty * price
    print("Subtotal :",subtotal,"of ",name,"Quantity:",qty)

total = 0
for name,qty,price in order_items:
    total += (price*qty)
print("Total :",total)

for name,qty,price in order_items:
    if qty > 1:
        print(name,":",qty)

# Assignment 5
dimensions = (40,20,10)
length,width,height = dimensions
print("height:",height)
print("breadth:",length)
print("width:",width)
volume = length * width*height
print("Volume:",volume)
# dimensions[0]=40
# TypeError: 'tuple' object does not support item assignment

# Assignment 6
status_log = ("placed","packed","shipped","delivered")
print("Count Shipped events:",len(status_log))
print("Frist Delivered Position:",status_log[0])
print("Last Delivered Position:",status_log[-1])
print("Stages before delivery:",status_log[0:3])

# Assignment 7
cart =["Laptop","Mouse","Keyboard","Monitor"]
cart_copy = cart.copy()
cart_copy.append("CPU")
print("Cart Items:",cart_copy)
print("Sorted Cart:",cart_copy.sort())
print("Filter the copy:",cart_copy[2:3])
print("Original Cart:",cart)
print("Copied Cart:",cart_copy)

# Assignment 8 
recommendation = [
    ["Laptop","Monitor","Keyboard"],
    ["Phone","Earbuds"],
    ["Camera","Tripod","Memory Card"]
]
print("Specific Product:",recommendation[0][2])

# Iterate through all groups
for product in recommendation:
    for product_name in product:
        print(product_name)
        
flattened_product = [
    product
    for group in recommendation
    for product in group
]
print("\nFlattened products:",flattened_product)

empty_group = [
    index for index,group in enumerate(recommendation) if not group      
]
print("Empty Group:",empty_group)

valid_group = [
    group for group in recommendation if len(group) >=2
]
print("Valid Groups:",valid_group)

# Assignment 9
# def check_summary(order_items):
#     if not order_items:
#         return 0,0.0,"REJECTED"
#     total_quantity = 0
#     total_amount = 0.0
#     for product_name , unit_price , quantity in order_items:
 

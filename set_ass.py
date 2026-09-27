# from ordered_set import OrderedSet

# prevent dupliacte tags : so use set 
tags = {"electronics","bestseller","discounted"}
tags.add("furniture")
tags.update(("fashion",'games'))
print("Tags:",tags)
# if we have used remove it will show error so thats why use discard
# tags.remove("books")
# File "C:\Users\anjali.pacharne\Desktop\Training\python\Day_4_ass.py", line 29, in <module>
#   tags.remove("books")
#   ~~~~~~~~~~~^^^^^^^^^
#KeyError: 'books'

tags.discard("books")
print("books removed",tags)

# customer who has item in cart but not purchased it
customer_with_cart = {101,102,103,104,105}
customer_who_ordered = {102,104}
abandoned_cart_customer = customer_with_cart - customer_who_ordered
print(abandoned_cart_customer)

# customer who purchased mobile or laptop
# customer who have unsubscribed is excluded
# customer who purchased both product should receive notification
mobile_customer = {101,102,103}
laptop_customer= {102,103,104,105}
unsubscribed_customer = {101,102}
print("Mobile Customer:",mobile_customer)
print("Laptop Customer:",laptop_customer)
print("Unsubscribed Customer:",unsubscribed_customer)
purchased_both = mobile_customer.intersection(laptop_customer)
print("Purchased Both:",purchased_both)
customer_group = mobile_customer.union(laptop_customer)
print("Customer Group:",customer_group)
subscribed_customer = customer_group.difference(unsubscribed_customer)
print("Subscribed Customer:",subscribed_customer)

# 1. Check whether all ordered product are packed
ordered_product = {"P101","P102","P103","P104"}
packed_product = {"P101","P102","P105"}
if ordered_product.issubset(packed_product):
    print("Product is ready to dispatch !!")
else:
    print("Order is Incomplete")

# 2. Find Missing Products
missing_product =  ordered_product.difference(packed_product)
print("Missing Products:",missing_product)

# 3. Find product that is packed by mistake
mistake_packed = packed_product.difference(ordered_product)
print("Mistakely Pakced :",mistake_packed)

# 4. find every mismatch non common values
mismatched_product = ordered_product.symmetric_difference(packed_product)
print("Mismacthed product:",mismatched_product)

# Assignment 1 
customer_categories = ["Electronics","Fashion","Electronics","Home Appliances","Fashion","Books","Electronics"]
categories_set = set(customer_categories)
print("Customer Categories:",categories_set)
if "Electronics" in categories_set:
    print("Product Exist")
else:
    print("Not exist")
categories_set.add("Gaming")
print("Added Gaming:",categories_set)
categories_set.update({"Mobile","Accessories"})
print("Added Mobile and Accessories:",categories_set)
categories_set.discard("Travel")
print("Safely remove travel")
print("Count of Unique Categories:",len(categories_set))

# Assignment 2 
api_products = ["P101","P102","P103","P101"]
csv_products = ["P102","P104","P105"]
db_products = ["P101","P105","P106"]
api_product = set(api_products)
csv_product = set(csv_products)
db_product = set(db_products)
print("API Products:",api_product)
print("CSV Product:",csv_product)
print("DB Product:",db_product)
print("Common in API and DB",api_product.intersection(db_product))
print("ID in API but not in DB",api_product.difference(db_product))
all_product = api_product.union(csv_product,db_product)
print("All Products:",all_product)
api_csv = api_product.intersection(csv_product)
csv_db = csv_product.intersection(db_product)
db_api = db_product.intersection(api_product)
shared_product = api_csv.union(csv_db,db_api)
print("Shared Product:",shared_product)
exclusive = all_product-shared_product
print("IDs exclusive either source",exclusive)
print("Unqiue Count :",len(all_product))

# Assignment 3
print("\n")
customer_a = {"Laptop","Mobile","Headphones","Keyboard"}
customer_b = {"Mobile","Headphones","Camera","Smart Watch"}
print("Customer A:",customer_a)
print("Customer B:",customer_b)
print("Common Products:",customer_a.intersection(customer_b))
print("All Unique Product:",customer_a.union(customer_b))
print("Product Customer A Purchased:",customer_a.difference(customer_b))
print("Product Customer B Purchased:",customer_b.difference(customer_a))

# Assignment 4
admin_permissions = {"view_product","add_product","update_product","delete_product"}
manager_permissions = {"view_product","add_product","update_product"}
report_permissions = {"view_reports","export_reports"}
grouped_premissions = admin_permissions.union(manager_permissions,report_permissions)
print("All Permissions:",grouped_premissions)
if "update_product" in grouped_premissions:
    print("Found !!")
print(manager_permissions.issubset(admin_permissions)) 
print(admin_permissions.issuperset(manager_permissions)) 
print(report_permissions.isdisjoint(admin_permissions.union(manager_permissions)))
manager_permissions.add("display_product")
print(manager_permissions.issubset(admin_permissions))

# Assignment 5
cart_skus = {"SKU101","SKU102","SKU103","SKU104"}
available_skus = {"SKU101","SKU103","SKU105","SKU106"}
skus = cart_skus.union(available_skus)
print("Fulfilled SKUs:",skus)
print("Inventory SKUs not in cart:",available_skus.difference(cart_skus))
print("cart SKUs that are unavailable:",cart_skus.difference(available_skus))
print("Whether every carrt SKU is available:",cart_skus.issubset(available_skus))

# Assignment 6
customer_restricted = {"Electronics","Books","Gaming"}
blocked_categories = {"Luxury","Wholesale","Restricted Goods"}
disjoint = customer_restricted.isdisjoint(blocked_categories)
print("check whether two sets are disjoint :",disjoint)
if not customer_restricted.isdisjoint(blocked_categories):
    overlapping = customer_restricted.intersection(blocked_categories)
    print("Overlapping:",overlapping)

product_tags = {"new","featured","electronics","discount"}
product_tags.add("bestseller")
product_tags.update({"furniture","books"})
print(product_tags)
print(product_tags.remove("discount"))
#this throws error
# print(product_tags.remove("discount"))  
print(product_tags.discard("discount"))


products_ids = {"P101","P102","P103","P104"}
primary_product = list(products_ids)[0]
print(primary_product)

# An Ordered Set or Linked Hash Set is used when both element 
# uniqueness and insertion order matter.
# from ordered_set import OrderedSet
# res = OrderedSet(['a', 'b', 'c', 'b', 'd'])
# print(res)

# for item in res:
#     print(item, end=" ")

default_permission = frozenset({"view_product","view_order","view_customer"})
if "view_order" in default_permission:
    print("found!!")
    
# Assignment 10
customer_categories ={"Electronics","Fashion","Gaming","Books","Electronics"}
wishlist_product = ["P101","P102","P103","P101","P104"]
purchased_products = {"P101","P105","P106"}
allowed_categories = {"Electronics","Fashion","Books","Gaming","Sports"}
manager_permissions = {"view_product","add_product","update_product"}
required_permissions = {"view_product","update_product"}

wishlist_product = set(wishlist_product)
print(wishlist_product)
print("Wishlist product already Purchased:",wishlist_product.intersection(purchased_products))
unqiue_product_id = wishlist_product.union(purchased_products)
print("Unique product:",unqiue_product_id)
if customer_categories.issubset(allowed_categories):
    print("validated !!")
else:
    print(customer_categories.difference(allowed_categories))
print(required_permissions.issubset(manager_permissions))

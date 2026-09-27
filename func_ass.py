products = [
    {"id": 101, "name": "Laptop", "category": "Electronics", "price": 75000},
    {"id": 102, "name": "Smartphone", "category": "Electronics", "price": 45000},
    {"id": 103, "name": "Headphones", "category": "Accessories", "price": 3000},
    {"id": 104, "name": "Keyboard", "category": "Accessories", "price": 2000}
]
def find_product(products,product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    else:
        print("Product not found !!")
product = find_product(products,102)
print(product)

categories_product = {}
def search_product(products,keyword):
    if not keyword.isalpha():
        print("Please enter name of product or category")
    keyword = keyword.lower()
    keyword = keyword.capitalize()
    for product in products:
        if product["name"] == keyword :
            return product
        if product["category"] == keyword:
            categories_product.update(product)
            
    else:
        print("Product not found")

print(search_product(products,"ELECTRONICS"))
from services.product_service import ProductService

class ProductCLI:
    def __init__(self):
        self.service = ProductService()


    def product_menu(self):
        while True:
            print("\n----- Product Managemment -----")
            print("1. Add Product")
            print("2. View All Products")
            print("3. View Product by ID")
            print("4. View Product by Name")
            print("5. Update Product")
            print("6. Delete Product")
            print("0. Back")
            choice = input("Enter Choice: ").strip()
            
            try:
#---------------------------------------------------------------------------------------                
                if choice == "1":
                    name = input("Product name: ")
                    category = input("Category: ")
                    price = float(input("Price: "))

                    product_id = self.service.create_product(name , category , price)
                    print(f"Product added successfully (ID: {product_id})")

#---------------------------------------------------------------------------------------
                elif choice == "2":
                    products = self.service.list_products()

                    if not products:
                        print("No products found")
                        return
        
                    print("\nID | Name | Category | Price")
                    print("-" * 35)

                    for p in products:
                        print(f"{p.id} | {p.name} | {p.category} | {p.price}")

#---------------------------------------------------------------------------------------
                elif choice == "3":
                    product_id = int(input("Enter product ID:"))
                    product = self.service.list_product_by_id(product_id)

                    if not product:
                        print("Product not found")
                        return
            
                    print("\n Product Details")
                    print(f"ID       : {product['id']}")
                    print(f"Name     : {product['name']}")
                    print(f"Category : {product['category']}")
                    print(f"Price    : {product['price']}")

#---------------------------------------------------------------------------------------
                elif choice == "4":
                    name = input("Enter product name: ")
                    product = self.service.list_product_by_name(name)

                    if not product:
                        print("No product found")
                        return
            
                    print("\n Product Details")
                    print(f"ID       : {product['id']}")
                    print(f"Name     : {product['name']}")
                    print(f"Category : {product['category']}")
                    print(f"Price    : {product['price']}")

#---------------------------------------------------------------------------------------
                elif choice == "5":
                    product_id = int(input("Enter product ID: "))
                    name = input("New Name: ")
                    price = float(input("New Price: "))

                    self.service.change_product(product_id , name , price)
                    print("Product updated successfully.")

#---------------------------------------------------------------------------------------
                elif choice == "6":
                    product_id = int(input("Enter product ID: "))
                    self.service.remove_product(product_id)
                    print("Product removed successfully.")

#---------------------------------------------------------------------------------------
                elif choice == "0":
                    break
                else :
                    print("Invalid Choice")

            except ValueError as e:
                print(f"Error: {e}")

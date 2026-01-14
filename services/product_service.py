from models.product import Product
from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def create_product(self , name , category , price):

        #Validation
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        
        if not category or not category.strip():
            raise ValueError("Product catgory cannot be empty")
        
        if price <= 0:
            raise ValueError("Product price must be greater than zero")

        product = Product(
            id = None, 
            name = name.strip(), 
            category = category.strip(),
            price = price
            )
        return self.repo.add_product(product)

    def list_products(self):
        return self.repo.get_all_products()
    
    def list_product_by_id(self , product_id):

        if product_id <= 0:
            raise ValueError("Invalid product ID")
        
        return self.repo.get_product_by_id(product_id)
    
    def list_product_by_name(self , product_name):

        if not product_name or not product_name.strip():
            raise ValueError("Product name cannot be empty")
        
        return self.repo.get_product_by_name(product_name)

    def change_product(self , product_id , name , price):

        if product_id <= 0:
            raise ValueError("Invalid product ID")
        
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        
        if price <= 0:
            raise ValueError("Product price must be greater than zero")
        
        updated = self.repo.update_product(product_id , name.strip() , price)

        if not updated:
            raise ValueError("Product not found")
        
        return True

    def remove_product(self , product_id):

        if product_id <= 0:
            raise ValueError("Invalid Product ID")
        
        deleted = self.repo.delete_product(product_id)

        if not deleted:
            raise ValueError("Product not found")
        
        return True

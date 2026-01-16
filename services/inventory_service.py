from repositories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self, ):
        self.repo = InventoryRepository()

#----------------------------------------------------------

    def ensure_stock_exists(self , product_id: int):
        if not self.repo.get_by_product_id(product_id):
            self.repo.create_stock(product_id)

    def add_stock(self , product_id: int , amount: int):
        if amount <= 0:
            raise ValueError("Stock amount must be positive.")
        
        stock = self.repo.get_by_product_id(product_id)

        if not stock:
            raise ValueError("Stock record not found.")
        
        new_quantity = stock.quantity + amount
        
        self.repo.update_quantity(product_id , new_quantity)

#----------------------------------------------------------

    def remove_stock(self , product_id: int , amount: int):
        if amount <= 0:
            raise ValueError("Stock amount must be positive.")
        
        stock = self.repo.get_by_product_id(product_id)

        if not stock:
            raise ValueError("Stock record not found.")
        
        if stock.quantity < amount:
            raise ValueError("Insufficient Stock.")
        
        new_quantity = stock.quantity - amount

        self.repo.update_quantity(product_id , new_quantity)

#----------------------------------------------------------

    def get_stock(self, product_id: int):
        return self.repo.get_by_product_id(product_id)

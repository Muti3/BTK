from Product import Product
class ProductHelper:
    @staticmethod
    def create_item_from_text(file_path):
        product_list = []
        with open(file_path, 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                product = Product(name.strip(), float(price.strip()), int(quantity.strip()))
                product_list.append(product)
        return product_list

    @staticmethod
    def get_total_balance(product_list):
        total_balance = sum(product.get_total_price() for product in product_list)
        total_balance_with_tax = total_balance * 1.20  
        return total_balance_with_tax
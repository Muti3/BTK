from ProductHelper import ProductHelper
if __name__ == "__main__":
    
    products = ProductHelper.create_item_from_text('Products.txt')
    

    total_balance = ProductHelper.get_total_balance(products)
    
    print(f"Toplam bakiye (KDV dahil): {total_balance:.2f}")
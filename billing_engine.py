# Group Activity: Billing Engine - Simba Supermarket, Kigali City
 
class ScannedItem:
    def __init__(self, item_name, price, quantity, category):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.category = category
 
    def get_item_details(self):
        subtotal = self.price * self.quantity
        return f"""[BEEP!] {self.item_name:<15} | {self.quantity} x {self.price} RWF | Category: {self.category:<10} | Subtotal: {subtotal} RWF"""



simba_cart = [
    ScannedItem("Winnaz Chips", 1000, 2, "Snacks"),
    ScannedItem("Fanta", 1200, 1, "Drinks"),
    ScannedItem("Energy", 600, 4, "Drinks"),
    ScannedItem("Omo", 7500, 1, "Detergent"),
]

grand_total = 0 

for item in simba_cart:
    print(item.get_item_details())
    subtotal = item.price * item.quantity
    
    if item.category == "Detergent":
        discount = subtotal * 0.05 
        subtotal = discount - subtotal
        print(f"        >>> PROMO! 5% off {item.item_name}: -{discount} RWF")
 
    grand_total = grand_total + subtotal
 
print("-" * 60)
print(f"GRAND TOTAL: {grand_total} RWF")
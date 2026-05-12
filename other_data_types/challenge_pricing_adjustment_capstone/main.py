# Task 1: Define a dictionary for grocery inventory
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}

# Task 2: Check Eggs price and reduce if needed
eggs_cat, eggs_price, eggs_stock = grocery_inventory["Eggs"]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (eggs_cat, eggs_price - 1, eggs_stock)
else:
    print("The price of Eggs is reasonable.")

# Task 3: Add Tomatoes
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

# Task 4: Manage Milk stock
milk_cat, milk_price, milk_stock = grocery_inventory["Milk"]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (milk_cat, milk_price, milk_stock + 20)
else:
    print("Milk has sufficient stock.")

# Task 5: Remove Apples if price > 2
apples_cat, apples_price, apples_stock = grocery_inventory["Apples"]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

# Final print
print("Updated inventory:", grocery_inventory)
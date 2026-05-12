grocery_items = "milk cheese bread apples oranges chicken"

# Correct slicing indices
dairy1 = grocery_items[0:4]    # 'milk'
dairy2 = grocery_items[5:11]   # 'cheese'
bakery1 = grocery_items[12:17] # 'bread'

# Combine with concatenation and print exact message
print("We have dairy and bakery items: " + dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5")
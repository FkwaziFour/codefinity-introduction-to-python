# Task: Create a function to apply a 10% discount to prices over $2.00
def apply_discount(prices):
    # Create a copy of the `prices` list
    prices_copy = prices.copy()
    
    # Iterate through the list using indexing
    for index in range(len(prices_copy)):
        # Apply a 10% discount if the price is greater than $2.00
        if prices_copy[index] > 2.00:
            prices_copy[index] *= 0.90  # Applying a 10% discount
    
    # Return the updated list of prices
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

# Print the updated prices
print(f"Updated product prices: {updated_prices}")
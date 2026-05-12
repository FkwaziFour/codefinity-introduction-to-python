# Task 1: Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

# Task 2: Define a function to format and display the sorted revenues
def formatted_output(revenues):
    for product, rev in sorted(revenues):
        print(f"{product} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# Task 3: Calculate revenues
revenue = calculate_revenue(prices, quantities_sold)

# Task 4: Combine products with their revenues
revenue_per_product = list(zip(products, revenue))

# Task 5: Print formatted, sorted output
formatted_output(revenue_per_product)
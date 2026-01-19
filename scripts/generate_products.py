import random
import pandas as pd
from faker import Faker

fake = Faker()

ELECTRONICS = [
    "Apple iPhone 14", "Apple iPhone 14 Pro", "Samzung Galaxy S21",
    "Samsung Galaxy S21", "OnePlus 11", "Sony Headphones",
    "Dell Inspiron Laptop", "HP Pavilion Laptop"
]

FASHION = [
    "Nike Running Shoes", "Adidas Sneakers", "Levis Denim Jeans",
    "Puma Sports T-Shirt", "Zara Casual Shirt"
]

GROCERIES = [
    "Organic Almonds", "Basmati Rice 5kg", "Whole Wheat Bread",
    "Fresh Cow Milk", "Brown Eggs Pack"
]

def generate_products(n=500):
    products = []
    for i in range(1, n + 1):
        category = random.choice([ELECTRONICS, FASHION, GROCERIES])
        name = random.choice(category)

        # Add slight variations / typos
        if random.random() < 0.1:
            name = name.replace("Samsung", "Samzung")

        products.append({
            "product_id": i,
            "product_name": name
        })
    return products

if __name__ == "__main__":
    data = generate_products()
    df = pd.DataFrame(data)
    df.to_csv("data/products.csv", index=False)
    print("✅ products.csv generated with 500 records")

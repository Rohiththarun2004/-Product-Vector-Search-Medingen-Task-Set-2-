import json
import pandas as pd
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer

# MySQL Config
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "products_db"
}

# Load CSV
df = pd.read_csv("data/products.csv")

# Generate TF-IDF embeddings
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df["product_name"]).toarray()

# Connect DB
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

for i, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO products_vectors (product_id, product_name, vector)
        VALUES (%s, %s, %s)
        """,
        (int(row["product_id"]), row["product_name"], json.dumps(vectors[i].tolist()))
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Embeddings stored in MySQL")

import json
import numpy as np
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DB_CONFIG = {
    "host": "YOUR_RDS_ENDPOINT",
    "user": "admin",
    "password": "password",
    "database": "products_db"
}

def lambda_handler(event, context):
    query = event.get("query", "")

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT product_id, product_name, vector FROM products_vectors")
    rows = cursor.fetchall()

    product_names = [r["product_name"] for r in rows]
    vectors = np.array([json.loads(r["vector"]) for r in rows])

    vectorizer = TfidfVectorizer()
    vectorizer.fit(product_names)
    query_vector = vectorizer.transform([query]).toarray()

    similarities = cosine_similarity(query_vector, vectors)[0]
    top_indices = similarities.argsort()[-5:][::-1]

    results = []
    for i in top_indices:
        results.append({
            "product_id": rows[i]["product_id"],
            "product_name": rows[i]["product_name"],
            "score": float(similarities[i])
        })

    cursor.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }

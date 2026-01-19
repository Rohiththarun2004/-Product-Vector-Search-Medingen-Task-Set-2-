# Product Vector Search (Medingen Task Set 2)

## Overview
This project implements vector-based product search using Python, MySQL, and AWS Lambda.

## Vector Logic
- TF-IDF embeddings are generated from product names
- Cosine similarity is used to find nearest products

## Steps (Local)
1. Install dependencies  
   `pip install -r requirements.txt`

2. Generate products  
   `python scripts/generate_products.py`

3. Create DB table  
   Run `sql/create_products_vectors.sql`

4. Generate embeddings  
   `python scripts/embed_products.py`

## AWS
- Upload CSV to S3
- Store vectors in RDS MySQL
- Deploy Lambda for semantic search

## Edge Cases
- Similar names (iPhone 14 vs iPhone 14 Pro)
- Typos (Samzung vs Samsung)

## Limitations
- TF-IDF is not semantic like BERT
- Lambda cold start latency

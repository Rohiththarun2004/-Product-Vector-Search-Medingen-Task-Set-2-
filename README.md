Product Vector Search System


 Overview
    This project implements a vector-based product search system using Python, MySQL, and AWS Lambda.
    It generates fake product data, converts product names into numerical vectors, stores them in a database, and allows similarity-based search using cosine         similarity.


The system is designed to handle:
   Similar product names
   Minor spelling mistakes (typos)
   Large product lists (500+ items)

Project Components:
   Data Generation (Python) – Generates 500 fake products
   Vector Generation (Python) – Creates embeddings and stores them in MySQL
   MySQL Database – Stores product vectors
   AWS Lambda – Performs similarity search


Instructions to Run Locally
 1️ Prerequisites:
     Python 3.8+
     MySQL Server
     pip

 2️ Install Dependencies:
     pip install -r requirements.txt

 3️ Generate Product Data:
     python scripts/generate_products.py
     This will generate:
        data/products.csv
        with 500 products, including similar names and typos.

 4️ Create MySQL Table:
     Login to MySQL and run:
         source sql/create_products_vectors.sql;

 5️ Generate Embeddings & Store in MySQL:
     python scripts/embed_products.py
     This will:
       Read products.csv
       Generate TF-IDF vectors
       Store them in the products_vectors table


Instructions to Run in AWS:
    1️ Upload CSV to S3
      Create an S3 bucket
      Upload products.csv

   2️ Create RDS MySQL
      Engine: MySQL
      Ensure Lambda has network access (VPC + Security Group)

   3️ Deploy Lambda Function
      Runtime: Python 3.9
      Handler: lambda_handler.lambda_handler
      Add MySQL credentials as environment variables

   4️ Invoke Lambda
        Example event:
        {
  "query": "Apple iPhone 14"
}


Response:

[
  {
    "product_id": 12,
    "product_name": "Apple iPhone 14 Pro",
    "score": 0.89
  }
]

 
 Vector Similarity Logic
    Embedding Method
    TF-IDF (Term Frequency – Inverse Document Frequency)
    Converts product names into numerical vectors based on word importance
    Similarity Metric
    Cosine Similarity
    Measures the angle between vectors (value between 0 and 1)
    Search Flow
    Convert query text into a vector
    Compare query vector with all stored product vectors
    Sort by similarity score
    Return top 5 most similar products


 Edge Case Handling
  Similar Product Names
   Example:
   Apple iPhone 14
   Apple iPhone 14 Pro
   Handled because TF-IDF captures shared keywords.

Typographical Errors

  Example:
   Samsung Galaxy S21
   Samzung Galaxy S21
   Handled because:
   Common tokens (Galaxy, S21) still match
   Cosine similarity remains high

Duplicate / Repeated Products
   Multiple similar entries are allowed
   Search returns the most relevant ones based on similarity score

Limitations / Assumptions
   TF-IDF is lexical, not semantic (unlike BERT)
   Assumes English product names
   Lambda memory limits may affect large datasets
   No real-time vector indexing (full scan used)


Conclusion
   This project demonstrates a complete vector search pipeline from data generation to cloud deployment, with realistic edge case handling and scalable design.

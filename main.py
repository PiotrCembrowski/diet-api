from fastapi import FastAPI
import sqlite3

app = FastAPI()

import db

DATABASE = 'database.db'

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/products")
def create_product():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES ('Apple', 1.0)")
    conn.commit()
    conn.close()
    
    return {"message": "Product has been created successfully!"}


# @app.get("/")
# def read_root():
#     users = cursor.fetchall()
#     conn.close()
#     return {"users": users}
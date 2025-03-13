from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/products")
def create_product():
    
    return {"message": "Product has been created successfully!"}
from fastapi import FastAPI
import sqlite3

app = FastAPI()

import db

DATABASE = 'database.db'

# classes
class Product:
    id: int
    name: str
    carbs: int
    protein: int
    alanine: int
    arginine: int
    aspartic_acid: int
    cystine: int
    glutamic_acid: int
    glycine: int
    histidine: int
    hydroxyproline: int
    isoleucine: int
    leucine: int
    lysine: int
    methionine: int
    phenylalanine: int
    proline: int
    serine: int
    threonine: int
    tryptophan: int
    tyrosine: int
    valine: int
    fat: int
    satureted_fat: int
    trans_fat: int
    mono_unsaturated_fat: int
    poly_unsaturated_fat: int
    omega3: int
    omega6: int
    omega9: int
    cholesterol: int
    phytosterol: int
    allulose: int
    fructose: int
    glucose: int
    lactose: int
    maltose: int
    sucrose: int
    galactose: int
    calories: int
    sugar: int
    fiber: int
    vitamin_a: int
    alpha_carotene: int
    beta_carotene: int
    beta_cryptoxanthin: int
    lycopene: int
    lutein_zeaxanthin: int
    retinol: int
    vitamin_b1: int
    vitamin_b2: int
    vitamin_b3: int
    vitamin_b5: int
    vitamin_b6: int
    vitamin_b12: int
    biotin: int
    choline: int
    folate: int
    vitamin_c: int
    vitamin_d: int
    vitamin_e: int
    beta_tocopherol: int
    gamma_tocopherol: int
    delta_tocopherol: int
    vitamin_k: int
    calcium: int
    chromium: int
    copper: int
    fluoride: int
    iodine: int
    iron: int
    magnesium: int
    manganese: int
    molybdenum: int
    phosphorus: int
    potassium: int
    selenium: int
    sodium: int
    zinc: int
    protein_quality: int
    fat_quality: int
    carb_quality: int

# ENDPOINTS
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/products")
async def create_product(product: Product):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (id, name, carbs, protein, alanine, arginine, aspartic_acid, cystine, glutamic_acid, glycine, histidine, hydroxyproline, isoleucine, leucine, lysine, methionine, phenylalanine, proline, serine, threonine, tryptophan, tyrosine, valine, fat, satureted_fat, trans_fat, mono_unsaturated_fat, poly_unsaturated_fat, omega3, omega6, omega9, cholesterol, phytosterol, allulose, fructose, glucose, lactose, maltose, sucrose, galactose, calories, sugar, fiber, vitamin_a, alpha_carotene, beta_carotene, beta_cryptoxanthin, lycopene, lutein_zeaxanthin, retinol, vitamin_b1, vitamin_b2, vitamin_b3, vitamin_b5, vitamin_b6, vitamin_b12, biotin, choline, folate, vitamin_c, vitamin_d, vitamin_e, beta_tocopherol, gamma_tocopherol, delta_tocopherol, vitamin_k, calcium, chromium, copper, fluoride, iodine, iron, magnesium, manganese, molybdenum, phosphorus, potassium, selenium, sodium, zinc, protein_quality, fat_quality, carb_quality) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?")
    conn.commit()
    conn.close()
    
    return {"message": "Product has been created successfully!"}


@app.get("/products")
def read_products():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return {"products": products}
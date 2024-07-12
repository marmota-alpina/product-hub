import uuid

import requests

from flask_sqlalchemy import SQLAlchemy
from models import Product  # Assumindo que você tenha um modelo Product definido


class FakeStoreService:
    FAKE_STORE_API_URL = "https://fakestoreapi.com"

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def load_products(self):
        try:
            response = requests.get(self.FAKE_STORE_API_URL + "/products")
            response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
            products_data = response.json()
            products_from_db = self.db.session.query(Product).filter_by(source='fake_store').all()

            for product_data in products_data:
                product = next((p for p in products_from_db if p.source_id == product_data['id']), None)
                if not product:
                    product = Product(
                        id=str(uuid.uuid4()),
                        source_id=product_data['id'],
                        source='fake_store',
                        title=product_data['title'],
                        price=product_data['price'],
                        quantity=0,
                        description=product_data['description'],
                        image=product_data['image'],
                        category=product_data['category'],
                        weight=product_data.get('weight', 0),
                        length=product_data.get('length', 0),
                        width=product_data.get('width', 0),
                        height=product_data.get('height', 0)
                    )
                    self.db.session.add(product)
                else:
                    product.title = product_data['title']
                    product.price = product_data['price']
                    product.description = product_data['description']
                    product.image = product_data['image']
                    product.category = product_data['category']

            self.db.session.commit()
            print("Products loaded successfully.")
        except requests.RequestException as e:
            print(f"Failed to load products from Fake Store API: {e}")
        except Exception as e:
            self.db.session.rollback()
            print(f"An error occurred: {e}")

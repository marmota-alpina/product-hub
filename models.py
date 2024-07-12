# Definindo modelos de banco de dados
from config import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.String, primary_key=True)
    source_id = db.Column(db.Integer)
    source = db.Column(db.String)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    image = db.Column(db.String)
    category = db.Column(db.String)
    weight = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.title}>'

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'category': self.category,
            'source_id': self.source_id,
            'source': self.source,
            'weight': self.weight,
            'length': self.length,
            'width': self.width,
            'height': self.height
        }

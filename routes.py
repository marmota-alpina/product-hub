import uuid

from flask_openapi3 import Tag, APIView
from flask import jsonify

from config import db
from fake_store_service import FakeStoreService
from models import Product
from schemas import ProductQuery, ProductBody, ProductPath, ProductBase

api_view = APIView(
    url_prefix="/product-hub/api/v1",
    view_tags=[Tag(name="product",  description="API for product management")]
)


@api_view.route("/product")
class ProductListAPIView:
    @api_view.doc(summary="Get product list")
    def get(self, query: ProductQuery):
        products = Product.query.filter_by(**query.model_dump(exclude_none=True)).all()
        serialized_products = [product.serialize() for product in products]
        return jsonify(serialized_products), 200

    # Create product
    @api_view.doc(summary="Create product")
    def post(self, body: ProductBody):
        product = Product(**body.model_dump())
        product.id = str(uuid.uuid4())
        db.session.add(product)
        db.session.commit()
        return jsonify(product.serialize()), 201


@api_view.route("/product/<int:id>")
class ProductAPIView:
    @api_view.doc(summary="Get product")
    def get(self, path: ProductPath):
        try:
            product = Product.query.get(path.id)
            if product:
                return jsonify(product.serialize()), 200
            else:
                return jsonify({"error": "Product not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @api_view.doc(summary="Update product")
    def put(self, path: ProductPath, body: ProductBase):
        product = Product.query.get(path.id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        for key, value in body.model_dump(exclude_unset=True, exclude_none=True).items():
            setattr(product, key, value)
        db.session.commit()
        return jsonify(product.serialize()), 200

    @api_view.doc(summary="Delete product")
    def delete(self, path: ProductPath):
        product = Product.query.get(path.id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"}), 200


@api_view.route("/product/<int:id>/find")
class ProductFindAPIView:
    @api_view.doc(summary="Find product")
    def get(self, path: ProductPath):
        try:
            product = Product.query.filter_by(source_id=path.id).first()
            if product is None:
                return jsonify({}), 200
            return jsonify(product.serialize()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@api_view.route("/product/synchronize")
class ProductSyncAPIView:
    @api_view.doc(summary="Sync product")
    def get(self):
        try:
            fake_store_service = FakeStoreService(db)
            fake_store_service.load_products()
            return jsonify({"success": True}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
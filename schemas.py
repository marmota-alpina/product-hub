from typing import Optional
from pydantic import BaseModel, Field


# Definindo schemas para validação de entrada com Pydantic
class ProductPath(BaseModel):
    id: str = Field(..., description="Product ID")


class ProductQuery(BaseModel):
    category: Optional[str] = Field(None, description='Category')
    title: Optional[str] = Field(None, description='Title')


class ProductBase(BaseModel):
    title: str = Field(..., description='Product title')
    price: float = Field(..., description='Product price')
    quantity: int = Field(..., description='Product quantity')
    description: str = Field(None, min_length=2, description='Product description')
    image: str = Field(None, description='Product image URL')
    category: str = Field(..., description='Product category')
    source_id: Optional[int] = Field(None, description='ID in the source system')
    source: Optional[str] = Field(None, description='Source system name')
    weight: float = Field(..., description='Product weight')
    length: float = Field(..., description='Product length')
    width: float = Field(..., description='Product width')
    height: float = Field(..., description='Product height')


class ProductBody(ProductBase):
    pass


class ConfigBody(BaseModel):
    key: str = Field(None, description='Config key')
    value: str = Field(None, description='Config value')


class ConfigPath(BaseModel):
    id: str = Field(..., description="Config ID")


class ConfigQuery(BaseModel):
    key: Optional[str] = Field(None, description='Config key')
    value: Optional[str] = Field(None, description='Config value')


class ConfigResponse(BaseModel):
    id: str = Field(..., description='Config ID')
    key: str = Field(..., description='Config key')
    value: str = Field(..., description='Config value')

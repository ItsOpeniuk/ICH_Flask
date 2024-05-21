from connection import DBConnector
from hw4_sqlalchemy import engine
from models import Categories, Product


categories_data = [
    {'category': 'Electronics', 'description': 'Devices and gadgets'},
    {'category': 'Books', 'description': 'Books and literature'},
    {'category': 'Clothing', 'description': 'Apparel and accessories'}
]


with DBConnector(engine=engine) as session:
    for obj in categories_data:
        session.add(Categories(**obj))
    session.commit()


products_data = [
    {'category_id': 1, 'name': 'Smartphone', 'price': 699.99, 'in_stock': True},
    {'category_id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True},
    {'category_id': 1, 'name': 'Headphones', 'price': 199.99, 'in_stock': False},
    {'category_id': 1, 'name': 'Smartwatch', 'price': 249.99, 'in_stock': True},
    {'category_id': 1, 'name': 'Camera', 'price': 449.99, 'in_stock': True},

    {'category_id': 2, 'name': 'Novel', 'price': 14.99, 'in_stock': True},
    {'category_id': 2, 'name': 'Science Book', 'price': 29.99, 'in_stock': True},
    {'category_id': 2, 'name': 'Cookbook', 'price': 24.99, 'in_stock': False},
    {'category_id': 2, 'name': 'History Book', 'price': 19.99, 'in_stock': True},
    {'category_id': 2, 'name': 'Children Book', 'price': 9.99, 'in_stock': True},

    {'category_id': 3, 'name': 'T-shirt', 'price': 19.99, 'in_stock': True},
    {'category_id': 3, 'name': 'Jeans', 'price': 49.99, 'in_stock': True},
    {'category_id': 3, 'name': 'Jacket', 'price': 89.99, 'in_stock': False},
    {'category_id': 3, 'name': 'Sneakers', 'price': 69.99, 'in_stock': True},
    {'category_id': 3, 'name': 'Hat', 'price': 14.99, 'in_stock': True}
]


with DBConnector(engine=engine) as session:
    for obj in products_data:
        session.add(Product(**obj))
    session.commit()

from connection import DBConnector
from hw4_sqlalchemy import engine
from models import Categories, Product
from sqlalchemy import and_, or_, not_, desc, func

with DBConnector(engine=engine) as session:
    #Извлеките все записи из таблицы categories.
    # Для каждой категории извлеките и выведите все связанные с ней продукты, включая их названия и цены.

    categories = session.query(Categories).all()
    if categories:
        for category in categories:
            print('*' * 30)
            print(f'Category: {category.category}')
            for product in category.products:
                print(f'Product - {product.name}, Price - {product.price}')

    #Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.

    smartphone = session.query(Product).filter(Product.name == 'Smartphone').first()
    if smartphone is not None:
        smartphone.price =  349.99
        session.commit()
        print(f'New price for Smartphone = {smartphone.price}')

    #Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.

    count_prod = session.query(
        Categories.category,
        func.count(Product.id).label("product_count")
    ).join(Categories).group_by(Product.category_id).all()

    print("Category: Amount of products")
    print("_" * 100)
    for group in count_prod:
        print(f"{group.category}: {group.product_count}")

    # Отфильтруйте и выведите только те категории, в которых более одного продукта.

    more_than_1 = session.query(
        Categories.category, func.count(Product.id).label("product_amount")
    ).join(Product).group_by(Categories.id).having(func.count(Product.id) > 1).all()

    print("Categories with amount of products more that 1:")
    print("_" * 100)
    for category in more_than_1:
        print(f"{category.category}")
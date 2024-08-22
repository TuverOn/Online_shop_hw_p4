from typing import Any

from src.product import Product
from src.zero_product_exception import ZeroProductException


class Category:
    """Категория товара"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        all_quantity = 0
        for j in self.__products:
            all_quantity += j.quantity
        return f"{self.name}, количество продуктов: {all_quantity} шт."

    def add_product(self, products: Product) -> Any:
        if isinstance(products, Product):
            try:
                if products.quantity == 0:
                    raise ZeroProductException(
                        "Нельзя добавить товар с нулевым количеством"
                    )
            except ZeroProductException as e:
                print(str(e))
            else:
                self.__products.append(products)
                Category.product_count += 1
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def get_product_list(self) -> str:
        product_list = ""
        for product in self.__products:
            product_list += f"{str(product)}\n"
        return product_list

    @property
    def products(self) -> list:
        products_list = []
        for product in self.__products:
            products_list.append(product)
        return products_list

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0

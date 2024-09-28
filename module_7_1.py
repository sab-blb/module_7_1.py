class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            content = file.read().strip()
            file.close()
            return content
        except FileNotFoundError:
            return ""

    def add(self, *products):
        current_products_str = self.get_products()
        current_products_list = current_products_str.split('\n') if current_products_str else []
        existing_names_weights = {tuple(line.split(', ')[:2]) for line in current_products_list if line}

        file = open(self.__file_name, 'a')
        for product in products:
            product_key = (product.name, str(product.weight))
            if product_key in existing_names_weights:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file.write(f"{product}\n")
                existing_names_weights.add(product_key)
        file.close()


#Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


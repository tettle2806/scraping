from base_parser import BaseParser
from time import time
from mixins import EditPriceMixin, ProductDetailMixin, ProductImageMixin

class CreditAsiaParser(BaseParser, EditPriceMixin, ProductDetailMixin, ProductImageMixin):
    def __init__(self):
        super(CreditAsiaParser, self).__init__()
        self.data = {}


    def main_page_parser(self):
        """Парсер главной страницы"""
        html = self.get_html()
        soup = self.get_soup(html)
        categories_block = soup.find('div', class_='desc-catalog-block-item-next-level')
        categories = categories_block.find_all('div', class_='sub-menu__item')
        for category in categories:
            category_title = category.find('a').get_text(strip=True)
            category_link = self.host + category.find('a').get('href')
            print('\033[93m' + category_title)
            print(category_link)
            self.data[category_title] = []

            self.category_page_parser(category_title, category_link)


    def category_page_parser(self, category_title, category_link):
        soup = self.get_soup(self.get_html(category_link))
        products_block = soup.find('div', class_='catalog-section-cont-product')
        products = products_block.find_all('div', class_='product_slider-card')
        for product in products:
            title = product.find('a', class_='product_slider-name').get_text(strip=True)
            print('\033[36m' + title)
            try:
                price = product.find('div', class_='price').get_text(strip=True)
                price = self.edit_price(price)
            except:
                price = 'Цена не указана'
            print(price)

            product_link = self.host + product.find('a', class_='product_slider-img').get('href')

            product_soup = self.get_soup(self.get_html(product_link))

            image_link = self.get_image(product_soup)
            if image_link != 'Нет изображения':
                image_link = self.host + image_link
            configs = self.get_detail(product_soup)

            self.data[category_title].append({
                'Наименование товара': title,
                'Цена товара': price,
                'Ссылка на товар': product_link,
                'Ссылка на изображение': image_link,
                'Характеристики': configs
            })




def start_parsing():
    start = time()
    parser = CreditAsiaParser()
    parser.main_page_parser()
    parser.save_json('elections', parser.data)

    finish = time()
    print(f'Парсер отработал за {finish - start} секунд')


start_parsing()
# 947 600 сум 47 380 сум -> 94760047380
# 1 - Если у цены есть скидка - брать только цену со скидкой
# 2 - Придумать как проходиться по всем страницам категории если их больше 1
# 3 - Спарсить все 5 крупных категории

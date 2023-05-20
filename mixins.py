# mixins - несамостоятельные классы созданные, чтобы расширять основные классы

class EditPriceMixin:

    def edit_price(self, price: str):
        # '2 466 750сум' -> 2466750
        lst = [i for i in price if i.isdigit()] # ['2', '4', '6'....]
        str1 = ''.join(lst)
        return int(str1)



class ProductDetailMixin:

    def get_detail(self, soup):
        data = {}
        block = soup.find('div', class_='configuration')
        configurations = block.find_all('div', class_='configuration-item')
        try:
            for conf in configurations:
                title = conf.find('div', class_='configuration-item-row-title').get_text(strip=True)
                data[title] = {}
                details = conf.find('div', class_='configuration-item-row-detail')
                rows = details.find_all('div', class_='flex')
                for row in rows:
                    r_title = row.find('span', class_='title').get_text(strip=True)
                    r_info = row.find('span', class_='info').get_text(strip=True)
                    data[title][r_title] = r_info
        except:
            data['Общее'] = 'Нет данных'
        return data



class ProductImageMixin:
    def get_image(self, soup):
        try:
            image_link = soup.find('a', class_='fancybox').get('href')
        except:
            image_link = 'Нет изображения'
        return image_link



import scrapy

from bs4 import BeautifulSoup
from travelspider2.items import TravelspiderItem


class TravelSpider(scrapy.Spider):
    name = "travel"
    allowed_domains = ["travel.qunar.com"]
    start_urls = [
         f"https://travel.qunar.com/p-cs299979-chongqing-jingdian"
         ,*[f"https://travel.qunar.com/p-cs299979-chongqing-jingdian-1-{page}" for page in range(2, 200)]
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        # 提取景点信息
        items = soup.find_all('div', class_='ct')
        for item in items:
            name = item.find('span', class_='cn_tit').get_text(strip=True)
            review_count = item.find('span', class_='icon_comment').next_sibling.strip()
            rating_percentage = int(item.find('span', class_='cur_star')['style'].split(':')[1].strip('%;'))
            print(name)
            print(review_count)
            travel_item = TravelspiderItem()
            travel_item['name'] = name
            travel_item['review_count'] = review_count
            travel_item['score'] = rating_percentage

            yield travel_item


        next_page = soup.find('a', class_='next')
        if next_page:
            next_page_url = response.urljoin(next_page['href'])
            yield scrapy.Request(url=next_page_url, callback=self.parse)
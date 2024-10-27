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
        # 使用内置 HTML 解析器 解析HTML文本
        soup = BeautifulSoup(response.text, 'html.parser')

        #根据网页源代码 找到单个景点对应的标签
        items = soup.find_all('div', class_='ct')
        for item in items:
            # 提取景点名称、评论数量和评分
            name = item.find('span', class_='cn_tit').get_text(strip=True)
            review_count = item.find('span', class_='icon_comment').next_sibling.strip()
            rating_percentage = int(item.find('span', class_='cur_star')['style'].split(':')[1].strip('%;'))

            # 创建 TravelspiderItem 实例，并将数据填充到该实例中
            travel_item = TravelspiderItem()
            travel_item['name'] = name
            travel_item['review_count'] = review_count
            travel_item['score'] = rating_percentage

            yield travel_item

        # 提取下一页的链接
        next_page = soup.find('a', class_='next')
        if next_page:
            next_page_url = response.urljoin(next_page['href'])
            #回调函数
            yield scrapy.Request(url=next_page_url, callback=self.parse)
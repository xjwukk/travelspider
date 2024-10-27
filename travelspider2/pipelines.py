import openpyxl

class ExcelPipeline:
    def open_spider(self, spider):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['景点名称', '评分', '评论数'])

    def close_spider(self, spider):
        self.wb.save('data.xlsx')

    def process_item(self, item, spider):
        self.sheet.append([item['name'], item['score'], item['review_count']])
        return item

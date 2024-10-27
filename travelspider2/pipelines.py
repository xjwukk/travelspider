import openpyxl

class ExcelPipeline:
    def open_spider(self, spider):
        # 当爬虫启动时调用，初始化 Excel 工作簿和工作表
        self.wb = openpyxl.Workbook()  # 创建一个新的 Excel 工作簿
        self.sheet = self.wb.active  # 获取当前活跃的工作表
        # 在工作表的第一行添加标题
        self.sheet.append(['景点名称', '评分', '评论数'])

    def close_spider(self, spider):
        # 当爬虫关闭时调用，保存 Excel 文件
        self.wb.save('data.xlsx')  # 将工作簿保存为 'data.xlsx'

    def process_item(self, item, spider):
        # 处理爬虫返回的每个项目
        # 将项目的相关数据添加到工作表中
        self.sheet.append([item['name'], item['score'], item['review_count']])
        return item  # 返回处理后的项目

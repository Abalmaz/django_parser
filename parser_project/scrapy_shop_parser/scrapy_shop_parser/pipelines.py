# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .tasks import save_to_db

class ScrapyShopParserPipeline(object):
    def process_item(self, item, spider):
        save_to_db.delay(item)
        return item

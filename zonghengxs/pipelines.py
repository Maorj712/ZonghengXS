# -*- coding: utf-8 -*-
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ZonghengxsPipeline(object):
    def process_item(self, item, spider):
        path = 'F:\\PycharmProjects\\novel\\{0}'.format(item['name'])
        folder = os.path.exists(path)
        if not folder:
            os.mkdir(path)
        filename = '\\' + item['title'] + '.txt'
        with open(path+filename, 'w') as f:
            f.write(item['details'])
        return item

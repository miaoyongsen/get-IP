# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class GetproxyPipeline(object):
    def process_item(self, item, spider):

        fileName = '/Users/amiao/Desktop/wangziliao/ip.txt'
        with open(fileName, "a") as f:
            f.write(item['protocol'] + '://' + item['ip'] + ":" + item['port'] + ',')

        f.close()
        return item



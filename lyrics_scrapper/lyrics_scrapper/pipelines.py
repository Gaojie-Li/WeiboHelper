import pymongo

class FilePipeline(object):
    def process_item(self, item, spider):
        with open('lyrics.txt', 'w', encoding='utf-8') as f:
            titles = item['title']
            song = item['song']
            for i,j in zip(titles, song):
                f.write(i + ':' + j + '\n')
        return item        
        


class MongoPipeline(object):

    collection = 'zhoujielun'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_RUI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        data = dict(item)
        table.insert_one(data)
        return item
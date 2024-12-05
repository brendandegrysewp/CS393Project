# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import random


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CountriesPipeline:
    def __init__(self):
        # print("pipeline")
        try:
            print(mysql.connector.apilevel)
            self.conn = mysql.connector.MySQLConnection(
                host = '127.0.0.1',
                user = 'django',
                password = 'mysecretpassword',
                database = 'aliens'
            )
            # print("succeeded")
        except Exception as e:
            print("failed")
            print(e)
        # print(self.conn)

        # print("pipeline")
        #     ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()
        # print("pipeline")
        # print(self.cur)
        pass

    def process_item(self, item, spider):

        ## Define insert statement
        # print(item)
        if item["country"] != None and item["name"] != None and item["position"] != None:
            self.cur.execute(""" insert into GovernmentEmployee (country, name, position) values (%s,%s,%s)""", (
                item["country"],
                item["name"],
                item["position"]
            ))

        ## Execute insert of data into database
            self.conn.commit()
            return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
        pass

class SpacecraftPipeline:
    def __init__(self):
        # print("pipeline")
        self.sighting = 1
        try:
            print(mysql.connector.apilevel)
            self.conn = mysql.connector.MySQLConnection(
                host = '127.0.0.1',
                user = 'django',
                password = 'mysecretpassword',
                database = 'aliens'
            )
            # print("succeeded")
        except Exception as e:
            print("failed")
            print(e)
        # print(self.conn)

        # print("pipeline")
        #     ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()
        # print("pipeline")
        # print(self.cur)
        pass

    def process_item(self, item, spider):

        ## Define insert statement
        # print(item)
        if item["model"] != None and item['model'] not in ["(",")",'"',",","."]:
            self.cur.execute(""" insert into expedition (sightingId, craftModel, duration) values (%s,%s,%s)""", (
                str(self.sighting),
                item["model"],
                str(random.randint(5,1800))
            ))

        ## Execute insert of data into database
            self.conn.commit()
            return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
        pass
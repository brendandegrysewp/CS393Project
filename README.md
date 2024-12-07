# Setup
1. Run the aliensDB.sql script
2. Do a Django migration
3. Run `scrapy crawl country` with the second pipeline commented out in settings and the first one active
4. Run alienCsvClean.py
5. Run `scrapy crawl spacecraft` with the first pipeline commented out in settings and the second one active
6. Run populateDB.sql

# Setup
1. Run the aliensDB.sql script
2. Run `scrapy crawl country` with the second pipeline commented out in settings and the first one active
3. Run `scrapy crawl spacecraft` with the first pipeline commented out in settings and the second one active
4. Run all but the last 2 lines of populateDB.sql
5. Run alienCsvClean.py
6. Run the last 2 lines of populateDB.sql

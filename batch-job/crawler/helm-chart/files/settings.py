BOT_NAME = 'yna_crawler'
SPIDER_MODULES = ['yna_crawler.spiders']
NEWSPIDER_MODULE = 'yna_crawler.spiders'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS_PER_DOMAIN = 2
ITEM_PIPELINES = {'yna_crawler.pipelines.YnaCrawlerPipeline': 300}
ELASTICSEARCH_PROTOCOL = 'http'
ELASTICSEARCH_HOST = 'elasticsearch-master'
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_USERNAME = 'elastic'
ELASTICSEARCH_PASSWORD = 'elastic'
LOG_STDOUT = True
FEED_EXPORT_ENCODING = 'utf-8'
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.jobboard.spiders.bulldogjob import BulldogJobSpider

import yaml


def crawl(settings_path: str):

    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_path)
    process = CrawlerProcess(get_project_settings())
    process.crawl(BulldogJobSpider)
    process.start()


def main():
    with open("params.yaml", "r") as f:
        cfg = yaml.safe_load(f)['scrap']

    crawl(cfg['crawler_settings'])


main()

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.models.boxingscraper import Scraper
from tinydb import TinyDB
from dotenv import dotenv_values
import logging
from datetime import datetime


class FightModel:

    def __init__(self):

        logging.basicConfig(filename='scraperschedule.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        env_vars = dotenv_values(".env")
        scrape_hour = env_vars.get('scrape_hour')
        scrape_minute = env_vars.get('scrape_minute')

        self.db = TinyDB('fights_db.json')
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.scrape_and_cache, CronTrigger(hour=scrape_hour, minute=scrape_minute))
        self.scheduler.start()
        logging.info(f"schedule started {datetime.now()}")

    def scrape_and_cache(self):
        scraper = Scraper()
        fights_scraped = scraper.get_schedule()
        self.db.truncate()
        self.db.insert_multiple(fights_scraped)
        print("Scraped")

    def get_cached_fights(self):
        fights = self.db.all()
        return fights

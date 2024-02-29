from app import app
from flask import request, jsonify
from app.models.boxingscraper import Scraper
from app.models.boxingfilter import Filter
from app.models.scrapescheduledb import FightModel


fightmodel = FightModel()
filter = Filter()
fights_scraped = fightmodel.get_cached_fights()


@app.route("/api/fights/")
def get_upcoming_fights_route():

    fights = filter.get_fights(
        request.args.get('top', type=int),
        request.args.get('month', type=str),
        request.args.get('title', type=str),
        fights_scraped
    )

    return jsonify(fights)


@app.route("/api/fights/<string:name>/")
def get_fight_by_name_route(name):

    fight = filter.get_fight_by_name(name, fights_scraped)

    return fight


@app.route("/api/fights/today/")
def get_fights_today_route():

    fights = filter.get_fights_today(fights_scraped)

    return fights

@app.route("/")
def time_check():
    return jsonify({"date":f"{filter.get_today_date()}"})

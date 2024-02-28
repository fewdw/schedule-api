import datetime

class Filter:
    def __init__(self):
        pass

    # function to check if query params are valid
    def check_valid(self, top, month, title):
        errors = []

        # no params entered
        if top is None and month is None and title is None:
            return "all_none"

        # params have errors
        if not isinstance(top, int):
            errors.append("invalid")
            print("invalid top")
        if str(month).upper() not in ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANY']:
            print("invalid month")
            errors.append("invalid")
        if str(title).upper() not in ["TRUE", "FALSE", "ANY"]:
            print("invalid title")
            errors.append("invalid")

        if errors:
            return "invalid"
        else:
            return "filter"


    def filter_fights(self, fights, top, month, is_title):
        filtered_fights = []

        # Convert month to lowercase for case-insensitive comparison
        month = month.lower()

        # Convert is_title to boolean if it's not 'any'
        if is_title != 'any':
            is_title = is_title.lower() == 'true'

        for fight in fights:
            # Extract the month from the date
            fight_month = fight['date'].split()[0]

            # Check if the month matches the specified month or if month is 'any'
            if month == 'any' or fight_month.lower() == month:
                # Check if the fight title matches the specified title or if title is 'any'
                if is_title == 'any' or fight['is_title'] == is_title:
                    filtered_fights.append(fight)

        # Sort the filtered fights by date
        filtered_fights.sort(key=lambda x: x['date'])

        # Return the top 'top' number of fights if specified
        if top:
            return filtered_fights[:top]
        else:
            return filtered_fights


    # function that returns a normal list of fights
    def get_fights(self, top, month, is_title, fights_scraped):

        fights = []

        msg = self.check_valid(top, month, is_title)

        if msg == "all_none":
            fights = fights_scraped
        if msg == "invalid":
            fights = {"error": "please verify all query params are present"}
        if msg == "filter":
            fights = self.filter_fights(fights_scraped, top, month, is_title)

        return fights

    def get_fight_by_name(self, name, fights_scraped):

        filtered_fights = []

        if len(name) > 3:
            for fight in fights_scraped:
                boxers = fight.get("boxers", [])
                if any(name.upper() in boxer.upper() for boxer in boxers):
                    filtered_fights.append(fight)
        else:
            filtered_fights = {"error" : "name must be longer than 3 chars"}

        if len(filtered_fights) == 0:
            filtered_fights = {"error" : f"no boxer with name {name}"}

        return filtered_fights


    def get_today_date(self):
        current_date = datetime.datetime.now()
        day = current_date.day
        month = current_date.strftime("%B")[:3]

        current = f"{month} {day}"

        return current


    def get_fights_today(self, fights_scraped):

        fights_today = []

        today_date = self.get_today_date()

        fights = fights_scraped

        for fight in fights:
            if fight['date'] == today_date:
                fights_today.append(fight)

        if len(fights_today) == 0:
            fights_today = {"response" : "no fights today, go take a walk!"}

        return fights_today

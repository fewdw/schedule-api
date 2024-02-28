from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        pass

    def get_schedule(self):
        url = 'https://www.boxingscene.com/schedule'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        fights = []

        for fight in soup.find_all('div', class_='schedule-fight'):
            fight_info = {}

            # Extracting boxers' names
            boxers_elem = fight.find('div', class_='fight-title').find('h3')
            fight_info['boxers'] = [name.strip() for name in boxers_elem.text.split('vs')]

            # Extracting division
            division_elem = fight.find('div', class_='fight-notes')
            fight_info['division'] = division_elem.text.strip() if division_elem else None

            # Extracting location
            fight_info['location'] = fight.find('div', class_='schedule-details').find_all('div')[-1].text.strip()

            # Extracting networks
            fight_info['network'] = [network.text.strip() for network in fight.find('div', class_='schedule-details').find_all('div')[1:-1]]

            # Extracting time
            time_elem = fight.find('div', class_='schedule-details').find('div', class_='mb-2')
            time_text = time_elem.text.strip() if time_elem else 'Check Local Listing'
            if 'Check Local Listing' not in time_text:
                # Remove everything after 'EST' if it's not 'Check Local Listing'
                time_text = time_text.split(' EST')[0] + ' EST'
            fight_info['time'] = time_text

            # Extracting date
            fight_info['date'] = fight.find('div', class_='fight-date').text.strip()

            # Extracting day
            day_elem = fight.find('div', class_='fight-day')
            fight_info['day'] = day_elem.text.strip() if day_elem else None

            # Checking if division contains "Title"
            fight_info['is_title'] = 'Title' in fight_info['division'] if fight_info['division'] else False

            fights.append(fight_info)

        return fights

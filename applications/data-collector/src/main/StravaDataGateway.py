import requests
import os
from dotenv import load_dotenv

class StravaDataGateway:
    def __init__(self):
        self.REFRESH_TOKEN = None
        self.ACCESS_TOKEN = 'af417a0d2256db0c1b5c5bdaa6e88ec6ce58a1e1'
        self._load_env_variables()

    def _load_env_variables(self):
        load_dotenv()
        self.CLIENT_ID = os.getenv('CLIENT_ID')
        self.CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        self.REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

    def get_access_token(self):
        params = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'grant_type': 'refresh_token',
            'refresh_token': self.REFRESH_TOKEN
        }

        res = requests.post('https://www.strava.com/api/v3/oauth/token', params=params)
        self.REFRESH_TOKEN = res.json()['refresh_token']
        access_token = res.json()['access_token']
        return access_token

    def auth_user(self):
        params = {
            'client_id': '98562',
            'client_secret': '1529ac60728f98d6ac564ff4e18e03687eed5356',
            'code': '7a411ea142584bdda924167fdd001ce5fa355c8e',
            'grant_type': 'authorization_code'
        }
        res = requests.post('https://www.strava.com/oauth/token', params=params)
        print(res.json())

    def get_starred_segments(self):
        headers = {
            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
        }

        res = requests.get('https://www.strava.com/api/v3/segments/starred', headers=headers)
        print(res.status_code)
        return res.json()

    def get_external_segment(self, id):
        headers = {
            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
        }
        res = requests.get(f"https://www.strava.com/api/v3/segments/{id}", headers=headers)
        return res.json()
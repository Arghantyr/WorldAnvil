# This file does nothing. It's here just for fun.
# It could, but it does nothing.

import json
import os.path
from pywaclient.api import BoromirApiClient

CONFIG_PATH = "../../config"
SCRIPT_NAME = "Stat_Hunter"
SCRIPT_LINK = ""
SCRIPT_VERSION = "1.1"
WORLD_ID = "9e606222-37af-4e55-9657-1866733ca047"

class WA_Client():
    def __init__(self):
        self.authenticated_user = {}
        self.worlds = {}
        self.articles = {}

        self.load_credentials()
        self.initialize()
        self.authenticate()
        self.pull_worlds()

    def load_credentials(self):
        with open(os.path.join(CONFIG_PATH, "credentials.json")) as fp:
            self.credentials = json.load(fp=fp)
        print("Credentials loaded.")
    def initialize(self):
        self.client =  BoromirApiClient(SCRIPT_NAME, SCRIPT_LINK, SCRIPT_VERSION,
                        self.credentials['API_key'],
                        self.credentials['API_token']
                        )
        print("Client initialized.")
    def authenticate(self):
        self.authenticated_user = self.client.user.identity()
        print(f"Authenticated user: {self.authenticated_user}")
    def pull_worlds(self):
        self.worlds = {world['id']: world for world in self.client.user.worlds(self.authenticated_user['id'])}
    def pull_categories(self):
        try:
            if WORLD_ID in self.worlds.keys():
                self.articles = {category['id']: {} for category in self.client.world.categories(WORLD_ID)}
                self.articles['-1'] = {}
            else:
                print(f"No world with ID: {WORLD_ID} found for the current seeker.")
        except Exception as e:
            print(f"Encountered problems while pulling categories:\n{e}")
    def pull_articles(self):
        try:
            if WORLD_ID in self.worlds:
                for category_id in self.articles.keys():
                    self.articles[category_id] = [
                        article['id'] for article in self.client.world.articles(WORLD_ID, category_id)
                    ]
        except Exception as e:
            print(f"Encountered problems while pulling articles:\n{e}")
    def pull_single_article(self, article_id: str=None, granularity: int = -1):
        try:
            article_json = self.client.article.get(article_id, granularity)
            return article_json
        except Exception as e:
            print(f"Encountered problems while pulling the specified article:\n{e}")


# This file does nothing. It's here just for fun.
# It could, but it does nothing.

import os
import time
import json
from pywaclient.api import BoromirApiClient

with open("../../config/credentials.json") as fp:
    credentials = json.load(fp=fp)

os.environ["WA_APPLICATION_KEY"]=credentials["API_key"]
os.environ["WA_AUTH_TOKEN"]=credentials["API_token"]
Script_name="Stat_Hunter"
Script_link=""
Script_version="1.1"
WORLD_ID='9e606222-37af-4e55-9657-1866733ca047'   #to be config'd


client = BoromirApiClient(
    Script_name,
    Script_link,
    Script_version,
    os.environ['WA_APPLICATION_KEY'],
    os.environ['WA_AUTH_TOKEN']
)

print("Starting script!")
# get your own user id. It is not possible to discover the user ids of other users via the API.
authenticated_user = client.user.identity()
print(f"Authenticated user: {authenticated_user}")

# get the references to all the category on the first world.
categories_ids = [category['id'] for category in client.world.categories(WORLD_ID)]
categories_ids.append('-1')

print(f"Category ids: {categories_ids}")

article_ids = []
# gets a list of all the articles without a category in the first world
for cat_id in categories_ids:
    article_ids += [article['id'] for article in client.world.articles(WORLD_ID, cat_id)]



#print(f"stat_properties: {stat_properties}")

for article_id in article_ids[:5]:
    try:
        article_json=client.article.get(article_id, 0)
        print('=========================')
        print(f"Article id: {article_id}\nArticle: {article_json}")
        #print(f"Article JSON at granularity {granularity}:\n{article_json}")
        stat_properties=[
            'state', 'isWip','isDraft', 'entityClass', 'tags', 'wordcount', 'likes', 'views'
        ]
        result_dict = {_key: article_json[_key] for _key in stat_properties}
        for time_property in ['creationDate', 'publicationDate', 'updateDate', 'notificationDate']:
            time_field = article_json[time_property]
            if time_field is not None:
                result_dict['_'.join([time_property, 'date'])] = time_field['date']
            else:
                result_dict['_'.join([time_property, 'date'])] = None
        current_time = time.time_ns()

        print(f"This is how the output looks like: {result_dict}")
    except Exception as e:
        print(f"Encountered a problem: {e}")

if '__name__'=='__main__':
    print("The end of the script!")


from Utility import WA_Client
import json



client = WA_Client()
"""
Get the self USER_ID
"""
print("Starting script!")
# get your own user id. It is not possible to discover the user ids of other users via the API.
authenticated_user = client.authenticated_user
print(f"Authenticated user: {authenticated_user}")

client.pull_categories()
categories_ids = [i for i in client.articles.keys()]
print(f"Category ids: {categories_ids}")

# gets a list of all the articles without a category in the first world
client.pull_articles()
article_ids = []
for category_id in client.articles.keys():
    article_ids += client.articles[category_id]


for article_id in article_ids[:5]:
    try:
        article_json = client.pull_single_article(article_id = article_id, granularity = 0)
        #print(f"Article JSON at granularity {granularity}:\n{article_json}")
        print(json.dumps(article_json, indent=2))

    except Exception as e:
        print(f"Encountered a problem: {e}")

if '__name__'=='__main__':
    print("The end of the script!")


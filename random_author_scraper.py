import json
import pickle
import requests
import time


def make_request(uri, max_retries=5):
    def fire_away(uri):
        response = requests.get(uri)
        assert response.status_code == 200
        return json.loads(response.content)
    current_tries = 1
    while current_tries < max_retries:
        try:
            time.sleep(1)
            response = fire_away(uri)
            return response
        except:
            time.sleep(1)
            current_tries += 1
    return fire_away(uri)


authors = []

json_data = make_request("https://api.pushshift.io/reddit/submission/search/?size=100")
for data in json_data["data"]:
    authors.append(data["author"])

with open("random_author_scraper_log.txt", "w") as l:
    l.write("Number of authors: " + str(len(authors)) + "\n")
    l.write("-----------------------------------------------------\n")
    for a in authors:
        l.write(a + "\n")

with open("random_authors.pickle", "wb") as p:
    pickle.dump(authors, p)

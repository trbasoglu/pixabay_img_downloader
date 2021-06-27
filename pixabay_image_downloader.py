import json
import requests
import sys
from tqdm import tqdm

configPath = "config.json"
if(sys.argv.__len__()>1):
    configPath = sys.argv[1]
fp = open(configPath, "r")

config = json.load(fp)

apikey = config["API-KEY"]
root_url = "https://pixabay.com/api/?key="+apikey
query_words = config["Keywords"]

for i in tqdm(range(len(query_words)),desc="Full process"):
    query_word = query_words[i]
    try:
        for page in tqdm(range(1,config["pageNumber"]),desc=f"pages for '{query_word}'"):
            session = requests.Session()
            get_url = root_url+"&q={}&per_page=&page={}&image_type=photo".format(query_word, page)
            query = session.get(get_url)

            query_dictionary = query.json() # keys:'totalHits', 'hits', 'total'
            total_hits = query_dictionary["totalHits"]
            hits = query_dictionary['hits']
            total = query_dictionary['total']
            '''
            ***********hit KEYS*******
            ['largeImageURL', 'webformatHeight', 'webformatWidth', 'likes', 'imageWidth', 'id',
            'user_id', 'views', 'comments', 'pageURL', 'imageHeight', 'webformatURL', 'type',
            'previewHeight', 'tags', 'downloads', 'user', 'favorites', 'imageSize', 'previewWidth',
            'userImageURL', 'previewURL']
            '''

            for j in tqdm(range(len(hits)),desc="Downloading"):
                hit = hits[j]
                img_query=session.get(hit['largeImageURL'])
                file_name = f"{hit['pageURL'].split('/')[-2]}.png"
                with open(file_name, 'wb') as f:
                    f.write(img_query.content)
    except json.decoder.JSONDecodeError as e:
        print(f"Exception occured:{e}\n")
        continue

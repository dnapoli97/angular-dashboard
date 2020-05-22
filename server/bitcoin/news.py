import requests, pathlib, json, os
from dotenv import load_dotenv
load_dotenv()

def main():
    jsonFilePath = os.path.dirname(os.path.abspath(__file__))+"/news.json"
    apiKey = os.getenv('NEWS_API_KEY')
    newsArticles = requests.get('https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey=' + apiKey).json()
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(newsArticles, indent=4))

main()

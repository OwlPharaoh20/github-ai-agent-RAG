#import modules & dependencies
import os 
import requests 
from dotenv import load_dotenv
from langchain_core.documents import Document


#load environment variables
load_dotenv()

#get github token
github_token = os.getenv("GITHUB_TOKEN")


#Function to fetch data (github issues) from github 
def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {github_token}",

    } 

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed with status code:", response.status_code)
        return []
    
    print(data)
    return data 






import serpapi
from dotenv import load_dotenv
import os

load_dotenv()

def search_profile(name: str):
  params = {
    "engine": "google",
    "q": name + " linkedin profile",
    "api_key": os.getenv("SERPAPI_KEY"),
  }

  try:
    search = serpapi.search(params)
    organic_results = search["organic_results"]
    link = organic_results[0]["link"]
    snippet = organic_results[0]["snippet"]
    if snippet == "No information is available for this page.":
      return "No good search result found"
    else:
      return link
  except Exception as e:
    raise ValueError("No good search result found")



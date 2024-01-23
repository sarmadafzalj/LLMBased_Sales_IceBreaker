import os
from dotenv import load_dotenv
import requests

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from linkedin profiles,
    Manually scrape the information from the Linkedin profile"""

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": os.getenv("PROXYCURL_KEY")}

    if linkedin_profile_url == "No good search result found":
        return "No Data Found for the profile"
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    # original = data
    # data = {
    #     k:v
    #     for k, v in data.items()
    #     if v not in ([], "", "", None) and k not in ["people_also_viewed"]
    # }

    # if data.get("groups"):
    #     for group_dict in data.get("groups"):
    #         group_dict.pop("profile_pic_url")

    return data#response.json()


#print( scrape_linkedin_profile("https://www.linkedin.com/in/sarmadafzal/"))
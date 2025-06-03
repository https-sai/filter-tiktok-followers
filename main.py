from dotenv import load_dotenv
import os
from api import fetch_all_followers
from filter import filter_usernames_by_keywords
from utils import save_json

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
KEYWORDS = [
  "cat",
  "dog"
]


followers = fetch_all_followers(ACCESS_TOKEN, USER_ID)
filtered = filter_usernames_by_keywords(followers, KEYWORDS)

save_json("all_followers.json", followers)
save_json("filtered_followers.json", filtered)

print(f"Total followers: {len(followers)}")
print(f"Filtered: {len(filtered)}")
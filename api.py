import requests
import time

def fetch_all_followers(access_token, user_id, max_count=100):
    url = "https://open.tiktokapis.com/v2/research/user/followers/"
    headers = {"Authorization": f"Bearer {access_token}"}
    followers = []
    cursor = 0

    while True:
        params = {"user_id": user_id, "cursor": cursor, "max_count": max_count}
        res = requests.get(url, headers=headers, params=params).json()
        batch = res.get("data", {}).get("followers", [])
        followers.extend(batch)
        print(f"Fetched {len(followers)}...")

        cursor = res.get("data", {}).get("cursor")
        if not cursor or not batch:
            break
        time.sleep(1)

    return followers
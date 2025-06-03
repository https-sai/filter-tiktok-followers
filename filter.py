def filter_usernames_by_keywords(followers, keywords):
    return [
        f for f in followers
        if any(k.lower() in f["username"].lower() for k in keywords)
    ]
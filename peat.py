import json
import os
import re

 #save title
def normalize_title(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(r"[^\w\s]", "", title)  # إزالة الرموز مثل علامات التنصيص والنقاط
    title = re.sub(r"\s+", " ", title)  # إزالة الفراغات الزائدة
    return title

# load posts
def load_posted_titles():
    if os.path.exists("posted_articles.json"):
        with open("posted_articles.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# dowload
def save_posted_title(title):
    posted = load_posted_titles()
    normalized_title = normalize_title(title)
    if normalized_title not in posted:
        posted.append(normalized_title)
        with open("posted_articles.json", "w") as file:
            json.dump(posted, file)

# publish
def is_duplicate(title):
    normalized_title = normalize_title(title)
    return normalized_title in load_posted_titles()

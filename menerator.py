import re

def generate_meta_description(title: str, article: str) -> str:
    # cleaning
    article = re.sub(r"[\n\r]", " ", article)
    article = re.sub(r"<.*?>", "", article)  # إزالة الوسوم HTML
    article = re.sub(r"\s+", " ", article).strip()

    # great scentences
    sentences = re.split(r"(?<=[.!?])\s+", article)
    for sentence in sentences:
        if 40 <= len(sentence) <= 160:
            return sentence

    # fallback: generate mauaal type writing
    return f"{title.strip().capitalize()} - Learn more about this topic in a concise and informative article."

# examples:
if __name__ == "__main__":
    title = "Moving Toward Circular Agriculture"
    article = """
    Circular agriculture is a modern approach that emphasizes sustainability. 
    It minimizes waste by reusing resources and integrating livestock with crop production. 
    Farmers and researchers are exploring these practices to ensure food security for the future.
    """
    meta = generate_meta_description(title, article)
    print("❤️create Meta Description:\n", meta)

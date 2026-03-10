import re


def generate_slug(text: str):

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    text = text.strip('-')

    return text
import urllib.request

def get_html_content(url):
    # Fetch HTML content using urllib
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def extract_stories(html):
    stories = []
    start_tag = '<h3 class="latest-stories__item-headline">'
    end_tag = '</h3>'

    parts = html.split(start_tag)[1:7]  # Limit to the first 6 stories

    for part in parts:
        title_end_index = part.find(end_tag)
        title = part[:title_end_index].strip()

        link_start = part.find('href="') + 6
        link_end = part.find('"', link_start)
        link = "https://time.com" + part[link_start:link_end]

        stories.append({
            "title": title,
            "link": link
        })

    return stories

if __name__ == "__main__":
    url = "https://time.com"
    html_content = get_html_content(url)
    stories = extract_stories(html_content)
    
    for story in stories:
        print(f"Title: {story['title']}")
        print(f"Link: {story['link']}")
        print()

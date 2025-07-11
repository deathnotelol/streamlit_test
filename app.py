import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="MOHA News Analytics 🇲🇲", page_icon="📊", layout="centered")

st.title("📊 MOHA.gov.mm Data Analytics Tool")

TARGET_URL = "https://moha.gov.mm/index.php/component/content/category/website-mobileapplication?layout=blog"

SEARCH_STRING = "စစ်ကိုင်းတိုင်းဒေသကြီး"

st.write(f"🔍 Analyzing articles from: [MOHA.gov.mm]({TARGET_URL})")

# Scrape function
@st.cache_data
def scrape_articles():
    articles = []
    page = 1
    while True:
        url = f"{TARGET_URL}&start={(page-1)*5}"
        response = requests.get(url)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.content, "html.parser")

        # Typical Joomla article list structure
        article_blocks = soup.find_all("div", class_="blog-item")

        if not article_blocks:
            break  # No more pages

        for article in article_blocks:
            # Get title
            title_tag = article.find("h2")
            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag.find("a")["href"]
                # Build full URL if needed
                if not link.startswith("http"):
                    link = "https://moha.gov.mm" + link

                # Get intro text (optional)
                intro = article.find("div", class_="blog-item-content")
                intro_text = intro.get_text(strip=True) if intro else ""

                # Combine title + intro for searching
                content_text = f"{title} {intro_text}"

                articles.append({
                    "title": title,
                    "link": link,
                    "text": content_text
                })

        page += 1

    return articles

# Run scrape
with st.spinner("🔄 Scraping articles..."):
    articles = scrape_articles()

total_articles = len(articles)
matching_articles = [a for a in articles if SEARCH_STRING in a["text"]]

st.success(f"✅ Total Articles Found: {total_articles}")
st.success(f"✅ Articles containing **'{SEARCH_STRING}'**: {len(matching_articles)}")

# Show matching posts
if matching_articles:
    st.write("---")
    st.write(f"### 📌 Posts containing '{SEARCH_STRING}':")
    for a in matching_articles:
        st.write(f"- [{a['title']}]({a['link']})")

# Note on view counts:
st.info("ℹ️ View count scraping depends on whether the page shows it. If each article page has view counts, this script can be expanded to visit each link and parse the count.")

import requests
import openai
import datetime

# STEP 1: Get Trending Topics (Google Trends)
def get_trending_topics():
    url = "https://trends.google.com/trends/api/dailytrends?geo=IN"
    response = requests.get(url)
    data = response.json()
    return data["default"]["trendingSearchesDays"][0]["trendingSearches"][0]["title"]

# STEP 2: Get Research Data (Serper.dev API)
def get_research_data(query):
    url = "https://google.serper.dev/search"
    payload = {"q": query}
    headers = {"X-API-KEY": "your_serper_api_key"}
    
    response = requests.post(url, json=payload)
    return response.json()

# STEP 3: Generate Blog Content (ChatGPT API)
def generate_blog_content(title, research):
    openai.api_key = "your_openai_api_key"
    
    prompt = f"Write an SEO-optimized blog on '{title}'. Use this research: {research}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# STEP 4: Save Blog to Markdown File
def save_blog(title, content):
    today = datetime.date.today()
    filename = f"_posts/{today}-" + title.replace(" ", "-").lower() + ".md"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"---\ntitle: {title}\ndate: {today}\n---\n")
        file.write(content)

# RUN AUTOMATION
topic = get_trending_topics()
research = get_research_data(topic)
blog_content = generate_blog_content(topic, research)
save_blog(topic, blog_content)

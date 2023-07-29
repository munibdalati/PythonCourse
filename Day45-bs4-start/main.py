from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)

max_val = max(article_upvotes)
index = article_upvotes.index(max_val)
print(index)
print(article_texts[index])
print(article_links[index])


# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/")
# soup = BeautifulSoup(response.text, "html.parser")
#
# news = soup.find_all(class_="titleline")
# for heading in news:
#     print(heading.find(name="a").get("href"))
#     print(heading.find(name="a").getText())
#
# scores = soup.find_all(class_="score")
# for score in scores:
#     print(score.getText().split(" ")[0])






















# # import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# #
# # print(soup.title.string)
# #
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)

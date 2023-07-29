from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movies = []
all_movies = soup.find_all(name="h3", class_="title")

for website_html in all_movies:
    movie_text = website_html.getText()
    movies.append(movie_text)

print(movies)

with open("movie.text", "w") as file:
    for i in reversed(movies):
        file.write(i+"\n")



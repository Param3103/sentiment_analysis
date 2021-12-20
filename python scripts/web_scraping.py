from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re

link1 = "https://www.imdb.com/title/tt7721946/reviews?ref_=tt_urv"
link2 = "https://www.imdb.com/title/tt8504014/reviews?ref_=tt_ov_rt"
html1 = urlopen(link1).read()
html2 = urlopen(link2).read()
urlopen(link1).close()
urlopen(link2).close()
page1_soup = soup(html1, "html.parser")
page2_soup = soup(html2, "html.parser")
page1_review = page1_soup.findAll("div",{"class":"text show-more__control"})
page1_ratings = page1_soup.findAll("div", {"class":"ipl-ratings-bar"})
page2_reviews = page2_soup.findAll("div",{"class":"text show-more__control"})
page2_ratings = page2_soup.findAll("div",{"class":"ipl-ratings-bar"})
# print(page1_ratings[0])
page1_ratings = [int(str(rating.findAll("span")[-2])[6]) for rating in page1_ratings]
page2_ratings = [int(str(rating.findAll("span")[-2])[6]) for rating in page2_ratings]
reviews = [re.sub('<br/>','',str(review)[37:-6]) for review in page1_review]+[re.sub('<br/>','',str(review)[37:-6]) for review in page2_reviews]
ratings = [1 if rating >= 5 else -1 for rating in page1_ratings+page2_ratings]

# reviews has 50 reviews of 2 movies, upon which i will do natural language processing on


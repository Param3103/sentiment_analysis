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
reviews = page1_soup.findAll("div",{"class":"text show-more__control"})
reviews2 = page2_soup.findAll("div",{"class":"text show-more__control"})
reviews = [re.sub('<br/>','',str(review)[37:-6]) for review in reviews]+[re.sub('<br/>','',str(review)[37:-6]) for review in reviews2]
# reviews has 50 reviews of 2 movies, upon which i will do natural language processing on


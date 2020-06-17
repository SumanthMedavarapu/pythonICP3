import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Deep_learning'
page = requests.get(URL)
#using beautifulsoup we will parse the data
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.string)
#find_all will find all tags
rows = soup.find_all('a')
#rows contain the list of all "a" tags
print(rows)
my_data_file = open('data.txt', 'w')
for link in rows:
    #link.get will gather  the attribute value i.e,href
    filtered_data = link.get('href')
    print(filtered_data)
    #file.write() used to write data into file
    my_data_file.write(str(filtered_data))
    #the below line is used to create new line using "\n"
    my_data_file.write("\n")

my_data_file.close()

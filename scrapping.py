import requests
import bs4
res = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = bs4.BeautifulSoup(res.text,"lxml")
#x=soup.select('.toctext')[0]
'''for i in soup.select('.toctext'):
    print(i.text)'''
print(soup.select('.thumbimage'))
computer = soup.select()

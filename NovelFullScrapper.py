import requests
from bs4 import BeautifulSoup
#import next_chapter_button

x = 1
b = int(input('highest chapter greater than 1 : '))
url = 'https://novelfull.com/a-wizards-secret/chapter-1-merlin.html'
# print(f'out -- {url}')
while x < b :
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    data = requests.get(url, headers = headers)
    soup = BeautifulSoup(data.content, 'lxml')
    report = open(f'D:\\PROJECTS\\PycharmProjects\\pythonProject\\tester\\Chapter_{x}.txt','w',encoding='utf-8')
    title = soup.find('h3').text
    report.write(title + '\n')
    content = soup.find_all('div', id='chapter-content')
    a = 0
    y = 2
    while a < y:
        for c in content:
            chp = c.findAllNext('p')
            report.write((chp[a].text) + '\n')
            y = len(chp)
            a = a+1
    report.close()
    print(f'Chapter {x} completed')
    # for i in range(1):
    #     page = soup.find('div', class_='btn-group')
    #     u = 'https://novelfull.com' + str(page.find('a', id='next_chap')['href'])
    page = soup.find('div', class_='btn-group')
    url = 'https://novelfull.com' + str(page.find('a', id='next_chap')['href'])
    # print(f'inner --- {url}')
    x = x + 1








import requests
from bs4 import BeautifulSoup

url = 'https://novelfull.com/infinite-mana-in-the-apocalypse.html'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
tst = requests.get(url, headers = headers).text
# print(tst)
soup = BeautifulSoup(tst, 'lxml')

## prints all the chapter name and there corresponding links ##
jobs = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-6')
# print(jobs)
# content = jobs.find_next('ul', class_='list-chapter')
# print(jobs)
for temp_content in jobs:
    content = temp_content.find_next('ul', class_='list-chapter')
    # print(content)
    for job in content:
        chapter_name = job.find('span', class_='chapter-text').text
        # print(chapter_name)
        temp_chapter_link = job.a['href']
        # print(temp_chapter_link)
        chapter_link = 'https://novelfull.com' + str(temp_chapter_link)
        print(chapter_name)
        print(chapter_link)
        print('')



















# for job in content:
#     chapter_name = job.find('span', class_='chapter-text').text
#     # print(chapter_name)
#     temp_chapter_link = job.a['href']
#     # print(temp_chapter_link)
#     chapter_link = 'https://novelfull.com' + str(temp_chapter_link)
#     print(chapter_name)
#     print(chapter_link)
#     print('')

# for job in jobs:
#     chapter_name = job.find('span',class_='chapter-text').text
#     chapter_name = job.findNext('span',class_='chapter-text').text
#     temp_chapter_link = job.a['href']
#     chapter_link = 'https://novelfull.com' + str(temp_chapter_link)
#     print(chapter_name)
#     print(chapter_link)
#     print('')

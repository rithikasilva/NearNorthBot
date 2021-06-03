import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time



def checkFacebook(isUserCall):


    result = requests.get("https://www.facebook.com/pg/NearNorthDSB/posts/?ref=page_internal")

    #200 means we got the website
    # print(result.status_code)


    # web source of the home page
    src = result.content

    # lxml is not something I need to worry about
    soup = BeautifulSoup(src, 'lxml') #lxml
    links = soup.find('div', {'class': '_1qkq _1ql0'}) #_4-u2 _4-u8 //////_427x
    links = links.find('p')
    content = links.getText()



    content = str(content)
    content = content.encode("ascii", "ignore")
    content = content.decode()

    file = open("nndsb/nndsbFacebook.txt", 'r+')

    fileContent = file.readline()

    if isUserCall:
        return content + " https://www.facebook.com/pg/NearNorthDSB/posts/?ref=page_internal"
    else:
        if fileContent != content:
            file.truncate(0)
            file.write(content)
            file.close()
            return content + " https://www.facebook.com/pg/NearNorthDSB/posts/?ref=page_internal"

        else:
            file.close()
            return False




def checkWebsite(isUserCall):
    result = requests.get("https://www.nearnorthschools.ca/")

    # web source of the home page
    src = result.content

    # lxml is not something I need to worry about
    soup = BeautifulSoup(src, 'lxml')

    first_link = soup.find('div', {'id': 'panel-4216-2-0-0'})
    first_link = first_link.find('a')
    first_link = first_link.attrs['href']

    second_link = soup.find('div', {'id': 'panel-4216-2-1-0'})
    second_link = second_link.find('a')
    second_link = second_link.attrs['href']

    third_link = soup.find('div', {'id': 'panel-4216-2-2-0'})
    third_link = third_link.find('a')
    third_link = third_link.attrs['href']

    news_list = [first_link, second_link, third_link]

    file = open("nndsb/nndsbWeb.txt", 'r+')

    file_content = []

    for x in range(3):
        file_content.append(file.readline())





    file_content = [x[:-1] for x in file_content]




    print_list = set(news_list) ^ set(file_content)



    final_list = set(set(print_list).intersection(news_list))


    final_list = list(final_list)


    # This is if the user uses the function to call the latest post
    if isUserCall:
        return news_list[0]

    # This is used for th hourly updates
    else:
        if len(final_list) > 0:
            file.truncate(0)
            for y in range(3):
                file.write(news_list[y] + '\n')
            file.close()

            content = ''

            for z in range(len(final_list)):
                content = content + ' ' + str(final_list[z])

            return content

        else:
            file.close()
            return False

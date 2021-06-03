import requests
from bs4 import BeautifulSoup


def checkWebsite(isUserCall):
    result = requests.get("https://www.nearnorthschools.ca/west-ferris/")


    # web source of the home page
    src = result.content

    # lxml is not something I need to worry about
    soup = BeautifulSoup(src, 'lxml')

    links = soup.find('section', {'id': 'featured-post-2'})
    links = links.find('article')
    links = links.find('a')
    link = links.attrs['href']
    content = links.getText()



    file = open("westFerris/westFerrisWeb.txt", 'r+')

    fileContent = file.readline()

    if isUserCall:
        return content + " " + link
    else:
        if fileContent != link:
            file.truncate(0)
            file.write(link)
            file.close()
            return content + " " + link

        else:
            file.close()
            return False



def checkFacebook(isUserCall):
    result = requests.get("https://www.facebook.com/pg/West-Ferris-Updates-154820244530305/posts/?ref=page_internal")

    #200 means we got the website
    # print(result.status_code)


    # print(result.headers)

    # web source of the home page
    src = result.content

    # lxml is not something I need to worry about
    soup = BeautifulSoup(src, 'lxml')  # lxml
    links = soup.find('div', {'class': '_1qkq _1ql0'})  # _4-u2 _4-u8 //////_427x
    links = links.find('p')
    content = links.getText()

    content = str(content)
    content = content.encode("ascii", "ignore")
    content = content.decode()

    # links = links.find('div', {'class': '_5_jv _58jw'})
    #links = links.find('p')
    # link = links.attrs['p']


    file = open("westFerris/westFerrisFacebook.txt", 'r+')

    fileContent = file.readline()

    if isUserCall:
        return content + " https://www.facebook.com/pg/West-Ferris-Updates-154820244530305/posts/?ref=page_internal"
    else:
        if fileContent != content:
            file.truncate(0)
            file.write(content)
            file.close()
            return content + " https://www.facebook.com/pg/West-Ferris-Updates-154820244530305/posts/?ref=page_internal"

        else:
            file.close()
            return False
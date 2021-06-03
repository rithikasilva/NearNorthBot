import requests
from bs4 import BeautifulSoup

def checkFacebook(isUserCall):
    result = requests.get("https://www.facebook.com/pg/cssraiders/posts/?ref=page_internal")

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


    file = open("chippewa/chippewaFacebook.txt", 'r+')

    fileContent = file.readline()

    if isUserCall:
        return content + " https://www.facebook.com/pg/cssraiders/posts/?ref=page_internal"
    else:
        if fileContent != content:
            file.truncate(0)
            file.write(content)
            file.close()
            return content + " https://www.facebook.com/pg/cssraiders/posts/?ref=page_internal"

        else:
            file.close()
            return False



def checkWebsite(isUserCall):
    result = requests.get("https://www.nearnorthschools.ca/chippewa/")


    # web source of the home page
    src = result.content

    # lxml is not something I need to worry about
    soup = BeautifulSoup(src, 'lxml')

    links = soup.find('div', {'id': 'pg-5730-1'})
    content = links.find('h3').getText()



    file = open("chippewa/chippewaWeb.txt", 'r+')

    fileContent = file.readline()


    if isUserCall:
        return content + " https://www.nearnorthschools.ca/chippewa/"
    else:
        if fileContent != content:
            file.truncate(0)
            file.write(content)
            file.close()
            return content + " https://www.nearnorthschools.ca/chippewa/"

        else:
            file.close()
            return False
import requests
from bs4 import BeautifulSoup


# This function checks the Chippewa Facebook page for the latest post
def check_facebook(is_user_call):

    # Sets result as the Chippewa Facebook posts page
    result = requests.get("https://www.facebook.com/pg/cssraiders/posts/?ref=page_internal")

    # Grab the source for the page
    src = result.content

    # Parse the text of the latest post
    soup = BeautifulSoup(src, 'html.parser')  # lxml
    links = soup.find('div', {'class': '_1qkq _1ql0'})  # _4-u2 _4-u8 //////_427x
    links = links.find('p')
    content = links.getText()

    # Convert the text to a string and convert all characters to ascii
    content = str(content)
    content = content.encode("ascii", "ignore")
    content = content.decode()

    # Open the respective .txt file
    file = open("chippewa/chippewaFacebook.txt", 'r+')

    # Read the only line of the file into file_content
    file_content = file.readline()

    # If the user called this function
    if is_user_call:
        # Return the latest post
        return content + " https://www.facebook.com/pg/cssraiders/posts/?ref=page_internal"
    # If the function is called automatically
    else:
        # If the newest post is indeed new
        if file_content != content:
            # Clear the file and write the content into the file
            file.truncate(0)
            file.write(content)
            file.close()
            # Return the latest post
            return content + " https://www.facebook.com/pg/cssraiders/posts/?ref=page_internal"

        else:
            file.close()
            # Return false so that the program understands to not print anything
            return False


# This function checks the Chippewa website for the newest news post
def check_website(is_user_call):
    # Set the Chippewa website as the result
    result = requests.get("https://www.nearnorthschools.ca/chippewa/")

    # Grab the source of the page
    src = result.content

    # Parse the text of the latest news
    soup = BeautifulSoup(src, 'html.parser')
    links = soup.find('div', {'id': 'pg-5730-1'})
    content = links.find('h3').getText()

    # Open the respective .txt file
    file = open("chippewa/chippewaWeb.txt", 'r+')

    # Read the only line in the .txt
    file_content = file.readline()

    # If this function was called by the user, print the latest post
    if is_user_call:
        return content + " https://www.nearnorthschools.ca/chippewa/"
    # If this function as called automatically
    else:
        # If the newest news hasn't already been posted
        if file_content != content:
            # Empty the file and write the newest news into it
            file.truncate(0)
            file.write(content)
            file.close()
            # Return the newest post title and the website
            return content + " https://www.nearnorthschools.ca/chippewa/"

        else:
            file.close()
            # Return false so that the program understands to not print anything
            return False

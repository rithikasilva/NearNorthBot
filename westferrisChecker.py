import requests
from bs4 import BeautifulSoup


# This function checks the West Ferris Facebook page for the latest post
def check_facebook(is_user_call):

    # Sets result as the Chippewa Facebook posts page
    result = requests.get("https://www.facebook.com/pg/West-Ferris-Updates-154820244530305/posts/?ref=page_internal")

    # Grab the source for the page
    src = result.content

    # Parse the text of the latest post
    soup = BeautifulSoup(src, 'html.parser')
    links = soup.find('div', {'class': '_1qkq _1ql0'})
    links = links.find('p')
    content = links.getText()

    # Convert the text to a string and convert all characters to ascii
    content = str(content)
    content = content.encode("ascii", "ignore")
    content = content.decode()

    # Open the respective .txt file
    file = open("westFerris/westFerrisFacebook.txt", 'r+')

    # Read the only line of the file into file_content
    file_content = file.readline()

    # If the user called this function
    if is_user_call:
        # Return the latest post
        return content + " https://www.facebook.com/pg/West-Ferris-Updates-154820244530305/posts/?ref=page_internal"
    # If the function is called automatically
    else:
        # If the newest post is indeed new
        if file_content != content:
            # Clear the file and write the content into the file
            file.truncate(0)
            file.write(content)
            file.close()
            # Return the latest post
            return content + " https://www.facebook.com/pg/West-Ferris-Updates-154820244530305/posts/?ref=page_internal"

        else:
            file.close()
            # Return false so that the program understands to not print anything
            return False


# This function checks the West Ferris website for the newest news post
def check_website(is_user_call):

    # Set the West Ferris website as the result
    result = requests.get("https://www.nearnorthschools.ca/west-ferris/")

    # Grab the source of the page
    src = result.content

    # Parse the text of the latest news
    soup = BeautifulSoup(src, 'html.parser')
    links = soup.find('section', {'id': 'featured-post-2'})
    links = links.find('article')
    links = links.find('a')
    link = links.attrs['href']
    content = links.getText()

    # Open the respective .txt file
    file = open("westFerris/westFerrisWeb.txt", 'r+')

    # Read the only line in the .txt
    file_content = file.readline()

    # If this function was called by the user, print the latest post
    if is_user_call:
        return content + " " + link
    # If this function as called automatically
    else:
        # If the newest news hasn't already been posted
        if file_content != link:
            # Empty the file and write the newest news into it
            file.truncate(0)
            file.write(link)
            file.close()
            # Return the newest post title and the website
            return content + " " + link

        else:
            file.close()
            # Return false so that the program understands to not print anything
            return False

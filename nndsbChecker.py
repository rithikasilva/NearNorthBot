import requests
from bs4 import BeautifulSoup


# This function checks the NNDSB Facebook page for the latest post
def check_facebook(is_user_call):
    # Set the posts face of the NNDSB Facebook page as the source
    result = requests.get("https://www.facebook.com/pg/NearNorthDSB/posts/?ref=page_internal")

    # Grab the source of the page
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
    file = open("nndsb/nndsbFacebook.txt", 'r+')

    # Read the only line of the file into file_content
    file_content = file.readline()

    # If this is a user call, return the latest post
    if is_user_call:
        return content + " https://www.facebook.com/pg/NearNorthDSB/posts/?ref=page_internal"
    # If this is a automatic call
    else:
        # If the post is new
        if file_content != content:
            # Clear the contents of the file and write the content of the post into the file
            file.truncate(0)
            file.write(content)
            file.close()
            # Return the content and the link of the Facebook page
            return content + " https://www.facebook.com/pg/NearNorthDSB/posts/?ref=page_internal"

        else:
            file.close()
            # Return false so that the program understands to not print anything
            return False


# This function checks the NNDSB website for the newest news post
def check_website(is_user_call):
    # Initialize result as the NNDSB website
    result = requests.get("https://www.nearnorthschools.ca/")

    # Grab the source of the page
    src = result.content

    # Parse the content
    soup = BeautifulSoup(src, 'html.parser')

    # Grab the first news item
    first_link = soup.find('div', {'id': 'panel-4216-2-0-0'})
    first_link = first_link.find('a')
    first_link = first_link.attrs['href']

    # Grab the second news item
    second_link = soup.find('div', {'id': 'panel-4216-2-1-0'})
    second_link = second_link.find('a')
    second_link = second_link.attrs['href']

    # Grab the second news item
    third_link = soup.find('div', {'id': 'panel-4216-2-2-0'})
    third_link = third_link.find('a')
    third_link = third_link.attrs['href']

    # Set a list with the new news items
    news_list = [first_link, second_link, third_link]

    # Open the respective .txt file
    file = open("nndsb/nndsbWeb.txt", 'r+')

    # Initialize empty list for file contents
    file_content = []

    # Write file content into file_content
    for x in range(3):
        file_content.append(file.readline())

    # Create new list that has only new news that has't been reported
    file_content = [x[:-1] for x in file_content]
    print_list = set(news_list) ^ set(file_content)
    final_list = set(set(print_list).intersection(news_list))
    final_list = list(final_list)

    # If the user is making the call, return the newest news item
    if is_user_call:
        return news_list[0]

    # If the function call is automatic
    else:
        # If the final_list has new news
        if len(final_list) > 0:
            # Clear the file
            file.truncate(0)
            # Print the three news items that are on display into the file
            for y in range(3):
                file.write(news_list[y] + '\n')
            file.close()

            # Initialize content as blank string
            content = ''
            # Set content as a concatenated string of each element in the final_list
            for z in range(len(final_list)):
                content = content + ' ' + str(final_list[z])
            # Return the content
            return content

        else:
            file.close()
            # Return false so that the program understands to not print anything
            return False

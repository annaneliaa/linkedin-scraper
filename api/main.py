from linkedin_api import Linkedin
import util
import extract
import messaging as msg

"""
This main class serves as a teting script for the LinkedIn API, where the functionality
created in extract.py and messaging.py is tested. These files hold all functions used to
extract data from LinkedIn profiles and send messages to LinkedIn profiles, respectively.
"""
# get credentials from file
credentials = util.get_creds_from_file()

# the profile id of the demo profile used in development
demo_hardcoded_profile_id = "anna-twopointo-329146275"

def create_api(username, password):
    """
    This function creates an API object for LinkedIn using a given username and password.
    
    :param username: The username parameter is a string that represents the username or email address
    associated with the LinkedIn account that will be used to create the API object
    :param password: The password parameter is a string that represents the user's password for their
    LinkedIn account. It is used to authenticate the user and allow them to access the LinkedIn API
    :return: an instance of the `Linkedin` class, which is created using the `username` and `password`
    parameters passed to the function.
    """
    # create api object
    api = Linkedin(username, password)
    return api

# create api object
# login with email and password
api = create_api(credentials.username, credentials.password)

if(api is not None):
    print("logged in!")

# list of test profiles to scrape
profiles = ["annavisman", "ieva-randytė-788956199", "arasaniulis", "kamilė-kaškelytė-7a18381a3"]

# scrape profile
res = api.get_profile(profiles[0])
data = extract.extract_profile_data(res)
extract.print_profile_data(data)

# send message to profile
msg.send_message_to_profile(api, "Hi, this is a testing message", profiles[0])

# get user's unread conversations
msg.get_unread_conversations(api)

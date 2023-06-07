from linkedin_api import Linkedin
import util
import extract
import messaging as msg

path = "/Users/annavisman/stack/RUG/CS/Year2/SE/scraping-demo/linkedin-scraper/pwrd.txt"

"""
This main class serves as a teting script for the LinkedIn API, where the functionality
created in extract.py and messaging.py is tested. These files hold all functions used to
extract data from LinkedIn profiles and send messages to LinkedIn profiles, respectively.
"""
# get credentials from file
credentials = util.get_creds_from_file(path)

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

profile = profiles[0]

# scrape profile
print("Scraping profile '" + profile + "':")
res = api.get_profile(profile)
data = extract.extract_profile_data(res)
data.print_lead()

# get conversation details for input profile
(print("Conversation details for profile '" + profile + "':"))
print(msg.get_conversations_details_by_profile(api, profile))

# get user's unread conversations
print("List of unread conversations:")
print(msg.get_unread_conversations(api))

# send message to profile
msg.send_message_to_profile(api, "Hi, this is a testing message", profile)

# get days since last message
print("Days since last message:")
print(msg.get_days_since_last_message(api, demo_hardcoded_profile_id, profile))

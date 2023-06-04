from linkedin_api import Linkedin
import util
import extract
import messaging as msg

# get credentials from file
credentials = util.get_creds_from_file()

demo_hardcoded_profile_id = "anna-twopointo-329146275"

# create api object
# login with email and password
api = Linkedin(credentials.username, credentials.password)

# list of test profiles to scrape
profiles = ["annavisman", "ieva-randytė-788956199", "arasaniulis", "kamilė-kaškelytė-7a18381a3"]

# scrape profile
#data = extract.extract_profile_data(profile)
#extract.print_profile_data(data)xs

# send message to profile
# msg.send_message_to_profile(api, "Hello, this is a test message", "annavisman")

# get user's unread conversations
# msg.get_unread_conversations(api)

#print(msg.get_conversations_details_by_profile(api, "annavisman").items())
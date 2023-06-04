from linkedin_api import Linkedin
import credentials as cred

# get credentials from file
credentials = cred.get_creds_from_file()

# create api object
# login with email and password
api = Linkedin(credentials.username, credentials.password)

test_dict = {
    "keyword_first_name": "Anna",
    "keyword_last_name": "Visman"
    }

def perform_search(**dict):
    return api.search_people(dict)
    #for key,value in dict.items():
    #    key_value = "{0} : {1}".format(key, value)
    #    print(key_value)


print(perform_search(**test_dict))
    
#result = api.search_people(keyword_first_name="Anna", keyword_last_name="Visman")
#print(result)
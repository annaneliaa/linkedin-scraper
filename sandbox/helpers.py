from linkedin_api import Linkedin

def login(username, password):
    api = Linkedin(username, password)
    if(api is not None):
        return True
    else:
        return False
    

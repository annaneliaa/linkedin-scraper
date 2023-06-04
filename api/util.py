PATH = "/Users/annavisman/stack/RUG/CS/Year2/SE/scraping-demo/linkedin-scraper/pwrd.txt"

from datetime import datetime

class credentials():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        cookies = {}

    def set_cookies(self, li_at, j_session):
        self.cookies = {
            "li_at": li_at,
            "JSESSIONID": j_session
        }
        return self
        
def get_creds_from_file():
    with open(PATH) as f:
        email = f.readline()
        pwrd = f.readline()
        li_at = f.readline()
        j_session = f.readline()
    return credentials(email, pwrd).set_cookies(li_at, j_session)

# function to crop a URN ID from a full URN string
def crop_urn(urn):
    return urn.split(":")[-1]

def convert_unix_time(date):
    t = datetime.utcfromtimestamp(int(date)/1000)
    return t.strftime('%m-%d-%Y %H:%M:%S')
from datetime import datetime

class credentials():
    """
    Class representing user credentials and cookies.
    Used to login to LinkedIn through the API.
    """
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
        
def get_creds_from_file(path):
    """
    This function reads credentials from a file stored on the users PC
    and returns them as a credentials object with cookies
    set.
    
    :param path: The path parameter is a string that represents the file path of the file containing the
    credentials
    :return: an instance of the `credentials` class with the email and password read from the file, and
    the `li_at` and `j_session` cookies set.
    """
    with open(path) as f:
        email = f.readline()
        pwrd = f.readline()
        li_at = f.readline()
        j_session = f.readline()
    return credentials(email, pwrd).set_cookies(li_at, j_session)

def crop_urn(urn):
    """
    This function takes a string URN ID and returns the last part of it after splitting it by
    ":". The last part of the URN ID is the unique identifier of the resource.
    
    :param urn: The input parameter "urn" is a string representing a Uniform Resource Name (URN) which
    is a unique identifier for a resource
    :return: The function `crop_urn` takes a string `urn` as input and returns the last element of the
    string after splitting it by the colon (":").
    """
    return urn.split(":")[-1]

def get_urn_from_profile_id(api, profile_id):
    """
    This function takes an API and a profile ID as inputs, retrieves the profile information using the
    API, and returns the cropped URN of the profile.
    
    :param api: It is likely an instance of a class that provides methods for interacting with the
    LinkedIn API. The specific implementation of this class is not provided in the code snippet
    :param profile_id: The profile ID is a unique identifier for a LinkedIn user's profile. It can be
    found in the URL of the user's profile page. For example, if the URL of the profile page is
    "https://www.linkedin.com/in/john-doe-12345678/", then the profile ID would
    :return: The function `get_urn_from_profile_id` returns the cropped `entityUrn` value from the
    LinkedIn profile of the given `profile_id`.
    """
    profile = api.get_profile(profile_id)
    return crop_urn(profile["entityUrn"])

def convert_unix_time(date):
    """
    The function converts a Unix timestamp to a formatted date and time string.
    
    :param date: The input parameter "date" is a Unix timestamp in milliseconds
    :return: The function `convert_unix_time` takes a Unix timestamp in milliseconds as input and
    returns a formatted string representing the corresponding date and time in the format "MM-DD-YYYY
    HH:MM:SS".
    """
    t = datetime.utcfromtimestamp(int(date)/1000)
    return t.strftime('%m-%d-%Y %H:%M:%S')
# The class `linkedinLead` defines a LinkedIn lead object with attributes such as first name, last
# name, location, education, experience, and languages, and a method to print the lead's information.
class linkedinLead():
    def __init__(self, fName, lName, location, country, headline = None):
        self.fName = fName
        self.lName = lName
        self.headline = headline
        self.education = []
        self.experience = []
        self.location = location
        self.country = country
        self.languages = []

    def print_lead(self):
        """
        The function prints out the personal information, education, work experience, and languages of a
        lead.
        """
        print(self.fName + " " + self.lName)
        print(self.location + ", " + self.country)
        print(self.headline)
        for i in range(len(self.education)):
            print(self.education[i])
        
        for i in range(len(self.experience)):
            print(self.experience[i])

        for i in range(len(self.languages)):
            print(self.languages[i])

def create_lead(fName, lName, location, country, headline = None):
    """
    This function creates a LinkedIn lead to be stored in the database 
    with the given first name, last name, location, country, and
    optional headline.
    
    :param fName: The first name of the lead
    :param lName: The last name of the lead
    :param location: The location parameter is a string that represents the city or region where the
    lead is located
    :param country: The "country" parameter is a string that represents the country of the lead being
    created.
    :param headline: The "headline" parameter is an optional parameter that can be passed to the
    "create_lead" function. It is used to specify a brief description or tagline for the lead being
    created. If no value is provided for this parameter, it will default to None
    :return: a LinkedIn lead object with the provided first name, last name, location, country, and
    optional headline.
    """
    return linkedinLead(fName, lName, location, country, headline)

# public_id is profile name
# input is a dict
# extracts profile information from dict
# returns lead object
def extract_profile_data(profile):
    """
    The function extracts data from a LinkedIn profile and creates a lead object with information such
    as name, location, education, experience, and languages.
    
    :param profile: The "profile" parameter is a dictionary containing information about a LinkedIn
    user's profile, such as their name, location, education, experience, and languages
    :return: The function `extract_profile_data` is returning a lead object.
    """
    # scrape first and last name
    last_name = profile["lastName"]
    first_name = profile["firstName"]

    # scrape location
    location = profile["geoLocationName"]
    country = profile["geoCountryName"]

    # create lead object
    lead = create_lead(first_name, last_name, location, country)

    # scrape headline
    headline = profile["headline"]
    lead.headline = headline

    # scrape education
    education = profile["education"]
    for i in range(len(education)):
        edu = education[i]
        lead.education.append(edu["schoolName"])
        edu.setdefault("fieldOfStudy", None)
        if edu["fieldOfStudy"] != None:
            lead.education.append(edu["fieldOfStudy"])

    # scrape experience
    experience = profile["experience"]
    for i in range(len(experience)):
        # get the company from list of experience
        exp = experience[i]
        # set default value for function (title) if not found
        exp.setdefault("title", None)

        # extract company name and append to list
        job = []
        job.append(exp["companyName"])
        job.append(exp["title"])
        lead.experience.append(tuple(job))

    # scrape languages
    languages = profile["languages"]
    if len(languages) == 0:
        # set default value to empty list for languages if not found
        profile.setdefault("languages", [])
    for i in range(len(languages)):
        lang = languages[i]
        lead.languages.append(lang["name"])

    return lead


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

def create_lead(fName, lName, location, country, headline = None):
    return linkedinLead(fName, lName, location, country, headline)

def print_lead(lead):
    print(lead.fName + " " + lead.lName)
    print(lead.location + ", " + lead.country)
    print(lead.headline)
    for i in range(len(lead.education)):
        print(lead.education[i])
    
    for i in range(len(lead.experience)):
        print(lead.experience[i])

    for i in range(len(lead.languages)):
        print(lead.languages[i])
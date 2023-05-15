from linkedin_api import Linkedin

class linkedinLead():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName
        self.education = []
        self.experience = []

def printLead(lead):
    print(lead.fName + " " + lead.lName)
    for i in range(len(lead.education)):
        print(lead.education[i])
    print("\n")
    for i in range(len(lead.experience)):
        print(lead.experience[i])

with open("pwrd.txt") as f:
    email = f.readline()
    pwrd = f.readline()

profiles = ["annavisman", "ieva-randytė-788956199", "arasaniulis", "kamilė-kaškelytė-7a18381a3"]

api = Linkedin(email, pwrd)

print(api.get_profile("annavisman"))

#geoCountryName
#geoLocationName
#headline

def extractLeads(profiles):
    for i in range(len(profiles)):
        profile = api.get_profile(profiles[i])

        #scrape first and last name
        last_name = profile['lastName']
        first_name = profile['firstName']
        lead = linkedinLead(first_name, last_name)

        #scrape education
        education = profile['education']
        for i in range(len(education)):
            edu = education[i]
            lead.education.append(edu['schoolName'])
            edu.setdefault('fieldOfStudy', None)
            if(edu['fieldOfStudy'] != None):
                lead.education.append(edu['fieldOfStudy'])
        
        #scrape experience
        experience = profile['experience']
        for i in range(len(experience)):
            exp = experience[i]
            lead.experience.append(exp['companyName'])
            exp.setdefault('title', None)
            if(exp['title'] != None):
                lead.experience.append(exp['title'])
                
        printLead(lead)
        print("\n")

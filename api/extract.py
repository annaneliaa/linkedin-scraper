import lead as l

# public_id is profile name
# input is a dict
# extracts profile information from dict
# returns lead object
def extract_profile_data(profile):
    # scrape first and last name
    last_name = profile["lastName"]
    first_name = profile["firstName"]

    # scrape location
    location = profile["geoLocationName"]
    country = profile["geoCountryName"]

    # create lead object
    lead = l.create_lead(first_name, last_name, location, country)

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

def print_profile_data(lead):
    return l.print_lead(lead)


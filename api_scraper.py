from linkedin_api import Linkedin

with open("pwrd.txt") as f:
    email = f.readline()
    pwrd = f.readline()

api = Linkedin(email, pwrd)

profile = api.get_profile('annavisman')
print(profile['lastName'])
education = profile['education']
rug = education[0]
print(rug['degreeName'], "\n", rug['schoolName'])

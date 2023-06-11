from flask import Flask, request
from helpers import *
from linkedin_api import Linkedin
from util import *
from messaging import *
from extract import *

app = Flask("__name__")

# get credentials from file
credentials = get_creds_from_file("pwrd.txt")

email = credentials.username
password = credentials.password
 
self_id = "anna-twopointo-329146275"

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route('/research/login')
def log_in():
    try: 
      api = Linkedin(email, password)
      c = api.get_profile("annavisman")
      data = extract_profile_data(c)
      return data
    except:
        return Exception("Login failed")

@app.route('/research/profile')
def get_profile():
    return "profile"

@app.route('/research/send')
def send_message():
    try: 
      api = Linkedin(email, password)
      profile_urn = get_urn_from_profile_id(api, "annavisman")
      print(profile_urn)
      api.send_message("hello", recipients=[profile_urn])

      return "message sent"
    except:
        return Exception("Send message failed")
 
@app.route('/research/unread')
def unread_conversations():
    try: 
      api = Linkedin(email, password)
      conv_list = get_unread_conversations(api)
      return conv_list
    except:
        return Exception("Retrieving list of unread conversations failed")
if __name__ == '__research__':
        app.run(debug=True)

@app.route('/research/status')
def conversation_status():
    try: 
      api = Linkedin(email, password)
      details = get_conversations_details_by_profile(api, "annavisman")
      return details
    except:
        return Exception("Retrieving conversation status failed")
if __name__ == '__research__':
        app.run(debug=True)

@app.route('/research/days')
def days_last_message():
    try: 
      api = Linkedin(email, password)
      days = get_days_since_last_message(api, self_id, "annavisman")
      return days
    except:
        return Exception("Fetching days since last message failed")
    
if __name__ == '__research__':
        app.run(debug=True)
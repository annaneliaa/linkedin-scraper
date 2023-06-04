from linkedin_api import Linkedin as api
import util

class Message():
    def __init__(self, text, date, sender_urn, name):
        self.text = text
        self.date = date
        self.sender_urn = sender_urn
        self.sender_name = name

def get_urn_from_profile_id(api, profile_id):
    profile = api.get_profile(profile_id)
    return util.crop_urn(profile["entityUrn"])

# get details of a conversation by profile ID
def get_conversations_details_by_profile(api, profile_id):
    profile_urn = util.crop_urn(api.get_profile(profile_id)["entityUrn"])

    # get conversation details
    result = api.get_conversation_details(profile_urn)

    body = result["events"][0]["eventContent"]["com.linkedin.voyager.messaging.event.MessageEvent"]["attributedBody"]["text"]
    date = util.convert_unix_time(result["events"][0]["createdAt"])
    sender = result["events"][0]["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["entityUrn"]
    first_name = result["events"][0]["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["firstName"] 
    last_name = result["events"][0]["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["lastName"]
    name = first_name + " " + last_name

    latest_message = Message(body, date, sender, name)
 
    # create dict of conversation details
    conversation_details = {
        'notification_status': result["notificationStatus"],
        'read': result["read"],
        'total_message_count': result["totalEventCount"],
        'num_unread_messages': result["unreadCount"],
        'last_activitity_at': util.convert_unix_time(result["lastActivityAt"]),
        'starred': result["starred"],
        'latest_message': latest_message.__dict__,
        'connected': not(result["withNonConnection"])
    }
    return conversation_details

# send a message in an existing conversation
def send_message_in_conv(api, message, conv_urn):
    api.send_message(message, conversation_urn_id=conv_urn)

# send message to a profile
def send_message_to_profile(api, message, profile_id):
    profile_urn = get_urn_from_profile_id(api, profile_id)
    api.send_message(message, recipients=[profile_urn])

# get number of unread conversations (not working)
def get_num_unread_conversations(api):
    return api.get_conversations()["metadata"]["unreadCount"]

# get list of unread conversations
# returns list of tuples: conversation URN and profile URN
def get_unread_conversations(api):
    conversations = api.get_conversations()["elements"]
    unread_conversations = []
    for i in range(len(conversations)):
        conv = conversations[i]
        if(conv["unreadCount"] > 0):
            conv_urn = conv["entityUrn"]
            profile_urn = conv["participants"][0]["entityUrn"]
            unread_conversations.append(conv_urn, profile_urn)
    return unread_conversations
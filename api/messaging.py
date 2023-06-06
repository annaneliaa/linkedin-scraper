from linkedin_api import Linkedin as api
import util

class Message():
    """
    Class representing a message in a conversation
    """
    def __init__(self, text, date, sender_urn, name):
        self.text = text
        self.date = date
        self.sender_urn = sender_urn
        self.sender_name = name

def get_invitations(api):
    """
    This function returns a list of invitations using the Linkedin API.
    
    :param api: The "api" parameter is the API object that provides methods for
    interacting with the Linkedin platform.
    :return: The function `get_invitations(api)` is returning the invitations obtained from the API.
    """
    return api.get_invitations()

def get_conversations_details_by_profile(api, profile_id):
    """
    This function retrieves details of a conversation by profile ID.
    
    :param api: This is an object representing the LinkedIn API that is being used to make requests and
    retrieve data
    :param profile_id: The ID of the LinkedIn profile for which you want to retrieve conversation
    details
    """
    profile_urn = util.crop_urn(api.get_profile(profile_id)["entityUrn"])

    # get conversation details
    result = api.get_conversation_details(profile_urn)

    body = result["events"][0]["eventContent"]["com.linkedin.voyager.messaging.event.MessageEvent"]["attributedBody"]["text"]
    date = util.convert_unix_time(result["events"][0]["createdAt"])
    sender = result["events"][0]["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["entityUrn"]
    first_name = result["events"][0]["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["firstName"] 
    last_name = result["events"][0]["from"]["com.linkedin.voyager.messaging.MessagingMember"]["miniProfile"]["lastName"]
    name = first_name + " " + last_name

    # extract latest message and store in Message object
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

def send_message_in_conv(api, message, conv_urn):
    """
    This function sends a message in an existing conversation using the provided API and conversation
    ID.
    
    :param api: The API object that is used to make requests to the messaging platform's API
    :param message: The message that you want to send in the conversation
    :param conv_urn: The conv_urn parameter is the unique identifier URN ID for the conversation in which you
    want to send the message.
    """
    api.send_message(message, conversation_urn_id=conv_urn)

def send_message_to_profile(api, message, profile_id):
    """
    This function sends a message to a LinkedIn profile using the LinkedIn API.
    
    :param api: The LinkedIn API object used to make requests to the LinkedIn API
    :param message: The message that you want to send to the profile
    :param profile_id: The ID of the LinkedIn profile you want to send a message to
    """
    profile_urn = util.get_urn_from_profile_id(api, profile_id)
    api.send_message(message, recipients=[profile_urn])

# returns list of tuples: conversation URN and profile URN
def get_unread_conversations(api):
    """
    This function retrieves a list of unread conversations and returns a list of tuples
    containing the conversation URN and profile URN.
    
    :param api: The "api" parameter is an instance of the LinkedIn API client that has been
    authenticated with valid credentials. It is used to make requests to the LinkedIn API to retrieve
    information about conversations
    :return: The function returns a list of tuples, where each tuple contains
    the conversation URN and profile URN of an unread conversation.
    """
    conversations = api.get_conversations()["elements"]
    unread_conversations = []
    for i in range(len(conversations)):
        conv = conversations[i]
        # if the number of unread conversations is larger than 0, the conversation is unread
        if(conv["unreadCount"] > 0):
            conv_urn = conv["entityUrn"]
            profile_urn = conv["participants"][0]["entityUrn"]
            unread_conversations.append(conv_urn, profile_urn)
    return unread_conversations
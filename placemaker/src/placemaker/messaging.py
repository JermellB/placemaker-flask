from twilio.rest import TwilioRestClient
from settings import NOT_CONFIGURED_MESSAGE, MIDDLEWARE_NOT_USED
from logging import getLogger
logger = getLogger(__name__)

def load_twilio_config():
    #twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    #twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_account_sid = "AC2ae988473e1b1c61a2edd236254d2a97"
    twilio_auth_token = "9f891edb8176ca163c23b059d043dfa9"
    #twilio_number = os.environ.get('TWILIO_NUMBER')
    twilio_number = "+13142070376"

    if not all([twilio_account_sid, twilio_auth_token, twilio_number]):
        logger.error(NOT_CONFIGURED_MESSAGE)
        raise MIDDLEWARE_NOT_USED

    return (twilio_number, twilio_account_sid, twilio_auth_token)


class MessageClient(object):
    def __init__(self):
        (twilio_number, twilio_account_sid,
         twilio_auth_token) = load_twilio_config()

        self.twilio_number = twilio_number
        self.twilio_client = TwilioRestClient(twilio_account_sid,
                                              twilio_auth_token)

    def send_message(self, body, to):
        self.twilio_client.messages.create(body=body, to=to,
                                           from_=self.twilio_number,
                                           # media_url=['https://demo.twilio.com/owl.png'])
                                           )


class TwilioNotificationsMiddleware(object):
    def __init__(self):
        #self.administrators = load_admins_file()
        self.administrators = [dict(name="Joe", phone_number="+19417357382")]
        self.client = MessageClient()

    def process_exception(self, request, exception):
        exception_message = str(exception)
        message_to_send = exception_message

        for admin in self.administrators:
            self.client.send_message(message_to_send, admin['phone_number'])

        logger.info('Administrators notified')

        return None

#test code
if __name__ == '__main__':
    m = TwilioNotificationsMiddleware()
    numlist = [("dan", "+13142070376"), ("allen", "+16506449098"), ("jermell", "+13142559197")]
    for name, num in numlist:
        print("sending message to {}".format(name))
        m.client.send_message("hi {}".format(name), num)
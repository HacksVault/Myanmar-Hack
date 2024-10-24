from twilio.rest import Client
import Keys

client = Client(Keys.account_sid,Keys.auth_token)

message = client.messages.create(
    body= "Hello Guys!",

from_= Keys.twilio_number,
to=Keys.target_number
)

print(message.body)
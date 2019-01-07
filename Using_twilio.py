from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
account_sid = "#####"
auth_token = "#####"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Twilio Test'.",
                     from_='####',       # From Twilio provided Number available on dashboard
                     to='###'   # To Any Number
                 )

print(message.sid)  # Receives a sent ack number
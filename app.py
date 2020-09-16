from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Gmail_To_Whatsapp import check_gmail
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    if msg.lower()=="unseen":
        resp = MessagingResponse()
        resp.message(check_gmail())

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
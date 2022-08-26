from http import server
from flask import *
import smtplib, ssl
import random
from jproperties import Properties


app = Flask(__name__)

otp = {"otp" : ""}

def getCreds():
    configs = Properties()

    with open('config.properties', 'rb') as config_file:
        configs.load(config_file)

    sender_email = str(configs.get("sender_email").data)
    sender_password = str(configs.get("sender_password").data)
    email_server_url = str(configs.get("email_server_url").data)

    creds = {
        "sender_email" : "",
        "sender_password" : "",
        "email_server_url" : ""
    }

    creds["sender_email"] = sender_email
    creds["sender_password"] = sender_password
    creds["email_server_url"] = email_server_url

    return creds


def generate_otp():
    otp = ""
    i = 0
    while i<6:
        otp = otp + str(random.randint(0,9))
        i=i+1
    return otp


def send_otp(sender_email, sender_password, to_email, smtp_server, otp):
    print("**********DEBUG MESSAGE : send_otp() METHOD STARTED**********")
    port = 465
    message = """\
    Subject: OTP

    Your OTP for verification : {otp}""".format(otp=otp)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message)
        print("**********DEBUG MESSAGE : EMAIL SENT SUCCESSFULLY**********")
        return True
    except:
        print("********DEBUG MESSAGE : EMAIL SENDING FAILED********")
        return False


@app.route("/home", methods=["GET", "POST"])
def index():
    server_error_msg = ""
    if request.method == "POST":
        to_email = str(request.form.get("email"))
        otp["otp"] = generate_otp()
        creds = getCreds()
        sender_email = creds["sender_email"]
        sender_password = creds["sender_password"]
        email_server_url = creds["email_server_url"]
        isDone = send_otp(sender_email, sender_password, to_email, email_server_url, otp["otp"])
        if isDone:
            return redirect(url_for("otpVerification"))
        else:
            server_error_msg = "not done"
    return render_template("index.html", server_error_msg=server_error_msg)



@app.route("/otpVerification", methods=["GET", "POST"])
def otpVerification():
    outcome = ""
    if request.method == "POST":
        userOTP = str(request.form.get("otp"))
        if userOTP == otp["otp"]:
            outcome = "true"
        else:
            outcome = "false"
        print(outcome)
    return render_template("otpVerificationPage.html", outcome=outcome)


app.run(debug=True, host="0.0.0.0")
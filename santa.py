import json
import smtplib

from os import getenv
from random import randint
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

json_list_file_name = f"{getenv('FILE_NAME')}.json"
base_email = getenv("BASE_EMAIL")
base_email_pass = getenv("BASE_EMAIL_PASSWORD")


def christmas_day():
    """
    :list_json: JSON file containing list of names and emails.

        The format for the JSON should be as follows:
            {
                <str:name>: <str:email>
            }
    """

    with open(json_list_file_name) as list_json:
        list_dict = json.load(list_json)

    sts_dict = create_sender_to_sendee_dict(list_dict)
    for sender in sts_dict:
        body = f"You have received {sts_dict[sender]} for FANCY Secret Santa!"
        send_santa_email(list_dict[sender], body)


def create_sender_to_sendee_dict(list_dict):
    sts_dict = {}
    unused_names = list(list_dict)
    for name in list_dict:
        santa_name = None
        while santa_name is None or santa_name == name:
            rand_int = randint(0, len(unused_names)) - 1
            santa_name = unused_names[rand_int]
            if len(unused_names) == 1 and unused_names[0] == name:
                print("Resetting")
                return create_sender_to_sendee_dict(list_dict)
            else:
                sts_dict[name] = santa_name
        unused_names.remove(santa_name)
    return sts_dict


def send_santa_email(email_to, email_body):
    email = MIMEMultipart()
    email["From"] = base_email
    email["To"] = email_to
    email["Subject"] = "FANCY Secret Santa"
    email.attach(MIMEText(email_body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(base_email, base_email_pass)
    server.sendmail(base_email, email_to, email.as_string())
    server.quit()


christmas_day()

import requests
import imaplib
import logging
from time import sleep

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_access_token_hotmail(data_hotmail, proxy=None):
    access_token = None
    try:
        post_data = {
            'client_id': data_hotmail.split('|')[3],
            'refresh_token': data_hotmail.split('|')[2],
            'grant_type': 'refresh_token',
        }

        response = requests.post(
            "https://login.microsoftonline.com/common/oauth2/v2.0/token",
            data=post_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            proxies={"http": proxy, "https": proxy} if proxy else None
        )

        response_data = response.json()
        access_token = response_data.get('access_token')

        logging.debug(f"Access token retrieved: {access_token}")

    except Exception as e:
        logging.error(f"Error during first request: {e}")

        try:
            post_data = {
                'client_id': data_hotmail.split('|')[3],
                'refresh_token': data_hotmail.split('|')[2],
                'grant_type': 'refresh_token'
                /IMAP.AccessAsUser.All'  # Request the correct scope
            }

            response = requests.post(
                "https://login.microsoftonline.com/common/oauth2/v2.0/token",
                data=post_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )

            response_data = response.json()
            access_token = response_data.get('access_token')

            logging.debug(f"Access token retrieved on second attempt: {access_token}")

        except Exception as e:
            logging.error(f"Error during second request: {e}")

    return access_token
def generate_auth_string(user, token):
    auth_string = f"user={user}\1auth=Bearer {token}\1\1"
    return auth_string

def get_code_hotmail_oauth2(data_hotmail, access_token):
    code = None
    try:
        email_address = data_hotmail.split('|')[0]
        
        # Kết nối đến máy chủ IMAP và bật chế độ debug
        mailbox = imaplib.IMAP4_SSL("outlook.office365.com")
        mailbox.debug = 4  # Enable debugging for the IMAP connection

        result, response = mailbox.authenticate("XOAUTH2", lambda x: generate_auth_string(email_address, access_token))

        logging.debug(f"Authenticated as {email_address}")

        # Lấy danh sách các hộp thư
        mailbox.select("inbox")

        # Lấy thông tin email
        result, data = mailbox.search(None, 'ALL')
        mail_ids = data[0].split()
        
        logging.debug(f"Mail IDs: {mail_ids}")

        # Giới hạn lấy tối đa 20 email
        for i in range(min(20, len(mail_ids))):
            mail_id = mail_ids[-(i + 1)]
            result, msg_data = mailbox.fetch(mail_id, '(RFC822)')
            raw_email = msg_data[0][1]


        if not code:
            sleep(1)

        mailbox.logout()
        logging.debug("Logged out successfully.")

    except Exception as e:
        logging.error(f"Error during mail fetch: {e}")

    return code

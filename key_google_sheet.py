#pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
def check_lisence(self):
    uuid = self.get_uuid()
    serial = self.get_serial()
    name = self.get_hostname()
    key = self.generate_sha256_hash(f"{uuid}{serial}{name}")
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_INFO = {
        "type": "service_account",
        "project_id": "bet11-360217",
        "private_key_id": "570ddf3e8c95d91f3e01e74ffc9914ec40134aaf",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCP9Ktz3hCl4Aii\nmNKHO1SJMXvgyB35P1CrdH7u0/AYNfLKNPAuPeh+btPrqc+UCZ5BCO1pc7e/KhLH\nU40Tnk0HKLo63rDSYSo50VT12hLm2xIJ9ktB1KGiJKI6/VPZRvjuXuW0hzauFfHu\nXDT26RLk+ysCy5kkUQJ5S/qEMkYdKGRUTwUHOzeoSeY6QIXScHW+UHA+eJ1dAY75\nWTHVL0G3ybT5LPR2rK7f6RxIlO0Lrv1keGhLQtZ84idOlXys7auVx/kahppPV8T9\n2KDTZ0sTzEwmzM64racE51yUD//EDhzESAbD9wONG+hfRYhOIRnJJFJEjeUOLSAk\n2KHoyjwpAgMBAAECggEACiXpYEWrTsY4VZ4IWVgpYXKHlRUGZ+e6vBt+Rz/RkSNc\ndjy9IcVjemY9skNKStlSuqrycZiiv2sr37lYHKXwMC0C09uXA32uCF1la99vra6L\n2v/t1jozGscSWK47FvoV2lf+QXe2txb88xy07yMHHfVG1u+bYCAF2J8ujdstbiir\nt8gb+LDM+lXbgIkjMZs+bY5mSJGecickLeYCLHBA1hvOFZZ550BZL1v/sdBlSUFQ\nmuEQaC0FJCenbQel2iFse2/SdYK2AZXq6dwUW2drSt8eVEV/gkm1tHWU90XvUKsf\njktns/Lk5MR7unSZKC17dMxjgyFWzqvwr6A6D5918QKBgQDDpF7xEn7IZ5KMFqO0\nb8qLcycphoTrfff4Z60HIk7uxIqExInAcAamHeipFAlJRHOZcGkyWUKm3OFuMPPs\nr0JyqG7VqW4AYedzFdjUPAT/XlM6x9eH6BPiHC8vcUS8YYfsXfwx/3bXxeXfXff5\nbd8lDZrm5dufd9V0KVZ1wFYTDwKBgQC8XikN7WEGPa1/duponen1VN4lwCiAPEMW\nLc+gQbPspBWCIxi0CoNu885pIXqfebvXa28APQ8vVpghQEJRKrPxgn+ZgTYbWgyN\nUceZpEB0ztQY8M9jMoAPCjoz9aOqv7OdJhOk7ZUuPCnRNZfUprSRFmt66WYj5YoF\nVFZqOhndRwKBgFNrOrA/2p9IykvBO3wsToi3SPOD0Bk5VQot6rEoB8/3Lbj+tF3B\nZpReHF47lNoQvdmm/LPjK3BKrjR12wwIjqSk/N1NqQGwvSdtIU8daGQarBJcM6JX\namL28YehHFXWoEZArNAExX+reiCLyLgqCQObkXjyeXq9dd5Z4evDXvAxAoGAEq9w\neR40Aq95l2xPYmNPwvNROgNuwRG5Qej3cJkz5OR98bPTjoCAezAaKJmWlV05Aex5\nTVfBOtvnKV07dtu6j9l3GN4VZO8w0Y/sMdR2RGAD8BlrKRboVxWXonHac2Six5Lw\nXernYne7WjJrxj9nKAFGViHy7NqnL1InZFAxIp8CgYAfyb1ArvkqFwH7ymoobs6w\nwW6W4SAAb3OxZZjHl46MbjMomPsiY0QRyKLsd0u/fCZpBGDNGBJi59cm0e0XYNY0\nrcBaMHkIPMhE3cl0wz9BWl541BvOAZJt1b4B1UcPtwKb1VRTvIFhuCEBJEYWUDua\nPs7YHsrvm8ZS7uh4l+xIPw==\n-----END PRIVATE KEY-----\n",
        "client_email": "bet188-danh@bet11-360217.iam.gserviceaccount.com",
        "client_id": "111248329424756769057",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bet188-danh%40bet11-360217.iam.gserviceaccount.com"
    }
    credentials = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = '1oiDq7OXTb6-Ya6C_mb7K1hNyAoEd5ZNM35cCUaEYD7Y' #key reg shopee
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range="Key").execute()
    values = result.get('values', [])
    for row in values:
        try:
            name = row[0]
            key_check = row[1]
            date_check = row[2]
            print(key_check)
            if key == key_check:
                return name, date_check
        except:
            pass
    return False, key

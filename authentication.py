import pyrebase

config = {
    'apiKey': "AIzaSyBA9qS60QyXhrdYXsyk8MLan4pNgnPfMjo",
    'authDomain': "dicegame-a8c5b.firebaseapp.com",
    'projectId': "dicegame-a8c5b",
    'storageBucket': "dicegame-a8c5b.appspot.com",
    'messagingSenderId': "17795767024",
    'appId': "1:17795767024:web:d1da35cf106eef5b640035",
    'measurementId': "G-MS3VJ2HC6R",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)


# GET USER INFO
# info = auth.get_account_info(user['idToken'])
# print(info)

# SEND EMAIL VERIFICATION
# auth.send_email_verification(user['idToken'])

# RESET PASSWORD
# auth.send_password_reset_email(email)
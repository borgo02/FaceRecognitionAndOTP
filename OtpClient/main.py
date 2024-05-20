import datetime
import pyotp
import time

secret_base32 = 'thisisoursecretkey'

totp = pyotp.TOTP(secret_base32)
url = pyotp.totp.TOTP(secret_base32).provisioning_uri(name='test@account.it', issuer_name='Esame Architetture')
print(url)
while True:
    current_value = totp.now() # => '492039'

    # OTP verified for current time
    current_result = totp.verify(current_value) # => True
    time_remaining = totp.interval - datetime.datetime.now().timestamp() % totp.interval
    print(current_value)
    print(current_result)
    print(time_remaining)
    time.sleep(30)
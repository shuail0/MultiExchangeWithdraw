from hashlib import sha256
import hmac

def get_sign(key, data):

    #sha256加密有2种
    # hsobj = sha256(key.encode("utf-8"))
    # hsobj.update(data.encode("utf-8"))
    # print(hsobj.hexdigest().upper())

    data = data.encode('utf-8')
    print(hmac.new(key.encode('utf-8'), data, digestmod=sha256).hexdigest().upper())

key='1546084445901'
data='testappSecret'
# get_sign(key,data)
get_sign(data,key)

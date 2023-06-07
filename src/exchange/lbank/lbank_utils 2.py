import base64
import hashlib
from cryptography.hazmat.primitives import serialization
from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from hashlib import sha256
import hmac

def prepare_parameters(api_key, signature_method, timestamp, echostr, **kwargs):
    """
    根据提供的参数生成待签名字符串。
    """
    params = {
        'api_key': api_key,
        'signature_method': signature_method,
        'timestamp': timestamp,
        'echostr': echostr,
        **kwargs
    }

    sorted_params = sorted(params.items())
    prepared_str = '&'.join([f"{k}={v}" for k, v in sorted_params])

    return prepared_str

def md5_digest(prepared_str):
    """
    生成MD5摘要并将所有字符转换成大写。
    """
    md5 = hashlib.md5(prepared_str.encode('utf-8'))
    return md5.hexdigest().upper()

def rsa_sign(prepared_str, secret_key):
    """
    使用RSA和私钥对准备好的字符串进行签名。

    参数:
        prepared_str (str): 准备好的字符串
        secret_key (str): Base64编码的私钥
    返回:
        str: 签名后的字符串
    """
    data = prepared_str.encode('utf-8')
    secret_key = base64.b64decode(secret_key)
    print(hmac.new(secret_key.encode('utf-8'), data, digestmod=sha256).hexdigest().upper())


# 使用示例
api_key = "23fa76ae-81d9-4b27-a29a-328b6bf3aa14"
signature_method = "RSA"
timestamp = "1585119477235"
echostr = "P3LHfw6tUIYWc8R2VQNy0ilKmdg5pjhbxC7"
secret_key = "MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBALgpScLVqK7OH8+qmRMlyPiCO1vPoCfEn9a9NqLgzyw3JYdfwnJfCQ9dCQ3VOd4PT9xCqMdROg1Dc+s69nmub6m5Xlh32vuFIDq8cGZ2fv/LC3IpYNKl46rO1q5RGMCKAe9IL4AVQNBbE7pX0QzsHccsDOSLMlfkvxPOUNf3AxAJAgMBAAECgYEAqHV0OJpTJBv/M2o9fitpLBGNFM3XFamiAL+yc8mrGSoU1UF+UDqowfn7p0CuH3foOHZth23A6ZMTPVEBV4t+Lbg4VEvt9b2AkfH7/0LKc0ec3/mFjneXMak7BOUPPTh2v64nu++oDLgjNDqwMNAmYhcyxUWEcFoG829J9kGI9pECQQDlxEVTKT1UWfW8w1LvoTtJa1w5Tgws2zgMgTpy0QP1zGYZp6uOjblS95IYU+sktz9aGDvPF7o4sUu0nRaerkblAkEAzTAKhleSoJP8IMaAJaDreye5kdAU86BJQAF2wTHVRWRz96Nv8AsnmYFf3nuinL95u/XCRAHkNgwTaQrmsOEOVQJBAKw3msakaIWrEBe2R5m5PdjgEbYaG+IbRj2JNygMJm28EOM1287zx266hdSaQeu5NlDvTRUCceBAc8Ai5mt1sUkCQQCXPI61YHzZ0NmoisbPdWG735bey8F1pLH49FtEoOdyg00avSN3ibFBauNvyC8eW99tVAJBQCemUpZH+Vn6C5gVAkBr4shqnLqP1Z/FwdXOV8WCOvAB9/AChlcSzKLYvPPSmIKQkdaVMVw4U29SJE8I7v8TY0NEkOxqbEa6vrijKlp1"

parameters = prepare_parameters(api_key, signature_method, timestamp, echostr)
prepared_str = md5_digest(parameters)
def get_private_key(key: str):
    try:
        # 将Base64编码的私钥字符串解码为字节数组
        decoded_key = base64.b64decode(key)
        print(decoded_key)
        # exit()

        # 从字节数组中加载私钥
        private_key = serialization.load_pem_private_key(
            decoded_key,
            password=None,
            backend=default_backend()
        )
        print(private_key)
        exit()
        return private_key
    except Exception as e:
        print(e)
        return None

# 示例：使用私钥字符串调用get_private_key函数
private_key_str = secret_key
private_key = get_private_key(private_key_str)
print(private_key)
exit()

# exit()
sign = rsa_sign(prepared_str, secret_key)

print("Parameters:", parameters)
print("Prepared string (MD5 digest):", prepared_str)
print("Sign:", sign)

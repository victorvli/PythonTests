# -*- coding: utf-8 -*-
import base64
from Crypto.Cipher import AES

AES_SECRET_KEY = 'AesSecretKeyTest'  # 此处16|24|32个字符
IV = "1234567890123456"

# padding算法
BS = len(AES_SECRET_KEY)


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def un_pad(s):
    return s[0:-ord(s[-1:])]


def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


class AESCoder(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    # 加密函数
    def encrypt(self, text):
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(ciphertext)

    # 解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return un_pad(plain_text)

    def decrypt_url_safe(self, text):
        text = text.replace('-', '+').replace('_', '/')
        return self.decrypt(text)


if __name__ == '__main__':
    aes_encrypt = AESCoder()
    my_email = "csc25005"
    e = aes_encrypt.encrypt(my_email)
    d = aes_encrypt.decrypt(e)
    print(my_email)
    print(e)
    print(d)
    print(aes_encrypt.decrypt_url_safe("-pRqGPwfH0yuKC05JQlCMQ=="))

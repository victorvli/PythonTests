from cipher_test import AESCoder

if __name__ == '__main__':
    aes_encrypt = AESCoder()
    my_email = "Hello World"
    e = aes_encrypt.encrypt(my_email)
    d = aes_encrypt.decrypt(e)
    print(my_email)
    print(e)
    print(d)
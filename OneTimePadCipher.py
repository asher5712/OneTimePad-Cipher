import random
import string
import pandas as pd


class OTPCipher:
    def __init__(self):
        self.encrypted_text = ''
        self.encrypted_key = ''

        def df_generator():
            lst = []
            st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            while True:
                lst_len = len(lst)
                if lst_len == 0:
                    letters = ""
                else:
                    letters = st[:lst_len]
                st1 = st[lst_len:] + letters
                lst.append(st1)
                if lst_len == 25:
                    break
            final_lst = []
            for st in lst:
                ls = [c for c in st]
                final_lst.append(ls)
            return final_lst

        self.df = pd.DataFrame(data=df_generator(), columns=df_generator()[0], index=df_generator()[0])

    def __str__(self):
        if self.encrypted_text == '' or self.encrypted_key == '':
            self.cipher_encrypter()
        return f"Encrypted Text= {self.encrypted_text}\nEncrypted Key={self.encrypted_key}"

    def cipher_encrypter(self):
        def encrypt(message):
            def random_key_generator(key_len):
                random_key = ''.join(random.choices(string.ascii_uppercase, k=key_len))
                return random_key

            cipher_word_list = []
            key_word_list = []
            for token in message.upper().split():
                alp = [x.upper() for x in token.strip()]
                key = [x for x in random_key_generator(len(token.strip()))]
                cipher = []
                for a, k in zip(alp, key):
                    cipher.append(self.df.loc[k, a])
                cipher_word_list.append(''.join(cipher))
                key_word_list.append(''.join(key))

            return dict(cipher='@'.join(cipher_word_list), key='@'.join(key_word_list))

        my_message = input('Enter your message: ')
        d = encrypt(my_message)
        self.encrypted_text = d['cipher']
        self.encrypted_key = d['key']
        return {'Cipher': d['cipher'], 'Key': d['key']}

    def cipher_decrypter(self):
        def decrypt(cipher, key):
            cipher_word_list = cipher.split('@')
            key_word_list = key.split('@')
            for i in range(len(cipher_word_list)):
                if len(cipher_word_list[i]) != len(key_word_list[i]):
                    print('Error!')
                    break
                else:
                    word_list = []
                    for cipherN, keyN in zip(cipher_word_list, key_word_list):
                        c_lst = [x for x in cipherN]
                        k_lst = [x for x in keyN]
                        t_char = []
                        for c, k in zip(c_lst, k_lst):
                            for t in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                                if self.df.loc[k, t] == c:
                                    t_char.append(t)
                                    break
                        word = ''.join(t_char)
                        word_list.append(word)
                    return ' '.join(word_list)

        my_cipher = input('Enter the cipher: ')
        my_key = input('Enter the key: ')
        return {'Message': decrypt(my_cipher, my_key)}

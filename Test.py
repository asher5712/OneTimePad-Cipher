import OneTimePadCipher as cipher

coder = cipher.OTPCipher()
print('----------------Message Encryption----------------')
my_dict = coder.cipher_encrypter()
print('Cipher:', my_dict['Cipher'])
print('Key:', my_dict['Key'], end='\n\n')

print('----------------Message Decryption----------------')
my_str = coder.cipher_decrypter()
print('Message:', my_str['Message'], end='\n\n')
print('--------------------------------------------------')

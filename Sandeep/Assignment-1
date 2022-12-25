# 1) Caesar Cipher
#encrypter
alphabet="abcdefghijklmnopqrstuvwxyz"
caesercipher= ""
message= input("Please enter you message:")   
shift=int(input("Please enter the character shift value for alphabet: numerical value only. "))
for character in message.lower():
    if character in alphabet:
        index=alphabet.find(character)
        newindex= (index + shift)%26
        newletter= alphabet[newindex]
        caesercipher += newletter
    else:
        caesercipher+= character
print(caesercipher)

#decrypter
alphabet="abcdefghijklmnopqrstuvwxyz"
decipher_caesercipher=""
message= input("Please enter you message:")
shift=int(input("Please enter the character shift value for alphabet: numerical value only. "))
for character in message:
    if character in alphabet:
        index=alphabet.find(character)
        newindex= (index - shift)%26
        newletter= alphabet[newindex]
        decipher_caesercipher= decipher_caesercipher+newletter
    else:
        decipher_caesercipher=decipher_caesercipher+character
print(decipher_caesercipher)

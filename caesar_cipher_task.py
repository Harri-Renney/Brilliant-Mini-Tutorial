def encode(message, shift):
    cipher = ""
    for i in range(len(message)):
        cipher += chr(ord(message[i]) + shift)
        
    return cipher
        
def decode(message, shift):
    plaintext = ""
    for i in range(len(message)):
        plaintext += chr(ord(message[i]) - shift)
        
    return plaintext
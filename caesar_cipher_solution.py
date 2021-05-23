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

message = "Hello there."
print("Custom message: " + message)

cipherMessage = encode(message, 5)
    
print("Cipher message: " + cipherMessage)
decodedMessage = decode(cipherMessage, 5)
    
print("Decoded message: " + decodedMessage)
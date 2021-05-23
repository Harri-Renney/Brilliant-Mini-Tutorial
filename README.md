# Brilliant-Mini-Tutorial

This repository contains the complementary code and instructions to facilitate the brilliant mini tutorial.

## Python

Python is a scripting language with an accessible programming syntax and powerful library of tools. It is regularly used in the fields of artificial intelligence and cyber security. Python files are saved in files ending in ".py"

## Files

* caesar_cipher_task.py - Contains the encode and decode functions for use in this tutorial.
* caesar_cipher_solution.py - A fully working example that demonstrates the use of the encode and decode functions.

## Instructions

For this lesson, you will use some existing code to encode and decode text using a caesar cipher. 

1. Open up this [online python compiler](https://www.programiz.com/python-programming/online-compiler/) to run your code.
2. Copy the code from the file "caesar_cipher_task.py" into the online python compiler.
3. Create a plain text message and print it so we can see our message clearly:

```
message = "Hello Rachel"
print("Custom message: " + message)
```

4. Now you have two python functions available called encode and decode we pasted in step 2. Use these functions to encode a message of your choice by adding:

```
cipherMessage = encode(message, 10)
print("Cipher message: " + cipherMessage)
```

5. Now you can see your cipher text printed. Let's decode this message and print the message, we should see our original message once more:

```
decodedMessage = decode(cipherMessage, 10)
print("Decoded message: " + decodedMessage)
```

### Bonus Task

Find a friend and agree upon a caesar shifting value (This is the number entered into the encode() and decode() functions). One of you create a custom message for your friend, encode it using the encode() function with the agreed on
shift value. Send this message to your friend. Your friend can then use the decode() function with the same shift value to decrypt the message and see what you have to say!
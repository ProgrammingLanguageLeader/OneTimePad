# One Time Pad

This is a set of scripts that enables you to encrypt / decrypt files using one of the most durable cryptographic ciphers  

## Requirements
Python 3.6 or higher must be installed on your machine

## How to use

### Secure key generation

To be sure that your encrypted files won't be cracked by some nosy person it's very important to use strong keys

The script _**generate_key.py**_ uses crypto persistent pseudo-random number generator and creates qualitative key  

Here is an example (it will generate 16 MB key and record it to the file "key.bin"):
```bash
python3 generate_key.py 16MB key.bin
```

### Files encryption and decryption

One Time Pad is a symmetric cipher, so encryption and decryption keys are the same

Moreover, due to using bitwise XOR (exclusive "OR") operation when encrypting files, 
repeated encryption with the same key will provide an original file!

That's why encryption and decryption is done with the same command

Here is an example (encryption of the file "plain.docx" with key from file "key.bin" and output file "encrypted.bin"):
```bash
python3 cipher.py key.bin plain.docx encrypted.bin
```

### Getting help
```bash
python3 cipher.py -h
python3 generate_key.py -h
```

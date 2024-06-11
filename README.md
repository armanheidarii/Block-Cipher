<p align="center">
<img alt = "Block Cipher Image"
    src="https://imgs.search.brave.com/q-Pt0EhgNWnFfgFNgPyyLwGFON2k9pP0GqsFzY1fpoE/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/dHV0b3JpYWxzcG9p/bnQuY29tL2NyeXB0/b2dyYXBoeS9pbWFn/ZXMvYmxvY2tfY2lw/aGVyLmpwZw">
</p>


## Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Test](#Test)
- [Description](#description)

## Introduction
A block cipher is a method of encrypting data in blocks to produce ciphertext using a cryptographic key and algorithm. The block cipher processes fixed-size blocks simultaneously, as opposed to a stream cipher, which encrypts data one bit at a time. Most modern block ciphers are designed to encrypt data in fixed-size blocks of either 64 or 128 bits.

### How Block Ciphers Work

A block cipher takes a block of plaintext bits and generates a block of ciphertext bits, generally of the same size. The size of the block is fixed in the given scheme. The choice of block size does not directly affect the strength of the encryption scheme. The strength of the cipher depends on the key length.

### Block Cipher Modes of Operation

There are several modes of operation for block ciphers, each with its own characteristics:
+ Electronic Codebook (ECB): A simple mode where each block of plaintext is encrypted independently, without any chaining or feedback.
+ Cipher Block Chaining (CBC): The most common mode, where each block of plaintext is XORed with the previous block of ciphertext before encryption.
+ Counter (CTR): A mode where a counter is used to generate a unique initialization vector (IV) for each block of plaintext.


## Usage
```bash
python main.py
```

## Test
```bash
python tests/test.py
```

## Description
The implemented hash algorithm is composed of several layers of abstraction:

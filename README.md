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
The designed block encryption algorithm takes 64-bit plaintext and 128-bit key as input, and produces 64-bit ciphertext as output. The general structure of the algorithm is as follows:
<p align="center">
<img alt = "Block Cipher Image"
    src="https://drive.google.com/uc?export=view&id=1ZBBFRfeDk9gTQ_VGUEaDxPCeBuZvcoWT">
</p>

### Round
As shown in the figure, this algorithm has 8 main **Round**s and a final **Output Transformation** round. In each round, the 64-bit input is received as 4 16-bit data blocks, and 6 16-bit subkeys are used in each round. The structure of each Round is as follows:

Step 1: Multiply p1 and K1<br />
Step 2: Add p2 and K2<br />
Step 3: Add p3 and K3<br />
Step 4: Add p4 and K4<br />
Step 5: XOR Step1 and Step3<br />
Step 6: XOR Step2 and Step4<br />
Step 7: Multiply Step5 and K5<br />
Step 8: Add Step6 and Step7<br />
Step 9: Multiply Step8 and K6<br />
Step 10: Add Step7 and Step9<br />
Step 11: XOR Step1 and Step9 (p1)<br />
Step 12: XOR Step3 and Step9 (p2)<br />
Step 13: XOR Step2 and Step10 (p3)<br />
Step 14: XOR Step4 and Step10 (p4)<br />

+ The three main operations of this algorithm are XOR, addition modulo 2<sup>16</sup>, and multiplication modulo 2<sup>16</sup>.
+ The values of step 11, step 12, step 13, and step 14 are equivalent to p1, p2, p3, p4 of the next Round, respectively.

### Output Transformation
The final round of this algorithm also receives 4 16-bit data blocks and uses 4 16-bit subkeys to ultimately construct the final ciphertext. The structure of Output Transformation is as follows:

<p align="center">
<img alt = "Block Cipher Image"
    src="https://drive.google.com/uc?export=view&id=1dPnm-63SGeUR_lbBTvYpOA_lyR2tlWfY">
</p>

### Modes of Operation
For the integration of blocks and the conversion of multi-block plaintext to ciphertext, this algorithm uses the following mode operations:

+ Cipher Block Chaining (CBC)
<p align="center">
<img alt = "Block Cipher Image"
    src="https://drive.google.com/uc?export=view&id=1T8tQ7k5RmngL1RGqctE6GlOgKenKLsPV">
</p>

+ Counter (CTR)
<p align="center">
<img alt = "Block Cipher Image"
    src="https://drive.google.com/uc?export=view&id=1cC-y_ixISnbPhGK139nCbG7nr50qDAw2">
</p>

By default, the algorithm operates in ECB (Electronic Codebook) mode.

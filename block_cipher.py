import binascii
import random


class BlockCipher:
    key_length = 128
    block_length = 64

    def __init__(self):
        pass

    def get_binary(hex_string):
        hex_string = binascii.hexlify(hex_string)
        return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

    def get_hex(binary_string):
        return hex(int(binary_string, 2))

    def rotate(string, n):
        return string[n:] + string[:n]

    def multiply(p, k, size=16, mod=2**16 + 1):
        multiplication = int(p, 2) * int(k, 2)
        return bin(multiplication % mod)[2:].zfill(size)

    def add(p, k, size=16, mod=2**16):
        addition = int(p, 2) + int(k, 2)
        return bin(addition % mod)[2:].zfill(size)

    def xor(p, k, size=16):
        p = p.zfill(size)
        k = k.zfill(size)

        ans = ""
        n = len(p)
        for i in range(n):

            if p[i] == k[i]:
                ans += "0"
            else:
                ans += "1"
        return ans

    def chunk(text, length, size=0):
        max_size = len(text) // length
        if size == 0 or size > max_size:
            size = max_size

        ans = [text[length * i : length * i + length] for i in range(size)]

        last_index = size * length
        if size == 0 and last_index < len(text):
            ans.append(text[last_index:])

        return ans

    def keygen(key):
        sub_keys = []
        for i in range(7):
            sub_keys.extend(BlockCipher.chunk(key, 16))
            key = BlockCipher.rotate(key, 25)
        return sub_keys

    def round_calculation(p, k):
        step1 = BlockCipher.multiply(p[0], k[0])
        step2 = BlockCipher.add(p[1], k[1])
        step3 = BlockCipher.add(p[2], k[2])
        step4 = BlockCipher.add(p[3], k[3])
        step5 = BlockCipher.xor(step1, step3)
        step6 = BlockCipher.xor(step2, step4)
        step7 = BlockCipher.multiply(step5, k[4])
        step8 = BlockCipher.add(step6, step7)
        step9 = BlockCipher.multiply(step8, k[5])
        step10 = BlockCipher.add(step7, step9)
        step11 = BlockCipher.xor(step1, step9)
        step12 = BlockCipher.xor(step3, step9)
        step13 = BlockCipher.xor(step2, step10)
        step14 = BlockCipher.xor(step4, step10)
        return [step11, step12, step13, step14]

    def output_transformation(p, k):
        step1 = BlockCipher.multiply(p[0], k[0])
        step2 = BlockCipher.add(p[1], k[1])
        step3 = BlockCipher.add(p[2], k[2])
        step4 = BlockCipher.multiply(p[3], k[3])
        return [step1, step2, step3, step4]

    def encrypt_block(plaintext, key):
        sub_keys = BlockCipher.keygen(key)

        ciphertext = BlockCipher.chunk(plaintext, 16)
        for i in range(8):
            ciphertext = BlockCipher.round_calculation(
                ciphertext, sub_keys[6 * i : 6 * i + 6]
            )

        ciphertext = BlockCipher.output_transformation(ciphertext, sub_keys[48:52])

        return "".join(ciphertext)

    def padding(block):
        block += "1"
        for i in range(BlockCipher.block_length - len(block)):
            block += "0"
        return block

    def generate_IV(n):
        key1 = ""

        for i in range(n):
            temp = str(random.randint(0, 1))
            key1 += temp

        return key1

    def encrypt_EBC(blocks, key):
        cipher_blocks = []

        for block in blocks:
            cipher_blocks.append(BlockCipher.encrypt_block(block, key))

        return "".join(cipher_blocks)

    def encrypt_CBC(blocks, key):
        iv = BlockCipher.generate_IV(BlockCipher.block_length)

        cipher_blocks = []

        ciphertext = iv
        for block in blocks:
            ciphertext = BlockCipher.encrypt_block(
                BlockCipher.xor(ciphertext, block), key
            )
            cipher_blocks.append(ciphertext)

        return "".join(cipher_blocks)

    def encrypt_CTR(blocks, key):
        iv = BlockCipher.generate_IV(BlockCipher.block_length)

        cipher_blocks = []

        for i in range(len(blocks)):
            cipher_blocks.append(
                BlockCipher.xor(
                    BlockCipher.encrypt_block(
                        BlockCipher.add(iv, f"{i}", size=64, mod=2**64), key
                    ),
                    blocks[i],
                )
            )

        return "".join(cipher_blocks)

    def encrypt(plaintext, key, mode="ECB"):
        plaintext = BlockCipher.get_binary(plaintext)
        key = BlockCipher.get_binary(key)

        blocks = BlockCipher.chunk(plaintext, BlockCipher.block_length)

        last_blocks_index = len(blocks) - 1
        if len(blocks[last_blocks_index]) < BlockCipher.block_length:
            blocks[last_blocks_index] = BlockCipher.padding(blocks[last_blocks_index])

        if mode == "ECB":
            return BlockCipher.encrypt_EBC(blocks, key)

        if mode == "CBC":
            return BlockCipher.encrypt_CBC(blocks, key)

        if mode == "CTR":
            return BlockCipher.encrypt_CTR(blocks, key)


plaintext = b"\x00\x11\x22\x33\x44\x55\x66\x77"
key = b"\x81\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x18"

print(BlockCipher.encrypt(plaintext, key))
print(BlockCipher.get_binary(b"2\x0b\x92\xedNe \x90"))

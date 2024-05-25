import binascii


class BlockCipher:
    def __init__(self, plaintext, key):
        pass

    def get_binary(plaintext):
        hex_string = binascii.hexlify(plaintext)
        return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

    def rotate(string, n):
        return string[n:] + string[:n]

    def multiply(p, k):
        multiplication = int(p, 2) * int(k, 2)
        return bin(multiplication % (2**16 + 1))[2:].zfill(16)

    def add(p, k):
        addition = int(p, 2) + int(k, 2)
        return bin(addition % (2**16))[2:].zfill(16)

    def xor(p, k):
        p = p.zfill(16)
        k = k.zfill(16)

        ans = ""
        n = len(p)
        for i in range(n):

            if p[i] == k[i]:
                ans += "0"
            else:
                ans += "1"
        return ans

    def chunk(text, size, length):
        return [text[length * i : length * i + length] for i in range(size)]

    def keygen(key):
        sub_keys = []
        for i in range(7):
            sub_keys.extend(BlockCipher.chunk(key, 8, 16))
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

    def encrypt(plaintext, key):
        plaintext = BlockCipher.get_binary(plaintext)
        key = BlockCipher.get_binary(key)

        if len(key) != 128 or len(plaintext) != 64:
            return None

        sub_keys = BlockCipher.keygen(key)

        ciphertext = BlockCipher.chunk(plaintext, 4, 16)
        for i in range(8):
            ciphertext = BlockCipher.round_calculation(
                ciphertext, sub_keys[6 * i : 6 * i + 6]
            )

        ciphertext = BlockCipher.output_transformation(ciphertext, sub_keys[48:52])

        return "".join(ciphertext)


plaintext = b"\x00\x11\x22\x33\x44\x55\x66\x77"
key = b"\x81\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x18"

print(BlockCipher.encrypt(plaintext, key))
print(BlockCipher.get_binary(b"2\x0b\x92\xedNe \x90"))

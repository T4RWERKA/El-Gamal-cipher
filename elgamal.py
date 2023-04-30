import importlib, num_algs
importlib.reload(num_algs)


headers = {
    "jpg": (0, 255),
    "jpeg": (0, 255),
    "png": (0, 137),
    "gif": (0, 71),
    "bmp": (0, 66),
    "doc": (0, 208),
    "docx": (0, 80),
    "pdf": (0, 37),
    "mp3": (0, 255),
    "wav": (0, 82),
    "avi": (0, 82),
    "mp4": (4, 102),
    "zip": (0, 80),
    "rar": (0, 82),
    "tar": (257, 117),
    "sqlite": (0, 83),
    "mysql": (0, 67),
    "postgresql": (0, 0)
}


def encrypt(M: int, p: int, g: int, y: int, k: int) -> tuple[int, int]:
    a = num_algs.pow_mod(g, k, p)
    b = num_algs.pow_mod(y, k, p) * M % p
    return a, b


def decrypt(a: int, b: int, x: int, p: int) -> int:
    return num_algs.pow_mod(a, p - 1 - x, p) * b % p


def break_cipher(cipher_text, extension, y, g, mod):
    result = []
    if len(cipher_text[::2]) < 1 or len(cipher_text[::2]) == cipher_text[::2].count(cipher_text[0]) and \
            extension in headers:
        known_encrypted_byte = cipher_text[1::2][headers[extension][0]]
        known_plain_byte = headers[extension][1]
        inv = number_algorithms.pow_mod(known_encrypted_byte, mod - 2, mod)
        print(f"m = {known_plain_byte}, v = {known_encrypted_byte}, p = {mod}, inv = {inv}")
        for byte in cipher_text[1::2]:
            result.append(byte * known_plain_byte * inv % mod)
            print(f"v' = {byte}, m' = {result[-1]}")
    else:
        x = num_algs.discrete_logarithm(y, g, mod)
        for i in range(0, len(cipher_text) - 1, 2):
            result.append(decrypt(cipher_text[i], cipher_text[i + 1], x, mod))
    return result



import mmh3

class MurmurHash:
    def __init__(self, seed: int):
        self.seed = seed

    def hash(self, key: str) -> int:
        if not isinstance(key, str):
            key = str(key)

        return mmh3.hash(key, self.seed) & 0xffffffff
    
class BaseHash:
    def __init__(self, seed: int = 0):
        self.seed = seed

    def hash(self, key: str) -> int:
        if not isinstance(key, str):
            key = str(key)

        h = self.seed
        p = 31
        mod = 10**9 + 9

        for char in key:
            h = (h * p + ord(char)) % mod

        return h


class DoubleHashing:
    def __init__(self, use_mmh3=False):
        if use_mmh3:
            self.hash1 = MurmurHash(seed=17)
            self.hash2 = MurmurHash(seed=31)
        else:
            self.hash1 = BaseHash(seed=17)
            self.hash2 = BaseHash(seed=31)

    def get_hashes(self, key: str, k: int, m: int):
        """
        Generate k hash values using double hashing.
        Output indices are in range [0, m-1]
        """
        h1 = self.hash1.hash(key)
        h2 = self.hash2.hash(key + "_salt")  # simple variation

        if h2 == 0:
            h2 = 1  # avoid zero step
        h2 = h2 % m
        if h2 % 2 == 0:
            h2 += 1
        hashes = []

        for i in range(k):
            combined = (h1 + i * h2) % m
            hashes.append(combined)

        return hashes
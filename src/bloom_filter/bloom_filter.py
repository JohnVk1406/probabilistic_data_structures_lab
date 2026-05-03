from src.bit_array import BitArray
from src.hashing import DoubleHashing
import math

class BloomFilter:
    def __init__(self, n: int, fp_rate: float, use_mmh3=False):
        if n <= 0 or not (0 < fp_rate < 1):
            raise ValueError("Invalid parameters")

        self.n = n
        self.fp_rate = fp_rate

        self.size = int(-(n * math.log(fp_rate)) / (math.log(2) ** 2))

        self.num_hashes = int((self.size / n) * math.log(2))

        self.num_hashes = max(1, self.num_hashes)

        self.bit_array = BitArray(self.size)
        self.hasher = DoubleHashing(use_mmh3=use_mmh3)

    def add(self, key: str):
        indices = self.hasher.get_hashes(key, self.num_hashes, self.size)

        for idx in indices:
            self.bit_array.set_bit(idx)

    def contains(self, key: str) -> bool:
        indices = self.hasher.get_hashes(key, self.num_hashes, self.size)

        for idx in indices:
            if self.bit_array.get_bit(idx) == 0:
                return False

        return True
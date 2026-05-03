class BitArray:
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size must be positive")

        self.size = size
        self.array = bytearray((size + 7) // 8)

    def _get_position(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Bit index out of range")

        byte_index = index // 8
        bit_offset = index % 8
        return byte_index, bit_offset

    def set_bit(self, index: int):
        byte_index, bit_offset = self._get_position(index)
        self.array[byte_index] |= (1 << (7 - bit_offset))

    def clear_bit(self, index: int):
        byte_index, bit_offset = self._get_position(index)
        self.array[byte_index] &= ~(1 << (7 - bit_offset))

    def get_bit(self, index: int) -> int:
        byte_index, bit_offset = self._get_position(index)
        return (self.array[byte_index] >> (7 - bit_offset)) & 1

    def __len__(self):
        return self.size

    def __repr__(self):
        bits = ''.join(str(self.get_bit(i)) for i in range(self.size))
        return f"BitArray({bits})"
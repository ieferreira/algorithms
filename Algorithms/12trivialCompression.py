from sys import getsizeof
# based on Kopec, 2019


class CompressedDirection:
    def __init__(self, set_direction: str) -> None:
        self._compress(set_direction)

    def _compress(self, set_direction: str) -> None:
        self.bit_string: int = 1
        for direction in set_direction.upper():
            self.bit_string <<= 2
            if direction == "N":
                self.bit_string |= 0b00
            elif direction == "S":
                self.bit_string |= 0b01
            elif direction == "W":
                self.bit_string |= 0b10
            elif direction == "E":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Direction:{direction}")

    def decompress(self) -> str:
        set_direction: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                set_direction += "N"
            elif bits == 0b01:
                set_direction += "S"
            elif bits == 0b10:
                set_direction += "W"
            elif bits == 0b11:
                set_direction += "E"
            else:
                raise ValueError(f"Invalid bits:{bits}")
        return set_direction[::-1]

    def __str__(self) -> str:
        return self.decompress()


original: str = "NSWENWESSNNWESNNWESNWNSNEWSENWNSNWENSNWENWSNWEEWSSWNSNWENSNWNEENWNSNWENS" * 20
original_size: int = getsizeof(original)
print(f"original  size is  {original_size} bytes")
compressed: CompressedDirection = CompressedDirection(original)  # compress
compressed_size: int = getsizeof(compressed.bit_string)
print(f"compressed size is {compressed_size} bytes")
print(compressed)  # decompress
print("original and decompressed are the same: {}".format(
    original == compressed.decompress()))
print(f"Compression Ratio {round((compressed_size/original_size)*100, 2)} %")

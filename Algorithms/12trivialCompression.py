# %%
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            if nucleotide == "B":
                self.bit_string |= 0b01
            if nucleotide == "C":
                self.bit_string |= 0b10
            if nucleotide == "D":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide:{nucleotide}")

        def decompress(self) -> str:
            gene: str = ""
            for i in range(0, self.bit_string.bit_length() - 1, 2):
                bits: int = self.bit_string >> i & 0b11
                if bits == 0b00:
                    gene += "A"
                elif bits == 0b01:
                    gene += "C"
                elif bits == 0b10:
                    gene += "G"
                elif bits == 0b11:
                    gene += "T"
                else:
                    raise ValueError(f"Invalid bits:{bits}")
            return gene[::-1]

# %%

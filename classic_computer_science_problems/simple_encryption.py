from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    tb: bytes = token_bytes(nbytes=length) # Return a random byte string containing nbytes number of bytes.
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")

# If the bits of two numbers are combines using XOR, a helpful property is that the product 
# can be recombined with either of the operands to produce the other operand
#
# A ^ B = C  
# C ^ B = A
# C ^ A = B 


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # Doing the XOR
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    # It was necessary to add 7 to the length of the decrypted data before using 
    # integer-division (//) to divide by 8 to ensure that we “round up,” to avoid 
    # an off-by-one error.
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!") 
    result: str = decrypt(key1, key2) 
    print(result)   
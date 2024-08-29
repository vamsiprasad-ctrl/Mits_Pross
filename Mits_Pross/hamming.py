class Hamming:
    def __init__(self, str1: str, str2: str):
        if len(str1) != len(str2):
            raise ValueError("Strings must be of equal length for Hamming distance")
        self.str1 = str1
        self.str2 = str2

    def similarity(self) -> int:
        distance = sum(char1 != char2 for char1, char2 in zip(self.str1, self.str2))
        return distance


# Example Usage
str2 = "Data Science"
str3 = "Machine Lear"

# Initialize the Hamming class with str2 and str3
hamming = Hamming(str2, str3)

# Calculate the Hamming distance
hamming_distance = hamming.similarity()

# Print the result
print(f"Hamming Distance between '{str2}' and '{str3}': {hamming_distance}")

class Overlap:
    def __init__(self, str1: str, str2: str):
        self.str1 = set(str1)
        self.str2 = set(str2)

    def similarity(self) -> float:
        intersection = self.str1.intersection(self.str2)
        min_size = min(len(self.str1), len(self.str2))
        return len(intersection) / min_size


# Example Usage
str1 = "Data Science"
str2 = "Machine Learning"

# Initialize the Overlap class with str1 and str2
overlap = Overlap(str1, str2)

# Calculate the Overlap similarity coefficient
overlap_coefficient = overlap.similarity()

# Print the result
print(f"Overlap Similarity between '{str1}' and '{str2}': {overlap_coefficient}")

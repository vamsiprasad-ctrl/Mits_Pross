class Jaccard:
    def __init__(self, str1: str, str2: str):
        self.str1 = set(str1)
        self.str2 = set(str2)

    def similarity(self) -> float:
        intersection = self.str1.intersection(self.str2)
        union = self.str1.union(self.str2)
        return len(intersection) / len(union)


# Example Usage
str1 = "Data Science"
str2 = "Machine Learning"

# Initialize the Jaccard class with str1 and str2
jaccard = Jaccard(str1, str2)

# Calculate the Jaccard similarity coefficient
jaccard_coefficient = jaccard.similarity()

# Print the result
print(f"Jaccard Similarity between '{str1}' and '{str2}': {jaccard_coefficient}")

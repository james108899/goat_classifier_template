# simple_random_model.py
import random

class RandomModel:
    def predict(self, image):
        # Randomly choose between two classes
        prediction = random.choice(["Mature Billy", "Nanny, Juvenile"])
        # Generate a random confidence score between 50% and 100%
        confidence = round(random.uniform(50, 100), 2)
        return prediction, confidence

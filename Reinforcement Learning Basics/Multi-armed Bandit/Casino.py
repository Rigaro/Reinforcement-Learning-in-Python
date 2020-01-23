import numpy as np
    
class SlotMachine:
    # SlotMachine class, basic functionality
    
    def __init__(self, probability):
        self.probability = probability # The probability of giving a reward
    
    def pull(self):
        # Simulates pulling the arm of a slot machine, which can either give a reward or not (returns 0 or 1)
        
        # First get a random number between 0 and 1
        randomNumber = np.random.random_sample()
        # Now check the with the probability and return 0 or 1
        if randomNumber <= self.probability:
            return 1
        else:
            return 0
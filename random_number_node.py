"""
Random Number Generator Node for ComfyUI
Generates random integers and floats between user-specified min/max values.
"""

import random


class RandomNumber:
    """
    A ComfyUI custom node that generates random numbers between two user-selectable values.
    Useful for seed variation, parameter randomization, and workflow experimentation.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "min_value": ("FLOAT", {
                    "default": 0.0,
                    "min": -999999.0,
                    "max": 999999.0,
                    "step": 0.01,
                    "display": "number"
                }),
                "max_value": ("FLOAT", {
                    "default": 100.0,
                    "min": -999999.0,
                    "max": 999999.0,
                    "step": 0.01,
                    "display": "number"
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff,
                    "display": "number"
                }),
            }
        }
    
    RETURN_TYPES = ("INT", "FLOAT")
    RETURN_NAMES = ("int", "float")
    FUNCTION = "generate"
    CATEGORY = "Logic/Math"
    
    DESCRIPTION = "Generates random numbers between min and max values. Use the seed for reproducible results."
    
    def generate(self, min_value, max_value, seed):
        """
        Generate a random number between min_value and max_value.
        
        Args:
            min_value: Minimum value (inclusive)
            max_value: Maximum value (inclusive)
            seed: Random seed for reproducible results
            
        Returns:
            tuple: (int_value, float_value)
        """
        # Ensure min is less than max - swap if needed
        if min_value > max_value:
            min_value, max_value = max_value, min_value
        
        # Set the seed for reproducibility
        random.seed(seed)
        
        # Generate random float
        float_val = random.uniform(min_value, max_value)
        
        # Convert to int
        int_val = int(float_val)
        
        return (int_val, float_val)


# Node registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "RandomNumber": RandomNumber
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomNumber": "Random Number"
}

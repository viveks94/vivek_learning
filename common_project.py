"""
This is a common project file for diffent features.
Author: Vivek Sikarwar  
Date: 2024-06-01
"""
import os
import inspect
import pdb
import logging as log
from common_lib import CommonLib
class CommonProject(CommonLib):
    def __init__(self):
        print("This is the constructor of CommonProject.")
        super().__init__()
    log.basicConfig(level=log.INFO)
    def calculate_factorial(self, desc="Calculate the factorial of a number"):
        """
        Calculate the factiorial of a number.
        params:
            desc: A description of the method. Default is "Calculate the factorial of a number".
        """
        try:
            num = int(input("Enter a number: "))
            fact = self.factorial(num)
            log.info(f"The factorial of {num} is: {fact}")
        except Exception as e:
            log.error(f"Encountered an exception in method calculate_factorial: {e}")
            return None

if __name__ == "__main__":
    my_object = CommonProject()
    my_object.test_methods()


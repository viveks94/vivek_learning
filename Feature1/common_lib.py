"""
This is a common library file.
Author: Vivek Sikarwar
Date: 2024-06-01
"""
import os
import sys
import inspect 
import pdb
import logging as log
class CommonLib:
    """
    This is a common library that can be used across multiple projects.
    """
    log.basicConfig(level=log.INFO)
    def factorial(self, num, desc="Calculate the factorial of a number"):
        """
        Calculates the factorial of a number.
        Params:
            num: The number to calculate the factorial of. eg num=5
            desc: A description of the method. Default is "Calculate the factorial of a number".
        """
        try:
            if num == 0:
                return 1
            else:
                return num * self.factorial(num - 1)
        except Exception as e:
            log.error(f"Encountered an exception in method factorial: {e}")
            return None



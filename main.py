def main():
    print("Hello from dsc190-tot-assignment-5!")


if __name__ == "__main__":
    main()
	
Python
import os  # Rule Violation 1: Unused import (F401)

def my_bad_function():
    x = 10  # Rule Violation 2: Local variable assigned but never used (F841)
    print(undefined_variable)  # Rule Violation 3: Undefined name (F821)

my_bad_function()

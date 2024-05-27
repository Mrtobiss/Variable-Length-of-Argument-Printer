"""
Variable Length Argument Printer

Created by: Ibrahim Yisau
Date: May 27, 2024

This program defines a function func1 that accepts a variable number of arguments using the *args syntax. The function iterates over each argument and prints its value. The program demonstrates how to define and call a function with variable length arguments in Python.

Usage:
Call the func1 function with any number of arguments, and it will print each argument value on a separate line. """

# Define a function named func1 that accepts a variable number of arguments (*args)
def func1(*args):
	# Iterate over each argument passed to the function
	for arg in args:
		# Print each argument value
		print(arg)

# Call the func1 function with two arguments
func1("Hello world!", "I am Yisau Ibrahim.")

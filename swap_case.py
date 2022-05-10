#!/usr/bin/env python3

# Challenge:
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# 
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# 
# Function Description: Complete the swap_case function in the editor below.
# 
# swap_case has the following parameters:
# string s: the string to modify
# Returns: string: the modified string
# Input Format: A single line containing a string
# 
# Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap(s):
    # input: s = string
    # output: result = string

    result = ""  # Initialize output

    for j in s:
        if j.isalpha():
	    result = result + j.swapcase()  # Swap case since alpha
        else:
            result = result + j  # Not alpha so just add as is

    return result


def main():
    result = swap(s)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# In Python, a string can be split on a delimiter.
# Example:
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# 
# Joining a string is simple:
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 
# 
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# 
# Function Description
# Complete the split_and_join function in the editor below.
# 
# split_and_join has the following parameters:
    # string line: a string of space-separated words
# 
# Returns
    # string: the resulting string
# 
# Input Format
# The one line contains a string consisting of space separated words.
# 
# Sample Input: this is a string   
# Sample Output: this-is-a-string

import pytest

def test1():
    assert split_and_join("This is a line") == "This-is-a-line"


def split_and_join(line):
    result = line.split(sep = " ")
    result = "-".join(result)
    return result


if __name__ == "__main__":
    line = "This is a line"
    res = split_and_join(line)
    print(res)

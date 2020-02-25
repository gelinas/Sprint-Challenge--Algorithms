'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # base case defined as first two letters of string are th
    if word[:2] == "th":
        count = 1

    # recursion, remove first letter of string and retest
    if len(word) > 2:
        count += count_th(word[1:])
    
    return count

# plan: split the word down, test it when just two characters

# print(count_th("supercalifragilisth"))
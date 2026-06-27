"""a list where every word has a length of 6
words that include the letter 'e'
words that do not include the letter 'e'
5 letter words that contain the letter e, but not in the first position"""
word_list = open("enable1.txt").read().splitlines()
length_of_six = [x for x in word_list if len(x) == 6]
include_e = [x for x in word_list if 'e' in x]
no_e = [x for x in word_list if x not in include_e]
e_not_in_first = [x for x in include_e if 'e' != x[0]]

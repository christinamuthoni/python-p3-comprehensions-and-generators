#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    return even_numbers
            
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
result = return_evens(num_list)
print(result)

def make_exclamation(sentence_list):
    new_sentence_list = [sentence_list + "!" for sentence_list in sentence_list]
    return new_sentence_list

sentence_list = ("am home")    
result = make_exclamation(sentence_list)
print(result)

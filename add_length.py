#Kyu 8
#https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python
# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.
def add_length(str_):
    
    str_ += " "
    word = ""
    result = []
    counter = 0
    
    for i in range(len(str_)):
        if str_[i] != " ":
            word += str_[i]
            counter += 1
        else:
            word += f" {len(word)}"
            result.append(word)
            word = ""
            counter = 0
            
    return result
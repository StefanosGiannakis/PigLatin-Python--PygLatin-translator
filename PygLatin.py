# we need a variable with the suffix string 'ay'
pyg = 'ay'

# We create a function to organize our code 
def word_machine():
    # make the input word lower case
    word=original.lower()
    # takes the first letter
    first=word[0]
    # creating of our new word with string concatenation
    new_word=word+first+pyg
    # we "subtract" the ex-first letter 
    new_word= new_word[1:len(new_word)]
    #Final word with uppercase the first letter is variable 'wordy'
    wordy=new_word[0].upper()+new_word[1:len(new_word)]
    
    return print(wordy)

    #Implementing our Own Validation Rules
while (True):
    original = input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        word_machine()
        break
    else:
        print (' Oops - try again')
        continue

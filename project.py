'''
Challenge 8 (Mini Project): Word Frequency Counter


👉 Take a paragraph and:

Convert to lowercase

Remove punctuation

Count how often each word appears

Print the top 5 most frequent words 
'''
import re
Paragraph = "You have the right to work, but for the work's sake only. You have no right to the fruits of work. Desire for the fruits of work must never be your motive in working. Never give way to laziness, either. Perform every action with you heart fixed on the Supreme Lord. Renounce attachment to the fruits. Be even-tempered in success and failure: for it is this evenness of temper which is meant by yoga. Work done with anxiety about results is far inferior to work done without such anxiety, in the calm of self-surrender. Seek refuge in the knowledge of Brahma. They who work selfishly for results are miserable."
Paragraph = Paragraph.lower()
punctuation_remove = re.sub(r'[^\w\s]','', Paragraph) # removes if the paragraph is not a word or white spaces
print(punctuation_remove)
listed_punctuation = punctuation_remove.split()
print(listed_punctuation)
dictionary_punctuated = {}

print(213*"*")
for values in listed_punctuation:
    if values in dictionary_punctuated:
        dictionary_punctuated[values] +=1
    else:
        dictionary_punctuated[values] = 1

top_5 = sorted(dictionary_punctuated.items(), key =lambda x:x[1], reverse=True)

for key, value in top_5[:5]:
    print(key, value)







        
    


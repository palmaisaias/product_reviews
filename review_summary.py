#Task 3

#I just left this sample here, but its not necessary since I gave the function ability to receive text.

# review = '''Over 60 years ago in 1954, J.R.R. Tolkien unveiled the first installment of his series 'Lord of the Rings' 
# with the publication of “The Fellowship of the Ring”. Unknown to him at the time, his series would stand to leave a legacy- 
# one that would bring together communities’ decades after his death and revolutionize the fantasy genre forever. 
# However, in light of the fact that the novel was published literal generations ago, I would like to try my best to 
# analyze whether or not it stacks up today with modern-day fantasy novels.'''

def summarizer():
    three_dots = '...'
    review = input('Enter your review here:\n')     #instead of predetermined text, you can now enter your own reviews. Also new line for formating
    itemized = review.split(' ')    #split with a ' ' as a separator. This way I will always get full words
    summary = itemized[:30]     #simple use of index
    flow = ' '.join(summary)    #once I have my desired characters, I rejoin the text
    lotr_summary = flow + three_dots #made '...' a variable and placed it inside my function

print('\nHere is a summary of your review:\n'+ summarizer())    #couple of new lines for formating
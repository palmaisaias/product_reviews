#1. Product Review Analysis
# Task 1: Keyword Highlighter
# Print out each review with the keywords in uppercase so they stand out.

#FIRST attempt. got caught up trying to find a way to reformat to original format WITH uppercase words incorporated. 

    # python_reviews = [ "This product is really good. I'm impressed with its quality.",
    # "The performance of this product is excellent. Highly recommended!",
    # "I had a bad experience with this product. It didn't meet my expectations.",
    # "Poor quality product. Wouldn't recommend it to anyone.",
    # "The product was average. Nothing extraordinary about it." ]

    # joined_list = ', '.join(python_reviews).lower()
    # # print(joined_list)

    # ratings = ["good", "excellent", "bad", "poor", "average"]

    # for rating in ratings:
    #     if rating in joined_list:
    #         correct_list = joined_list.replace(rating, rating.upper())

    # print(correct_list)
        

    # for rating in ratings:
    #     if rating in joined_list:
    #         joined_list


    # upper_list = [review.upper() for review in python_reviews]
    # print(upper_list)

#SECOND/ millionth attempt.    

python_reviews = [ "This product is really good. I'm impressed with its quality.", 
"The performance of this product is excellent. Highly recommended!",
"I had a bad experience with this product. It didn't meet my expectations.",
"Poor quality product. Wouldn't recommend it to anyone.",
"The product was average. Nothing extraordinary about it." ]

ratings = ["good", "excellent", "bad", "poor", "average"] #made to pinpoint words on interest

joined_list = ', '.join(python_reviews).lower() #makes the list a single string and also lowercase. easier to search imo.

for rating in ratings:  #run loop to check if items in 'ratings' list are in 'python_reviews'
    if rating in joined_list:
        joined_list = joined_list.replace(rating, rating.upper()) #if words are found, it replaces them with all uppercase. 
    
joined_list = joined_list.split(', ')   #takes the single-string list and splits it back up into multiple strings inside the list. Used the original ', ' that I used to 'join' earlier in the code
for joined in joined_list:  #run 'for loop' just to get the formating I wanted.
    print(joined)
    print()

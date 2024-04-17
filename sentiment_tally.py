#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review. 
#Use a predefined list of positive and negative words to check against. 
#The function should return the count of positive and negative words for each review.

#FIRST few attempts. Mostly notes. Code is no good. Was missing a 'housing' to collect all of my 'good_tally' counts. They just kept recycling 

    # py_reviews = [ "This product is really good. I'm impressed with good its quality.", 
    # "The performance of this product is excellent. Highly recommended!",
    # "I had a bad experience with this product. It didn't meet my expectations.",
    # "Poor quality product. Wouldn't recommend it to anyone.",
    # "The product was average. Nothing extraordinary about it." ]

    # positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
    # negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


    # for review in py_reviews:   #starts loop for every string in the list of reviews
    #     good_tally = 0    
    #     for pos in positive_words:  #nested 'for loop' in order to work with every item in 'positive_words'
    #        if pos in review:    #if a positve word is found in the review...
    #            good_tally += review.count(pos)  #add the count (aka number of times it appears) to the total of 'good_tally'
    #     print(good_tally)   #prints for every string in 'py_reviews' aka every 'review'
          
#THIRD, or so, attempt. Got the structure down for collecting a tally.

    # py_reviews = [ "This product is really good. I'm impressed with good its quality.", 
    # "The performance of this product is excellent. Highly recommended!",
    # "I had a bad experience with this product. It didn't meet my expectations.",
    # "Poor quality product. Wouldn't recommend it to anyone.",
    # "The product was average. Nothing extraordinary about it." ]

    # positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
    # negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    # def tally_function():   
    #     listed_results = [] #I want my results of each iteration in a list so they remain separate. Also relatively easier to format
    #     for review in py_reviews:   #starts loop for every string in the list of reviews
    #         good_tally = 0  #using this as a counter.    
    #         for pos in positive_words:  #nested 'for loop' in order to work with every item in 'positive_words'
    #             if pos in review:    #if a positve word is found in the review...
    #                 good_tally += review.count(pos)  #add the 'count' (aka number of times it appears) to the total of 'good_tally'
    #         listed_results.append(good_tally)   #adds the count of positive words, per review to 'listed_results' list 
    #     return listed_results   #DONT FORGET TO 'PRINT' THE FUNCTION TO SEE RESULTS  

    # pos_tally_count = tally_function()  #gave it a variable so I could iterate through it

    # for index in range(len(py_reviews)):    
    #     print(py_reviews[index],': This review has', pos_tally_count[index], 'positive remarks')
    #     print()

# Lost count of attempts. In this set i put together the logic from the previous attempt and applied it to the 'negative' words

    # def tally_function():   
    #     listed_results = [] #I want my results of each iteration in a list so they remain separate. Also relatively easier to format
    #     listed_bad_results = []
    #     for review in py_reviews:   #starts loop for every string in the list of reviews
    #         good_tally = 0  #using this as a counter.    
    #         bad_tally = 0
    #         for pos in positive_words:  #nested 'for loop' in order to work with every item in 'positive_words'
    #             if pos in review:    #if a positve word is found in the review...
    #                 good_tally += review.count(pos)  #add the 'count' (aka number of times it appears) to the total of 'good_tally'
    #         listed_results.append(good_tally)   #adds the count of positive words, per review to 'listed_results' list 
    #         for neg in negative_words:
    #             if neg in review:
    #                 bad_tally += review.count(neg)
    #         listed_bad_results.append(bad_tally)
    #     return listed_results, listed_bad_results   #multiple returns have to be listed in this format. Separated by a ',' 

    # pos_tally_count, neg_tally_count = tally_function()  #gave it a variable so I could iterate through it

    # for index in range(len(py_reviews)):    #lists correspond so this works wonderfully
    #     print(py_reviews[index],': This review has', pos_tally_count[index], 'positive remarks and', neg_tally_count[index], 'negative remarks.')
    #     print()


#7036th attempt
# One of the words in the reviews is CAPITALIZED. Dint account for that so going to try and run it all lowercase.

py_reviews = [ "This product is really good. I'm impressed with good its quality.", 
"The performance of this product is excellent. Highly recommended!",
"I had a bad experience with this product. It didn't meet my expectations.",
"Poor quality product. Wouldn't recommend it to anyone.",
"The product was average. Nothing extraordinary about it." ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def tally_function():
    py_revs_lower = [rev.lower() for rev in py_reviews]   #takes every element of original reviews and makes them lowercase. This was the key. This is how to get the formatting back in the output.
    listed_results = [] #I want my results of each iteration in a list so they remain separate. Also relatively easier to format
    listed_bad_results = []
    for review in py_revs_lower:   #starts loop for every string in the list of reviews
        good_tally = 0  #using this as a counter.    
        bad_tally = 0
        for pos in positive_words:  #nested 'for loop' in order to work with every item in 'positive_words'
            if pos in review:    #if a positve word is found in the review...
                good_tally += review.count(pos)  #add the 'count' (aka number of times it appears) to the total of 'good_tally'
        listed_results.append(good_tally)   #adds the count of positive words, per review to 'listed_results' list 
        for neg in negative_words:
            if neg in review:
                bad_tally += review.count(neg)
        listed_bad_results.append(bad_tally)
    return listed_results, listed_bad_results   #multiple returns have to be listed in this format. Separated by a ',' 

pos_tally_count, neg_tally_count = tally_function()  #gave it a variable so I could iterate through it

for index in range(len(py_reviews)):
    print()    #lists correspond so this works wonderfully
    print(py_reviews[index],': This review has', pos_tally_count[index], 'positive remarks and', neg_tally_count[index], 'negative remarks.')
    print()


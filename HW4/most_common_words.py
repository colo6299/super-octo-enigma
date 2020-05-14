
# This code is bad, and I should feel bad for having written it. 
# The based version of this same thing is in my markov project
def most_common_words(text, num):
    
    word_dictionary = {}
    for word in text.split():
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    top_n = [0] * num

    for word, count in word_dictionary:
        for index, number in enumerate(top_n):
            if count > number[1]:
                top_n.insert(index, (word, count))
                top_n.pop()
    
    return top_n
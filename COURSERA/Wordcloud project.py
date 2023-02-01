###########################
# Wordcloud project
#
# Project goal: 
# Create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the WordCloud class.
#
# Once you have the dictionary, use this code to generate the word cloud image:
# cloud = wordcloud.WordCloud()
# cloud.generate_from_frequencies(frequencies)
# cloud.to_file("myfile.jpg")
############################

##############################
# Things to remember 
# Before processing any text, you need to remove all the punctuation marks. 
# To do this, you can go through each line of text, character-by-character, using the isalpha() method. 
# This will check whether or not the character is a letter.
##############################
#
# To split a line of text into words, you can use the split() method.
#
###############################
# Before storing words in the frequency dictionary, check if they’re part of the "uninteresting" set of words (for example: "a", "the", "to", "if"). 
# Make this set a parameter to your function so that you can change it if necessary.
#
###############################
# Input file
# For the input file, you need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a 
# website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, 
# like a Shakespeare play or a novel by Jane Austen.
###################################

## For this project, you’ll create a “word cloud” from a text by writing a script. This script needs to process the text, remove punctuation, 
# count the frequencies, and ignore uninteresting or irrelevant words. 

#################################################################
#
# Write a function in the cell below that iterates through the words in file_contents, removes punctuation, and counts the frequency of each word. 
# Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the". 
# Then use it in the generate_from_frequencies function to generate your very own word cloud!
#
# Hint: Try storing the results of your iteration in a dictionary before passing them into wordcloud via the generate_from_frequencies function.

#################
# This worked on coursera lab!!!!
#
#################

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
# split    
    words=file_contents.split()

# make list all lower case
    lower_case_words=[s.lower() for s in words] 
#initialise the dictionary
    word_dictionary={}

    for word in lower_case_words:  
        if word.isalpha():
    #reset word count for the next word
            word_count=0

    # check if they are an uninteresting word
        if word in uninteresting_words:
      # if it is uninnteresting, jump to next iteration of the loop
            continue


    # create the dictionary

    # get a number count
        word_count=lower_case_words.count(word)

 

    # Append to the dictionary ONLY if its not already there
        if word not in word_dictionary:
            word_dictionary[word]=word_count

   
  # Not all alpha numeric so remove punctuation here
        else:
            new_word=""
            word_count=0
  #iterate through each string char and replace
            for letter in word:
                if letter.isalpha():
        # build the word via individual chars
                    new_word += letter

    # add 1 to include the existing
            word_count=lower_case_words.count(new_word) + 1 

            if new_word not in word_dictionary:
          #print(word_dictionary.keys())
          #print(new_word)
                word_dictionary[new_word]=word_count
    
    
    #wordcloud
    #cloud = wordcloud.WordCloud()
    #cloud.generate_from_frequencies(word_dictionary)
    #return cloud.to_array()

calculate_frequencies("Hello I am the game, yes the game is the game")


    #wordcloud
    #cloud = wordcloud.WordCloud()
    #cloud.generate_from_frequencies()
    #return cloud.to_array()
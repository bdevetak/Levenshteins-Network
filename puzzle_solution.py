import string
import time

# get_next_level function
def get_next_level(current_level, current_level_test_set):
    """ 
    Finds the words from the set current_level_test_set, that are at
    levenstein distance 1 from at least one words in the current_level set.
    """
    global number_of_members
    global level_cursor

    # level counter message
    print "Processing level ", level_cursor, ":"
    
    # word variations of the current level 
    # print "--> lv ", level_cursor, ">>", "calculating current level variations...", "\n"
    current_level_variations = set()
    for current_level_word in current_level:
        for letter in letters:
            # insert variations
            for index in range(len(current_level_word) + 1):
                i_variation = current_level_word[0:index] + letter + current_level_word[index:]
                current_level_variations.add(i_variation)
            # replace and delete variations
            for index in range(len(current_level_word)):
                # replace
                r_variation = current_level_word[:index] + letter + current_level_word[index+1:]
                current_level_variations.add(r_variation)
                # delete
                d_variation = current_level_word[:index] + current_level_word[index+1:]
                current_level_variations.add(d_variation)
     
    # Exclude current level from current_level_test_set
    remaining_words = current_level_test_set.difference(current_level)

    # get friends for the current level as intersection of remaining_words and current_level_variations
    friends = remaining_words.intersection(current_level_variations)
    
    # update number of network members
    number_of_members = number_of_members + len(current_level)

    # level result message
    print "\t ( lv ", level_cursor, ") --> (", len(friends), ") friends found in next level.", "\n"
    
    # process next level or exit
    if len(friends) > 0:
        level_cursor = level_cursor + 1
        get_next_level(friends, remaining_words)

print "--------------\n"
print "START:        \n"
print "--------------\n"

# start time
start_time = time.time()

# variables
number_of_members = 0
words = set()
letters = set()
level_cursor = 0

# import words from file
words_file = open("word.list.txt","r")
words_array = map(string.rstrip, words_file.readlines())

# init words and letters sets
for word in words_array:
    words.add(word)
    for letter in word:
        letters.add(letter)
        
start_level = set()
start_level.add('causes')

get_next_level(start_level, words)

print "\n"
print "Total number of members in network of 'causes': ", number_of_members
print "\n"

duration = time.time() - start_time

print "total processing time: ", duration, "seconds."
print "--------------\n"
print "END:          \n"
print "--------------\n"

from collections import defaultdict


# Takes a word and returns a lower case string of the letters in alphabetical order
# The precondition for this function is that it is called on a string.
# The loop invariant is that all letters considered by the loop will have been added
# To the list declared in the function, and be converted to lower case.
# The list is then sorted, and joined into a string to make the post condition:
# Returns an alphabetized lower case key for a string.


def create_key(word):
    letters = []
    for c in word:
        letters.append(c.lower())
    letters = sorted(letters)
    return ''.join(letters)


# Iterates through list of words from a text file.  If the key for the word is not in the dictionary,
# it is added, and an empty list created for it's value.  The word is then appended to the empty list.
# If the key and list already exist, the value is appended to the list.
# The precondition is that there is a 'words.txt' document in the correct folder location, though
# this is easily adjusted, populated with one word per line.
# There are two loops, and therefore two loop invariants.  The first, is that all lines previous to
# the currently considered one will have been stripped of white space and new line characters, and
# added to the word_list.
# The post condition is word_list will be populated with all words from the words.txt file. This is also
# the precondition for the 2nd loop.  It's invariant is that all words considered up to the current one in word_list
# will have either created dictionary keys and been assigned to them as list entry values, or been assigned as list
# entry values to existing keys.
# The post condition of the entire function is a dictionary of all the words from the text file keyed by their
# alphabetical order, and assembled in lists based on the letters they contain.


def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d


def build_dictionary():
    word_list = []
    anagrams = {}
    raw_word_list = open('wordList.txt', 'r')
    for line in raw_word_list.readlines():
        word = line.strip()
        if word.startswith("v"):
            word_list.append(word)
    raw_word_list.close()
    for word in word_list:
        key = create_key(word)
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return anagrams


# This is the function I chose to manually call.  It's precondition is the dictionary created by the above function.
# The first loop invariant is that the most_anagrams variable will contain a number equal to the largest yet seen
# (in terms of items in the list values) list value.
# The nested loops achieve printing the lists in descending order.  The invariant is that until the dictionary is
# traversed, every considered list value with size matching the most_anagrams variable will be printed.  Once all lists
# of the largest size are printed, most_anagrams is decremented by 1.
# The post condition is the final print out of lists in descending order.
# I added a variable and a line at the end to display the number of sets printed.


def print_anagram_sets(vWordsList):
    # anagrams = build_dictionary()
    # most_anagrams = 0
    # total_sets = 0
    # for key in anagrams:
    #     if len(anagrams[key]) > most_anagrams:
    #         most_anagrams = len(anagrams[key])
    # for i in range(most_anagrams, 1, -1):
    #     for key in anagrams:
    #         if len(anagrams[key]) == most_anagrams:
    #             print(anagrams[key])
    #             total_sets += 1
    #     most_anagrams -= 1
    # print(total_sets)
    for key, val in build_dictionary().items():
        if val in vWordsList:
            print(key, val)

    ##main loop
wordsList = ["serve", "rival", "lovely", "caveat", "devote", "irving", "livery", "selves", "latvian", "saviour", "observe", "octavian", "dovetail", "levantine"]
print_anagram_sets(wordsList)

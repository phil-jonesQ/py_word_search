

def anagram_checker(seed, words):
    results = {} # Creat an empty dict to store the results
    for word in words:
        seed_s = sorted(seed) # Sort the anagram to a list of chars
        word_s = sorted(word) # Sort the word we are processing to a list of chars
        if seed_s == word_s: # Check if the sorted results match (if so, they are an anagram of the seed word)
            results[word] = True # Update the result
        else:
            results[word] = False 
    return results

def display_results(results, anagram_seed):
    # Process Results
    for key in results:
        if results[key]:
            print(key + " is an anagram of " + anagram_seed)
        else:
            print(key + " is not an anagram of " + anagram_seed)

# Change here to check if other words are anagrams
anagram_seed = "players"
anagrams = ["parsley","yelsrap","pteyras","pleyars","yalpers","serplay","playsrez","palsyer","larpsey"]

# Check the anagram list against the anagram seed using the anagram_checker funtion, and assign the returned results
results = anagram_checker(anagram_seed, anagrams)

# Process Results
display_results(results, anagram_seed)

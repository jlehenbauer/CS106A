def main():
         dictionary = {}
         dictionary["learning"] = "awesome"
         dictionary["coding"] = "fun"
         # ... Fill with more data
         remove_keys_containing_string(dictionary, "learn")
         print(dictionary)
"""
This Python method takes in a dict and a string, then loops through
the dict and removes all entries that have a key containing that string.
"""
def remove_keys_containing_string(dictionary, remove):
    # Since toRemove is being initialized as `None`, you won't be able to add
    # anything to it as a dictionary.
    toRemove = None
    for key in dictionary:
        # You're checking to see whether characters in the ky match the whole
        # string to remove. Consider using the python `is in` operator.
        for i in range(len(key)):
            if key[i:i+1] == remove:
                # This is not how to add items to a dictionary, remind yourself
                # how up above!
                toRemove.add(key)
    if toRemove != None:  
        for key in toRemove:
            del dictionary[key]


main()
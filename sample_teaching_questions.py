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
    # Initialize a list to store the values we want to remove.
    toRemove = []
    for key in dictionary:
        # Check if the string portion exists in the key.
        if remove in key:
            # Append the required key to the list of keys to remove.
            toRemove.append(key)
    if toRemove != []:  
        for key in toRemove:
            del dictionary[key]


main()
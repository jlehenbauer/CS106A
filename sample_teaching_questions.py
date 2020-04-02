def main():
         dictionary = {}
         dictionary["learning"] = "awesome"
         dictionary["coding"] = "fun"
         # ... Fill with more data
         remove_keys_containing_string(dictionary, "learn")
 """
 This Python method takes in a dict and a string, then loops through
 the dict and removes all entries that have a key containing that string.
 """
def remove_keys_containing_string(dictionary, remove):
    toRemove = None
    for key in dictionary:
        for i in range(len(key)):
            if key[i:i+1] == remove:
                toRemove.add(key)
    if toRemove != None:  
        for key in toRemove:
            del dictionary[key]
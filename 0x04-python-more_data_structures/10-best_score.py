#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
<<<<<<< HEAD
        return None
    else:
        value = 0
        for i in a_dictionary:
            if a_dictionary[i] > value:
                value = a_dictionary[i]
                key = i
        return key
=======
        return (None)
    return (max(a_dictionary, key=a_dictionary.get))
>>>>>>> cd8b9a21332c2f809257f6f9334063e3ca09debd

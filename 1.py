# Write a function that accepts two parameters, a parent and a child string. 
# Determine how many times the child string - or an anagram of the child string - 
# appears in the parent string, while non-overlapping.

# myFunction("AdnBndAndBdaBn", "dAn") // 4 ("Adn", "ndA", "dAn", "And")
# myFunction("AbrAcadAbRa", "cAda") // 2

# !NOTE
# According to the specification we are looking for `non-overlapping` solutions, but
# the example in line 5 is an `overlapping` solution.
#
# To solve this contradiction I've implemented both.
# In real project I'll merge the two function -- or I'll ask wich is needed


def my_function(parent, child):
    # I've changed the function name for PEP8
    
    def count_overlapping(anagrams):

        found = []

        for i in range(len(parent)):
            for ii in range(len(anagrams)):
                if parent[i:].startswith(anagrams[ii]):
                    found.append(anagrams[ii])
                    break
            
        print(f'\nThe anagrams of `{child}` are {anagrams}\n')
        print(f'`{parent}` contains {len(found)}! OVERLAPPING anagrams of `{child}`')
        print(f'{found}\n')


    def count_non_overlapping(anagrams):

        found = []
        len_anagrams = len(anagrams[0])     # for non-overlapping
        len_parent = len(parent)            # for non-overlapping
        it_parent = iter(range(len_parent)) # for non-overlapping

        for i in it_parent:
            for ii in range(len(anagrams)):
                if parent[i:].startswith(anagrams[ii]):
                    found.append(anagrams[ii])

                    for _ in range(len_anagrams -1):    # for non-overlapping
                        i = next(it_parent)  

                    break
            
        print(f'`{parent}` contains {len(found)}! NON-OVERLAPPING anagrams of `{child}`')
        print(f'{found}\n')


    def create_anagram_arr(string):

        anagrams = []
        if len(string) <= 1:
            anagrams.append(string)
        else:
            for char in create_anagram_arr(string[1:]):

                for i in range(len(string)):
                    anagrams.append(char[:i] + string[0:1] + char[i:])

        return anagrams 

    count_overlapping(create_anagram_arr(child))
    count_non_overlapping(create_anagram_arr(child))


if __name__ == "__main__":
    my_function("AdnBndAndBdaBn", "dAn")    
    my_function("AbrAcadAbRa", "cAda")     
    my_function("FooBarbarbar", "arv")

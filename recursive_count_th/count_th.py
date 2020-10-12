'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    '''If the input is an empty string '''
    if not word:
        return 0
    
    '''else compare the first 2 letters to th and recursively the rest of the characters'''
    return (1 if word[0:2]=='th' else 0) + count_th(word[1:])
    


    
print(count_th('thereforththth'))

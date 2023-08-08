def palindromguesser(word):
    if word == word[::-1]:
        return True
    else:
        return False

palindromguesser('лепсспел')
palindromguesser('helloworld')
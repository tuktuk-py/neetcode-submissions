def remove_fourth_character(word: str) -> str:
    new =  word[:3]
    minus_fourth = word[4:]
    output = new + minus_fourth
    return output

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

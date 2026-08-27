from typing import List


def create_list_of_odds(n: int) -> List[int]:
    length = range(n+1)
    ans = [i for i in length if i % 2 == 1]
    return ans


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))

from typing import List

list_of_ints: List[int] = [1, 2, 3]
print(list_of_ints[1])  # 2

list_of_strs: List[str] = ["hello", "beautiful", "world"]
print(list_of_strs[1])  # 'beautiful'

list_of_ints.append(4)
print(list_of_ints)  # [1, 2, 3, 4]

list_of_strs.append("!")
print(list_of_strs)  # ['hello', 'beautiful', 'world', '!']

# garbage.py

class Dillo:
    def __init__(self, length: int, is_dead: bool):
        self.length = length
        self.is_dead = is_dead

all_dillos = []  # ArrayList, starting length 4
all_dillos.append(Dillo(10, True))
Dillo(15, False)
tiny_dillo = Dillo(5, False)

all_dillos.append(tiny_dillo)

all_dillos.pop(0)  # Remove first item from the list


nums = [67, 45, 0, 66, -21, 50]

# Example 1
pos_nums = [x for x in nums if x > 0]
avg_val = sum(pos_nums) / len(pos_nums)
print(avg_val)

# Example 2
def avg_pos(numlist: list[int]) -> float:
    pos_nums = [x for x in numlist if x > 0]
    avg_val = sum(pos_nums) / len(pos_nums)
    return avg_val

result = avg_pos(nums)
print(result)
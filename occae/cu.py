from typing import List

previous_reward: List[int] = [0, 0]

# Accessing elements
print(previous_reward[0])  # Output: 0
print(previous_reward[1])  # Output: 0

# Modifying elements
previous_reward[1] = 10
print(previous_reward)  # Output: [0, 10]

# Adding more elements (type safe)
# This would raise a type error:
# previous_reward.append("Hello")

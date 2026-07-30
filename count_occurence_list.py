from collections import Counter
import pandas as pd

arr = [1,2,3,2,3,4,5,2]

#count_2 = arr.count(2)

# element = 2
# count = 0
# for num in arr:
#     if num == element:
#         count += 1

#print("Count of 2 in the list:", count)

counter = Counter(arr)
print(counter[2])

series = pd.Series(arr)
print(series.value_counts())


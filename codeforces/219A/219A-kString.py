# %%
from collections import Counter

k = int(input())
s = input()

set_chars = set(s)
num_chars = Counter(s)

ls = []
for i in num_chars:
    ls.append(num_chars[i])

check = set(ls)

if len(check) == 1:
    ls_str = [str(s) for s in set_chars]
    joined_string = "".join(ls_str)

    print(joined_string*k)
else:
    print("-1")

# %%

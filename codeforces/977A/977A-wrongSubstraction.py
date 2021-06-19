
# %%
n, k = map(int, input().split())

for i in range(k):
    if str(n).endswith("0"):
        n //= 10
    else:
        n -= 1

n = int(n)
print(n)

# %%

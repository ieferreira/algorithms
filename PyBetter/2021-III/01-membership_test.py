# %%
# Check if a variable is contained in some multiple values
# %%

c = 2
x, y, z = 12, 2, 3

if any(i == c for i in (x, y, z)):
    print("exists")
else:
    print("does not exist")

# %%

# Membership test with list
if c in [x, y, z]:
    print("It exists!")
else:
    print("It does not exist!")
# Membership test with tuple
if c in (x, y, z):
    print("It exists!")
else:
    print("It does not exist!")
# Membership test with set
if c in {x, y, z}:
    print("It exists!")
else:
    print("It does not exist!")

# %%

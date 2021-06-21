

dorms, letters = [int(x) for x in input().split()]
number_rooms = []

for i in range(dorms):
    temp = int(input())
    number_rooms.append(temp)

address = []
for i in range(letters):
    temp = int(input())
    address.append(temp)

sendto = []

for i in range(letters):
    for j in range(dorms):
        if address[i] - number_rooms[j] < 0:
            sendto.append((j, (address[i]-number_rooms[j])*-1))
        else:
            pass

print(sendto)


# print(dorms, letters)
# print(number_rooms)
# print(address)

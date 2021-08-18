# for x in range(1,21):
#     if x == 4 or x == 13:
#         print(f"{x} is unlucky")
#     elif x % 2 == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")

for x in range(1,21):
    if x == 4 or x == 13:
        state = "unlucky"
    elif x % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{x} is {state}")

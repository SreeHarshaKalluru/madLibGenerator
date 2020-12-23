stories = {1:"vacuum", 2:'flip_flops', 3:'chicken fight'}
for i in stories:
    print(i, stories[i])
id = int(input("Enter any story id from the above : "))

#No switch case is available in python
if id == 1:
    noun = input("Enter a noun : ")
    print("Be careful not to vacuum the " + noun + " when you clean under your bed.")
elif id == 2:
    adjective = input("Enter an adjective : ")
    print("Flip flops are staple of any " + adjective + " summer wadrobe")
elif id == 3:
    adjective = input("Enter an adjective : ")
    print("If you're going to challenge a couple to a chicken fight during spring break, make sure they're more " + adjective + ' than you!')
else:
    print("Invalid story selected.")
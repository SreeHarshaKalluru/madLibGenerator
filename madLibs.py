stories = {1:"vacuum", 2:'flip_flops'}
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
else:
    print("Invalid story selected.")
distance=int(input("Input the distance travelled: "))
unit=input("Input type K for kms or M for miles: ")
if unit.upper() == "K":
    converted=distance/1.609
    print(f"You have covered {converted} miles")
elif unit.upper()== "M" :
    converted=distance*1.609
    print(f"You have covered {converted} kms")
else:
    print("Wrong input")
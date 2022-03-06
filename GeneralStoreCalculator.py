# Writing a python program which will keep adding a stream of numbers input by the user.

Total = 0
while(True):
    New_amount = input("Enter the item price or enter N to stop: \n")
    if (New_amount!='N'):
        Total = Total + int(New_amount)
        print(f"Order total so far: {Total}")

    else:
        print(f"Your Bill Total is {Total}")
        print("Thanks for using our Calculator")
        break


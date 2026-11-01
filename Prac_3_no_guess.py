low = 1
high = 100
print("think a no. between 1-100")
while low<=high:
    mid = (low+high)//2
    print("guess no. = ",mid)
    result = input("is the guess correct , higher or lower ?").lower()
    if result == "correct":
        print("guessed no. was correct i.e ",mid)
        break
    elif result == "higher":
        low=mid+1
    elif result == "lower":
        high=mid-1
    else:
        print("invalid feedback try again ! ")
else:
    print("the no. guessed was not in range ")

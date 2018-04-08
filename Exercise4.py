print("program started")
good = 0
limit = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20 
limit = limit + 1

for a in range(1, limit, 1):
    # print(a,"outerloop")
    
    good = 0
    for b in range(1, 21, 1):
                # print(b, "inner loop")
                if a % b ==0:
                    good = good + 1
    # print(good, "is value of good")
    if good == 20:
        print ((a),"is the answer")
        print("program ended1")
        quit()

print("program ended2")

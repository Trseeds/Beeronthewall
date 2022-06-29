import time
global beernum
global origbeernum
#
def count():
    global beernum
    if (beernum) > (0):
        print(f"{beernum} bottles of beer on the wall,")
        time.sleep(1)
        print(f"{beernum} bottles of beer!")
        time.sleep(1)
        print("Take one down,")
        time.sleep(1)
        print("Pass it around")
        time.sleep(1)
        (beernum) = (beernum) - 1
        print(f"{beernum} bottles of beer on the wall!")
        time.sleep(1)
        count()
    else:
        print("No more bottles of beer on the wall!")
        time.sleep(1)
        print("No more bottles of beer,")
        time.sleep(1)
        print("Head to the store,")
        time.sleep(1)
        print("Buy some more,")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print(f"{origbeernum} bottles of beer on the wall!")
        (beernum) = (origbeernum)
        time.sleep(1)
        count()
#
origbeernum = (input("Pick a number, Any (whole) number!\n"))
origbeernum = int(origbeernum)
beernum = (origbeernum)
#
count()

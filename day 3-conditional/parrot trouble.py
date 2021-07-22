#parrot trouble
'''
talking=bool(input())
hr=int(input())
if talking and (hr<7 or hr>20):
    print("true")
else:
    print("false")
'''
talking=bool(input())
hr=int(input())
if talking:
    print("true")
elif hr<7 or hr>20:
    print("true")
else:
    print("false")

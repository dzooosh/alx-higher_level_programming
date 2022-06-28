#!/usr/bin/python3
for i in range(100):
    if (i == 99):
        print("{}".format(i))
        break
    print("{:d}{:0.0f}".format(int(i / 10), i % 10), end=", ")

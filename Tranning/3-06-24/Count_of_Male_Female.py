n=input()
M=n.count("M")
F=n.count("F")
if M==F:
    print("0")
elif M>F:
    print("M")
else:
    print("F")

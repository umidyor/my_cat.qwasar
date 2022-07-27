import sys
for i in sys.argv[1:]:
    f = open(i,"r")
    i = f.read().strip()
    print(i)
    f.close()
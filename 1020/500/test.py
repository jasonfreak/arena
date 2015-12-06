A = 9
B = 22
C = 562
#i = -10000
#while i <= 10000:
#    if (C - A * i) % B == 0:
#        print True
#        exit()
#    i = i + 1
gap = max(abs(A), abs(B)) % min(abs(A), abs(B))
print gap
if C % gap == 0:
    print True
    exit()
print False


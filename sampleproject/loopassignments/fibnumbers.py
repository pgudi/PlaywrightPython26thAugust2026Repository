# 10) Write a program to print first 10 Fibonacci numbers?
'''
0   1   1   2   3   5   8   13    21   34  55
fn=0
sn=1
tn=fn + sn
fourth=sn + tn
fifth= tn + fourth
sixth= fourth + fifth
'''
fn=0
sn=1
print(fn,end=" ")
print(sn,end=" ")

for i in range(1,11):
    tn=fn+sn
    fn=sn
    sn=tn
    print(tn, end=" ")

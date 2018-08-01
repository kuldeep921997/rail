st1 = raw_input("Enter String 1 : ")
st1 = st1.replace(' ', '')
st1=st1.replace(" ", "")

print(st1)

list1 = []
list2 = []
end=0
list3 = []

length = len(st1)
i=0
for i in range(length):
    if i%2==0:
        list1.append(st1[i])
    else:
        list2.append(st1[i])
'''        
for n in list1:
    if n==chr(32):
        list1.remove(n)
        
for m in list2:
    if m==chr(32):
        list2.remove(m)
'''

#lenl2=len(list2)
print(list1)
print(list2)
sto1=''.join(list1)
sto2=''.join(list2)

stfinal=sto1+sto2

print("The ENCRYPTED Format Of String Is : %s" %(stfinal))
hlen=length/2.0
dec, point = divmod(hlen, 1)
if point>=0.5:
    dec=dec+1
rem = length-dec
i=0
k=0
j=0
while i!=length:
    while k!=dec:
        list3.append(list1[k])
        while j!=rem:
            list3.append(list2[j])
            j=j+1
            break
        k=k+1
    i=i+1
    
stfinaldec = ''.join(list3)
print("The DECRYPTED Format Of String Is : %s" %(stfinaldec))

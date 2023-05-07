ct=str(input("ENTER THE CIPHER TEXT : "))
letter="abcdefghijklmnopqrstuvwxyz"
key="qwertyuiopasdfghjklzxcvbnm"
dec=""
for x in ct:
    if x in letter:
        pos=letter.find(x)
        new_char=key[pos]
        dec+=new_char
    else:
        dec+=x
print("PLAIN TEXT : "+dec)


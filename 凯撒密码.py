times=0
plain=input()
value=13
secret_list=list(plain)
secret_list_len=len(secret_list)
 
while times < secret_list_len:
    times=times+1
    ansi_raw=ord(secret_list[0+times-1])

    ansi=ansi_raw+13
 
    word=(secret_list[0+times-1])
 
    if (ansi_raw < 65 or ansi_raw > 90) and word.islower() == False :
        print(word,end='')
 
    elif (ansi_raw < 97 or ansi_raw > 122) and word.isupper() == False:
        print(word,end='')
 
    else:
        while word.isupper() == True and ansi > 90:
            ansi = -26 + ansi 
 
        while word.isupper() == True and ansi < 65:
            ansi = 26 + ansi
 
        while word.isupper() == False and ansi > 122:
            ansi = -26 + ansi
 
        while word.isupper() == False and ansi < 97:
            ansi = 26 + ansi
     
        print(chr(ansi),end='')

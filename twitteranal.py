import sys
f=open("twitter.txt",encoding="utf8")
l2=[]
c=0
c1=0
f.seek(0)
if f.mode == 'r':
  fl =f.readlines()
  
  for x in fl:
    
    x.split()
    
    l=x
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    print(x.translate(non_bmp_map))
    f2=open("positive-words.txt","r")
    if f2.mode == 'r':
        f3 =f2.readlines()
        for x1 in f3:
            l2.append(x1)
    for i in range(0,len(x)):
        if(x[i] in l2):
            c+=1
    c1+=len(x)
print("Positive comments about donaldtrump:",((c+500)/c1)*100,"%")
print("Negative comments about donaldtrump:",100-(((c+500)/c1)*100),"%")

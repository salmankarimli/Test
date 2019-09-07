n=int(input("Dəqiqəni daxil edin "))
#print ("deqiqe =",n)
#if n>=3600:
#   s=n//3600
#else:
s=n//60
d=n-(s*60)
if s>=72:
    s=s-72
if s>=48:
    s=s-48
if s>=24:
    s=s-24
print("Saat=",s," Dəqiqə=",d)
fihrist = open("./algoritmalar_2014_ogrenci_listesi.csv","r") 
isimler=fihrist.read().split("\n") 
def BKDRHash(key):#1.09
    seed = 131 # 31 131 1313 13131 131313 etc..
    hash = 0
    for i in range(len(key)):
        hash = (hash * seed) + ord(key[i])
    return (hash % 150)
slotlist=[] #boş liste

for isim in isimler:
    print(isim," slotu -->",BKDRHash(isim))
    slotlist.append(BKDRHash(isim))
    print("raha",slotlist)

import time # zaman modulunu cagirdim

def tekrar_slotlari_filtirle(slot_list):

    dizi2 = []

    for slot in slot_list:
        if (slot_list.count(slot)!= 1):
            if (slot in dizi2) == False:
                dizi2.append(slot)

    print("Tekrar yapan Slotlar:",dizi2)
    
def DEKHash(key): #1.18
    hash = len(key);
    for i in range(len(key)):
        hash = ((hash << 5) ^ (hash >27)) ^ ord(key[i])
    return (hash % 150)

start = time.clock() #programin calisma ani

#Portaldaki Ogrenci dosyasini acdik okuma modunda
fihrist = open("./algoritmalar_2014_ogrenci_listesi.csv","r")

ogr_isim=fihrist.read().split("\n") #dosyayi okuyub liste haline getirdim


slot_list=[] #bos liste tanimladim

for line in ogr_isim:
    print(line," slotu -->",DEKHash(line))
    slot_list.append(DEKHash(line))



print("\n\n")

print("Slotlarin Siralanamis Hali.",slot_list)

print("\n\n")

tekrar_slotlari_filtirle(slot_list)



end = time.clock()
gecen_sure = end - start #Programin calisma zamani

print("\n")

#Programin Calisma zamanini ekrana bastim
print("Programin calisma suresi:",gecen_sure)




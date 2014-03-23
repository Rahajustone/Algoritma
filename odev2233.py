def tekrar_slotlari_filtirle(slot_list):
	dizi2 = []
        for slot in slot_list:
		if (slot_list.count(slot)!= 1):
			if (slot in dizi2) == False:
		        	dizi2.append(slot)
				print("Tekrar yapan Slotlar:",dizi2)
    
def DJBHash(key): #1.55
	hash = 5381
   	for i in range(len(key)):
     		hash = ((hash << 5) + hash) + ord(key[i])
    	return (hash % 150)

	dosya = open("./algoritmalar_2014_ogrenci_listesi.csv","r")

	isim=dosya.read().split("\n") 


	slotlist=[] 

	for line in isim:
		print(line," slotu -->",DEKHash(line))
	    	slotlist.append(DEKHash(line))



	print("\n\n")

	print("Slotlarin Siralanamis Hali.",slotlist)





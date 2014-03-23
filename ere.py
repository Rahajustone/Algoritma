def RSHash(key):
    a = 378551
    b = 63689
    hash = 0
    for i in range(len(key)):
        hash = hash * a + ord(key[i])
        a = a * b
    return (hash % 150)
def JSHash(key): #1.2
    hash = 1315423911
    for i in range(len(key)):
        hash ^= ((hash << 5) + ord(key[i]) + (hash >2))
    return (hash % 150)
def PJWHash(key): #1.12
    BitsInUnsignedInt = 4 * 8
    ThreeQuarters = ((BitsInUnsignedInt * 3) // 4)
    OneEighth = BitsInUnsignedInt // 8
    HighBits = (0xFFFFFFFF) << (BitsInUnsignedInt - OneEighth)
    hash = 0
    test = 0

    for i in range(len(key)):
        hash = (hash << OneEighth) + ord(key[i])
        test = hash & HighBits
        if test != 0:
            hash = (( hash ^ (test >ThreeQuarters)) & (~HighBits))

    return(hash%150)
def ELFHash(key): #1.07
    hash = 0
    x = 0
    for i in range(len(key)):
        hash = (hash << 4) + ord(key[i])
        x = hash & 0xF0000000
        if x != 0:
            hash ^= (x >24)
            hash &= ~x
    return (hash % 150)
def BKDRHash(key):#1.09
    seed = 131 # 31 131 1313 13131 131313 etc..
    hash = 0
    for i in range(len(key)):
        hash = (hash * seed) + ord(key[i])
    return (hash % 150)
def SDBMHash(key): #1.35
    hash = 0
    for i in range(len(key)):
        hash = ord(key[i]) + (hash << 6) + (hash << 16) - hash;
    return (hash % 150)
def DJBHash(key): #1.55
    hash = 5381
    for i in range(len(key)):
        hash = ((hash << 5) + hash) + ord(key[i])
    return (hash % 150)
def DEKHash(key): #1.18
    hash = len(key);
    for i in range(len(key)):
        hash = ((hash << 5) ^ (hash >27)) ^ ord(key[i])
    return (hash % 150)
def APHash(key):
    hash = 0
    for i in range(len(key)):
        if ((i & 1) == 0):
            hash ^= ((hash << 7) ^ ord(key[i]) ^ (hash >3))
        else:
            hash ^= (~((hash << 11) ^ ord(key[i]) ^ (hash >5)))
        return (hash %150)
print (RSHash ('abcdefghijklmnopqrstuvwxyz1234567890'))
print (JSHash ('abcdefghijklmnopqrstuvwxyz1234567890'))
print (PJWHash ('abcdefghijklmnopqrstuvwxyz1234567890'))
print (ELFHash ('abcdefghijklmnopqrstuvwxyz1234567890'))
print (BKDRHash('abcdefghijklmnopqrstuvwxyz1234567890'))
print (SDBMHash('abcdefghijklmnopqrstuvwxyz1234567890'))
print (DJBHash ('abcdefghijklmnopqrstuvwxyz1234567890'))
print (DEKHash ('abcdefghijklmnopqrstuvwxyz1234567890'))
print (APHash ('abcdefghijklmnopqrstuvwxyz1234567890'))

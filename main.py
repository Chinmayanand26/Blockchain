import datetime
import hashlib
import string
from random import choice, randint



class Block():
    ''' Hashing Mechanism Using sha256 and Local Time '''
    BlockNo = 0 # Block Number.
    HashNo = 0 # Hash Number.
    NextHash = None # Next Hash.
    PervHash = 0x0 # Pervious Hash.
    Data = None
    TimeStamp = datetime.datetime.now()

    # Define init constructor object.
    def __init__(self, Data):
        self.Data = Data

    # Hashing Mechanism.
    def Hash(self):
        H = hashlib.sha256()
        H.update(
            str(self.HashNo).encode('utf-8')+
            str(self.Data).encode('utf-8')+
            str(self.PervHash).encode('utf-8')+
            str(self.TimeStamp).encode('utf-8')+
            str(self.BlockNo).encode('utf-8')            
             )
        return H.hexdigest()
    
    #Convert an object to a string.
    def __str__(self):
        return  "\nBlockNo: " + str(self.BlockNo) + "\nBlockData: " + str(self.Data) + "\nBlockHash: " + str(self.Hash()) + "\nHashNo: " + str(self.HashNo)


class Chain():
    ''' Chain Mechanism '''
    ChallengeSeq = 1 # Hash challenge sequence (when ChallengeSeq > 0 the difficulty increase).
    MaxHashes = 2**32
    Target = 2**(256 - ChallengeSeq)
    Blocks = Block("StrongHashString")
    Head = Blocks

    # Calculate Hash For Challenge Sequence.
    def add(self,Blocks):
        Blocks.BlockNo +=1
        for _n in range(self.MaxHashes):            
            if int(Blocks.Hash(), 16) <= self.Target:
                print(Blocks)
                break
            else:
                Blocks.HashNo += 1


class Mine():
    ''' Mine Mechanism '''
    # Test Hashing For Multi Threads.
    for n in range(10):
        RandomStr = "".join(choice(string.hexdigits) for x in range(randint(2, 64)))     
        Chain().add(Block(str(RandomStr)))
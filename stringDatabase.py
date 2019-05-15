class stringDatabase :
    list=[]
    def __init__(self) :
        with open("four_letters.txt","r") as file_pointer :
            i=0;
            for line in file_pointer :
                wordlist=line.split()
                for eachword in wordlist :
                    self.list.append(eachword)






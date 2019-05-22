"""
@author : Maqsood
"""
class stringDatabase :
    """
    stringDatabase class used to store the Words
    variable list is a list Type
    """
    list=[]
    def __init__(self) :
        """
            init is a consttrctor of the class that reads the file into list.
        """
        with open("four_letters.txt","r") as file_pointer :
            i=0;
            for line in file_pointer :
                wordlist=line.split()
                for eachword in wordlist :
                   self.list.append(eachword)






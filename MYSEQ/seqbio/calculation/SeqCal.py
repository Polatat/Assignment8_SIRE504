# Seqcal module
def countBase(seq,base):
    #   seq eg. "ATGC"
    #   base eg. "A","T"
    return seq.count(base.upper())


def gcContent(seq):
    return float(((countBase(seq,'G') + countBase(seq,'C'))/len(seq)))

def atContent(seq):
    return float(((countBase( seq,'A')+ countBase(seq,'T'))/len(seq)))

def countBasesDict(seq):
    baseM = {}
    for base in seq.upper():
        baseM[base] = baseM.get(base,0) +1 # correct
        # baseM[base] = len(base) + 1 # wron version
    return baseM

if __name__ == "__main__":
    seq ="ATCGATGTGTCTCTC"
    print("gcpercentage")
    print(gcContent(seq))
    print("atpercentage")
    print(atContent(seq))
    print("countbase")
    print(countBasesDict(seq))

    



    
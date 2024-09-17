# import each funcitons
from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.dnaconvert import *

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    ) 
    # subparsers.required = True
# define eachc commands
    # gcContent find
    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    # countbase 
    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r","--revcomp", action ='store_true',
                                help= " Convert DNA to reverse-complementary")
    # transcription
    transcr_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcr_command.add_argument("-s","--seq", type=str, default= None,
                             help = "Provide sequence")
    transcr_command.add_argument("-r","--revcomp", action ='store_true', 
                               help= " Convert DNA to reverse-complementary")
    #translation
    transla_command = subparsers.add_parser('translation', help='Convert DNA->protein')
    transla_command.add_argument("-s","--seq", type=str, default= None,
                             help = "Provide sequence")
    transla_command.add_argument("-r","--revcomp", action ='store_true', 
                               help= " Convert DNA to reverse-complementary")
    # enztarget
    enz_command = subparsers.add_parser('enzTargetsScan', help ='Find restriction enzyme')
    enz_command.add_argument("-s","--seq", type=str, default= None,
                             help = "Provide sequence")
    enz_command.add_argument("-e","--enz", type =str, default = None,
                             help=  "Enzyme name")
    enz_command.add_argument("-r","--revcomp", action='store_true', 
                               help= " Convert DNA to reverse-complementary")
    
    #parser.print_help()
    return parser


#input

def test():
    # Input
# test GC content
    # parser = argparserLocal()
    # args = parser.parse_args(["gcContent","-s","ATCGCTTTTTTCGCGCG",])
    # print("Input",args.seq,"\nGC content", gcContent(args.seq))  
 # test CountBase
    # parser = argparserLocal()
    # args = parser.parse_args(["countBases","-s","ATGGGccGTAGAATTCTTGCaaGCCCGT","-r"])
    # seq = args.seq
    # if args.revcomp:
    #     seq = reverseComplementSeq(seq)
    # print("Input",args.seq,"\ncountBases =", countBasesDict(seq))  

 # test Transcription
    # parser = argparserLocal()
    # args = parser.parse_args(["transcription","-s","ATGGGccGTAGAATTCTTGCaaGCCCGT","-r"])
    # seq = args.seq
    # if args.revcomp:
    #     seq = reverseComplementSeq(seq)
    # print("Input",args.seq,"\nTranscription =", dna2rna(seq))   

## test Translation
#     parser = argparserLocal()
#     args = parser.parse_args(["translation","-s","ATGGGccGTAGAATTCTTGCaaGCCCGT","--revcomp"])
#     seq = args.seq
#     if args.revcomp:
#         seq = reverseComplementSeq(seq)
#     print("Input",args.seq,"\nTranslation=", dna2protein(seq)) 
# # test enzTargetsScan
    parser = argparserLocal()
    args = parser.parse_args(["enzTargetsScan","-s","atgggccgtagaattcttgcaagcccgtggatccaagctt","-e","BamHI","-r"])
    seq = args.seq
    enz = args.enz
    if args.revcomp:
        seq = reverseComplementSeq(seq)
    print("Input",args.seq,"\n" f'{enz} sites =', enzTargetsScan(seq,enz)) 






    
def main():
     parser = argparserLocal()
     args = parser.parse_args()

     if args.seq == None:
          print(("------\nError: You do not provide -s or --seq\n------\n"))
    
     else:
        seq = args.seq.upper()

# if -r or --revcomp represent.
     
    #  print('check1')
     # gc content
     if args.command == 'gcContent':
         if args.seq == None:
             exit(parser.parse_args(['gcContent','-h']))

         print("Input",args.seq,"\nGC content =", gcContent(seq) )   

    # countbase 
     elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        
        print("Input",args.seq,"\ncountBases =", countBasesDict(seq))

    #transcription
     elif args.command == 'transcription':
         if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
         if args.revcomp:
            seq = reverseComplementSeq(seq)
        
         print("Input",args.seq,"\nTranscription =", dna2rna(seq))
    
    #translation
     elif args.command =='translation':
         if args.seq == None:
             exit(parser.parse_args(['translation','-h']))
         if args.revcomp:
            seq = reverseComplementSeq(seq)
        
         print("Input",args.seq,"\n Translation =", dna2protein(seq))
        

    #enztarget 
     elif args.command == 'enzTargetsScan':
         enz = args.enz
         if args.seq == None:
             exit(parser.parse_args(['enzTargetsScan','-h']))
         elif args.enz == None:
             print("------\nError: You do not provide -e or --enz\n------\n")
             exit(parser.parse_args(['enzTargetsScan','-h']))
         elif args.revcomp:
            seq = reverseComplementSeq(seq)
         print("Input",args.seq,"\n" f"{enz} sites =" , enzTargetsScan(seq,enz))


# test
if __name__ == "__main__":
    # main()
    test()      

         



    
    



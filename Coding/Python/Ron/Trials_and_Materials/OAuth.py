import time

def goFlush(length=100):

    for l in range(length):
        prog = "#"*l
        prog_bg = "_"*(length-l)
        print(f"{l:>3}% {prog}{prog_bg}", end="\r", flush=True)
        time.sleep(.01)
    print("DONE!"+" "*l)

# goFlush()

def QAuth2():
    header = 1
    tail = 1
    options = list("ABCDEF")
    txt ="""Authorization Request
Authorization Grant
Authorization Grant
Access Token
Access Token
Protected Resource"""
    contents = txt.split("\n")
    gap_amt = int(len(options)/2)-1
    line_amt = len(options)+gap_amt*3
    l_model = "client"
    r_model_1 = """Resource
Owner
Authorization
Server
Resource
Server"""



    print(line_amt)

    for i,option in enumerate(options):
        if i%2 == 0:
            print(f"--({option}){contents[i]:-^30}>",end="\n"*2)
        else:
            print(f"<-({option}){contents[i]:-^30}-",end="\n"*4)


QAuth2()

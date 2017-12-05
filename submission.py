## Submission.py for COMP6714-Project1
from math import log

###################################################################################################################
## Question No. 0:
def add(a, b): # do not change the heading of the function
    return a + b




###################################################################################################################
## Question No. 1:

def gallop_to(a, val):# do not change the heading of the function
    pass # **replace** this line with your code


###################################################################################################################
## Question No. 2:

def Logarithmic_merge(index, cut_off, buffer_size): # do not change the heading of the function
    #pass # **replace** this line with your code
    index = index[:cut_off]
    result = [[]]
    if (buffer_size==0):
        return result
    z0 = []
    while index!=[] or len(z0)==buffer_size:
        if len(z0)<buffer_size:
            if index!=[]:
                z0.append(index[0])
                index = index[1:]
        else:
            for i in range (len(result)):
                if (len(result[i])+len(z0)<=buffer_size*pow(2,i)):
                    result[i] +=z0
                    z0 = []
                    break
                else:
                    z0+=result[i]
                    result[i]=[]
                    continue
            if z0!=[]:
                result.append(z0)
                z0=[]
    for i in range(len(result)):
        result[i] = sorted(result[i])
    #if z0!=[]:
    result = [sorted(z0)]+result
    #result.reverse()
    return result

# index = [15, 46, 19, 93, 73, 64, 33, 80, 73, 26, 22, 77, 27]
# result = Logarithmic_merge(index, 10, 5) #cut_off = 10, initial buffer_size = 3
# print(result) # expect to see a list of lists
###################################################################################################################
## Question No. 3:
def decode_step1(inputs):
    for i in range(len(inputs)):
        if inputs[:i+1].endswith("0"):
            return pow(2, i)+int(inputs[i+1:2*i+1],2),inputs[2*i+1:]
            #return inputs[:i+1],inputs[i+1:2*i+1],inputs[2*i+1:]
#def gamma_decode_step2(input1,input2):
#    return pow(2, len(input1)-1)+int(input2,2)
#
def delta_decode_step(inputs):
    for i in range(len(inputs)):
        if inputs[:i+1].endswith("0"):
            kd = int(inputs[:i],2)+int(inputs[i+1:2*i+1],2)
            return pow(2,kd)+int(inputs[2*i+1:2*i+1+kd],2),inputs[2*i+1+kd:]

def decode_gamma(inputs):# do not change the heading of the function
    result = []
    while inputs!="":
        res,inputs = decode_step1(inputs)
        result.append(res)
    return result

#    pass # **replace** this line with your code

def decode_delta(inputs):# do not change the heading of the function
    result = []
    while inputs!="": # **replace** th   is line with your code
        res,inputs = delta_decode_step(inputs)
        result.append(res)
    return result

def rice_decode_step1(inputs,b,inc):
    for i in range(len(inputs)):
        if inputs[:i+1].endswith("0"):
            #print(int(inputs[i+1:i+1+inc],2))
            return i*b+int(inputs[i+1:i+1+inc],2), inputs[i+1+inc:]

def decode_rice(inputs, b):# do not change the heading of the function
    inc = int(log(b, 2))
    result = []
    while inputs!="": # **replace** th   is line with your code
        res,inputs = rice_decode_step1(inputs,b,inc)
        result.append(res)
    return result


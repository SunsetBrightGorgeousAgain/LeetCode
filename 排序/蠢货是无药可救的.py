def AdjustArray(input_list,start,end):
    i = start
    j = end
    base = input_list[i]
    while i<j:
        while i<j and input_list[j]>=base:
            j-=1
        if (i<j):
            input_list[i],input_list[j] = input_list[j],input_list[i]
            i+=1

        while i<j and input_list[i]<base:
            i+=1
        if(i<j):
            input_list[i],input_list[j] = input_list[j],input_list[i]
            j-=1
    input_list[i] = base

    return input_list

print(AdjustArray([1,4,5,3],0,3))
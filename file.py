def print_dict(dict):
    for k in dict:
        print(k,dict[k])

file_name=input("Type the file name: ")
word_counter=dict()
with open(file_name) as T:
    w=T.read().split(" ")
    for i in w:
        if i in word_counter:
            word_counter[i]+=1
        else :
            word_counter[i]=1 

print_dict(word_counter)

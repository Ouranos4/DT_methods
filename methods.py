import os
list_methods= []
for method in dir(list):
    if method.startswith("__"):
        continue
    else:
        list_methods.append(method)

str_methods= []
for method in dir(str):
    if method.startswith("__"):
        continue
    else:
        str_methods.append(method)

tuple_methods= []
for method in dir(tuple):
    if method.startswith("__"):
        continue
    else:
        tuple_methods.append(method)

dict_methods= []
for method in dir(dict):
    if method.startswith("__"):
        continue
    else:
        dict_methods.append(method)

set_methods= []
for method in dir(set):
    if method.startswith("__"):
        continue
    else:
        set_methods.append(method)

bool_methods= []
for method in dir(bool):
    if method.startswith("__"):
        continue
    else:
        bool_methods.append(method)

int_methods= []
for method in dir(int):
    if method.startswith("__"):
        continue
    else:
        int_methods.append(method)

float_methods= []
for method in dir(float):
    if method.startswith("__"):
        continue
    else:
        float_methods.append(method)

title_s = ['List','Str','Tuple','Dictionary','Set','Boolean','integer','float']
class_es= [list_methods,set_methods,tuple_methods,dict_methods,set_methods,bool_methods,int_methods,float_methods]
max_len=0
for class_ in class_es:
    if len(class_)>max_len:
        max_len=len(class_)
with open(r"Methods.txt", "w") as f:
    for title in title_s:
        print(title,end="")
        print(" " * (30 - len(title)), end="")
        f.write(title)
        f.write(" " * (30 - len(title)))

    print()
    f.write("\n")


    for i in range(max_len):
        print()
        f.write("\n")
        for class_ in class_es:
            if len(class_)<=i:
                print("--------", end='')
                print(" " * 22, end="")
                f.write("--------")
                f.write(" " * 22)
            else:
                print(class_[i],end="")
                print(" "*(30-len(class_[i])), end='')
                f.write(class_[i])
                f.write(" " * (30 - len(class_[i])))
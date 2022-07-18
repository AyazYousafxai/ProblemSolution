list_=['a','a','a','a','b','c','c','d','d','ayaz','ayaz','shaheroom','ayaz']
output_list=[]
check_list=[]
count = 0
list_=sorted(list_)
for i,v in enumerate(list_):
    if v in check_list:
        if count==1:
            output_list.append(v+"_"+str(count))
        count+=1
        check_list.append(v)
        output_list.append(v+"_"+str(count))

    else:
        count=1
        check_list.append(v)
print(output_list)

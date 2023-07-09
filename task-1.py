str_list = input("Enter a string \n")
str_list = str_list.split(" ")
cnt_deleted = 0
for i in range(len(str_list)):
    i -= cnt_deleted
    if len(str_list[i]) > 3:
        str_list.pop(i)
        cnt_deleted += 1
print(str_list)

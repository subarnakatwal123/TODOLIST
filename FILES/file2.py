# with open("alpha.txt", "w+") as file:
#     for i in range(4):
#         file.write(f"Line{i} \n")
#     file.seek(0)
#     print(file.read())
#     file.seek(0)

#     filelist = list(file.read().split())
#     print(filelist)
#     if "Line2" in filelist:
#         filelist[filelist.index("Line2")] = "Medium"
#     file.seek(0)
#     print(filelist)
#     file.truncate(0)
#     file.seek(0)
#     for i in range(len(filelist)):
#         file.write(f"{filelist[i] }\n")
#     file.seek(0)
#     print(file.read())

with open("rdr.txt", "w+") as file:
    for i in range(4):
        file.write(f"Line{i}\n")
    
    file.seek(0)
    lines = file.readlines()
    if "Line2\n" in lines:
        lines[lines.index("Line2\n")] = "Medium\n"
    
    file.seek(0)
    file.writelines(lines)
    file.seek(0)
    print(file.read())


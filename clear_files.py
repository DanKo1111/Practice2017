import os

def clear_directory(inpath, outpath="", delete=False):
    if not outpath:
        outpath = inpath
    try:
        os.makedirs(outpath)
    except:
        pass
    for i in os.walk(inpath):
        if i[2]:
            for j in i[2]:
                file_path = i[0] + "\\" + j
                file_result = ""
                a = open(file_path, "r", encoding="utf-8")
                for k in a:
                    parts = k.split()
                    if int(parts[2]) < 1919:
                        file_result += k
                        file_result += "\n"
                a.close()
                a = open(outpath + "\\" + j, "w", encoding="utf-8")
                a.write(file_result)
                a.close()
                if delete:
                    os.remove(file_path)


                
clear_directory("H:\\Files\\Files6", "H:\\Files\\Files6_cleared", False)

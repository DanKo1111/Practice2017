import os, time

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
                try:
                    file_path = i[0] + os.sep + j
                    file_result = open(outpath + os.sep + j, "a", encoding="utf-8")
                    a = open(file_path, "r", encoding="utf-8")
                    for k in a:
                        parts = k.split()
                        if int(parts[2]) < 1919:
                            file_result.write(k + "\n")
                    a.close()
                    file_result.close()
                    if delete:
                        os.remove(file_path)
                    print("Файл ", file_path, " успешно обработан ", current_time())
                except MemoryError:
                    print("Ошибка памяти:", j, "; ", current_time())
                except:
                    print("Ошибка в файле:", j, "; ", current_time())
                    

def current_time():
    fin_time = time.localtime()
    return str(fin_time[2]) + "." + str(fin_time[1]) + "." + str(fin_time[0]) + " || " + str(fin_time[3]) + "h " + str(fin_time[4]) + "m " + str(fin_time[5]) + "s"

                
clear_directory("H:\\Files\\Files6_2", "H:\\Files\\Files6_cleared", True)

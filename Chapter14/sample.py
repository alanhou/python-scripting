try:
    f = open('logfile', 'r')
    print(f.read())
    f.close()
except:
    print("File not found. Please check whether the file is present in you directory or not.")

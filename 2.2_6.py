with open("filehandling/demo4.txt","a+") as f:
    f.write("good evening")
    f.seek(0)
    print(f.read())
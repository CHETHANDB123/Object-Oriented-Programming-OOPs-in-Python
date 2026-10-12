import json
with open("filehandling/sample.json","w+") as f:
    d={1:"alice",2:"ben"}
    json.dump(d,f)
    #f.write(json_str)
    print(json)
    print(f.tell())
    f.seek(0)
    #data=f.read()
    pobject=json.load(f)
    print(pobject,type(pobject))
    
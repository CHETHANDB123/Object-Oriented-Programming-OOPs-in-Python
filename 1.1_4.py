'''
print(__name__)  #only when this module is directly exectued
                 #get actual modulenmae,when __name__is exectued as a result of importing package3.file1
'''
def add(a,b):
    print(a+b)
#value of __name__is "package3.file1" to import file1 so __name__!=__main__
if __name__=="__main__":
    add(10,10)                 

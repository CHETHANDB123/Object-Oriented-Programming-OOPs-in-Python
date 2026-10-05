#finally
print("Start")
try:    # This acts like a "if"
    print("hello")
    # print(9/0)
except Exception:
    print("exception handling")
else:
    print("else block executed when no exception occurs")
finally:
    print("finally executes always wrt try block")
print("End")  
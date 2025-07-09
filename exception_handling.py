
try:
    print(X)  
except NameError:
    print("Variable X is not defined.")  
else:
    print("evrything went wrong")
    
    
X = -1

if X < 0:
    raise E
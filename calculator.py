def calculator(command,a,b):
    if(command == 'sum'):
        return a + b
    if(command=='sub'):
        return a-b
    if(command=='div'):
        return a/b
    if(command=='mult'):
        return a*b
    

result = calculator('sum',3,4)
print(result)

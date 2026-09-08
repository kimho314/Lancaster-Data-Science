def add(a,b):
    result = a+b
    return result

def sub(a,b):
    result = a-b
    return result

def multi(a,b):
    result = a*b
    return result

def div(a,b):
    if b == 0:
        raise Exception("zero is not allowed for b")
    result = a/b
    return result

print(add(1,2))
print(sub(3,2))
print(multi(3,5))
print(div(4,2))
print(div(4,0))
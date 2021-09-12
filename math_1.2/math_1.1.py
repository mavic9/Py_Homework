# count of vector magnitude

vector = list((input('Enter coordinates of vector in any dimention separated by space: ')).split(' '))

def vector_len(vector: list) -> float:
    a = 0
    for i in vector:
        a += float(i)**2
    l = a**0.5
    return l

print(f'The magnitude of the vector is {vector_len(vector)}')

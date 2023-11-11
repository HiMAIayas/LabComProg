
def LeftRotate(arr,n):
    return arr[n:] + arr[:n]
def RightRotate(arr,n):
    return arr[5-n:]+ arr[:5-n]

arr=[i for i in input("Enter 5 inputs: ").split()]
rotate = input("Enter an integer number of rotations (0-4): ")
if rotate.isnumeric() and 4>=int(rotate)>=0:
    n=int(rotate)
    print(f'The left-rotated list: {LeftRotate(arr,n)}')
    print(f'The right-rotated list: {RightRotate(arr,n)}')
else:
    print('Error!')

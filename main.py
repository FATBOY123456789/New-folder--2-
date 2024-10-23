class A:
    def __init__(self,s):
        self.s=s
    def reverse(self):
        return self.s[::-1]
s1=input('Enter a string: ')
a1=A(s1)
print('Reverse is', a1.reverse())
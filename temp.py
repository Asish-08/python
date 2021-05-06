#Write a Python program to convert temperatures to and from celsius, fahrenheit.
print('mention if the readngs are in celcius or farienheit')
temp=input()
if temp =='celcius':
    cel=int(input())
    far=1.8*cel + 32
    print(far)
    print('the farienheit readings:',far)
elif temp =='farienheit':
    far=int(input())
    cel=(5/9)*far - 32
    print('the celcius readings:',cel)

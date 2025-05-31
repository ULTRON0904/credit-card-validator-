sun_odd_digits=0
sum_even_digits=0
total=0

credit_card=input('Enter a credit card:')
credit_card=credit_card.replace("-","")
credit_card=credit_card.replace(" ","")
credit_card=credit_card[::-1]

for a in credit_card[::2]:
    sun_odd_digits+=int(a)

for a in credit_card[1::2]:
    a=int(a)*2
    if a >=10:
        sum_even_digits+=(1+(a%10))
    else:
        sum_even_digits+=a

if total%10==0:
    print('VALID')
else:
    print('INVALID')

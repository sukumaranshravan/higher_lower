import random

hitters=[{'Rohit Sharma': 'Indian Batsman','No of 6 hits':582},{'Yuvraj Singh': 'Indian Batsman','No of 6 hits':251},
{'Sachin Tendulkar': 'Indian Batsman','No of 6 hits':264},{'Chris Gayle': 'West Indies Batsman','No of 6 hits':553},
{'Shahid Afridi': 'Pakistani Batsman','No of 6 hits':476},{'Brandon McCullum': 'New Zealand Batsman','No of 6 hits':398},
{'Martin Guptil': 'New Zealand Batsman','No of 6 hits':383},{'MS Dhoni': 'Indian Batsman','No of 6 hits':359},
{'Eoin Morgan': 'English Batsman','No of 6 hits':346},{'AB de Villers': 'South African Batsman','No of 6 hits':328},
{'David Miller': 'South African Batsman','No of 6 hits':244},{'Jose Butler': 'English Batsman','No of 6 hits':317},
{'David Warner': 'Australian Batsman','No of 6 hits':300},{'Glen Maxwell': 'Australian Batsman','No of 6 hits':272},
{'Virat Kohli': 'Indian Batsman','No of 6 hits':292},{'Rose Taylor': 'New Zealand Batsman','No of 6 hits':273},]

A=random.choice(hitters)
B=random.choice(hitters)

for key,value in A.items():
    player_1=key
    description=value
    break
print("1).",player_1,",",description,end='  v/s  ')

for key,value in B.items():
    player_2=key
    description=value
    break
print("2).",player_2,",",description,'\n')

choose=int(input("Who hits More 6s ?"))
points=[]
x=A['No of 6 hits']
y=B['No of 6 hits']
if choose==1:
    you=x
    print(f"{player_1} hits {x} sixes")
    print(f"{player_2} hits {y} sixes")
    if you>y:
        print("You Won")
    else:
        print("Game over")
else:
    you=y
    print(f"{player_1} hits {x} sixes")
    print(f"{player_2} hits {y} sixes")
    if x>y:
        print("Game Over")
    else:
        print("You Won")

def single_ton(cls):
    L=[]
    def inner():
        if len(L)==0:
            obj=cls()
            L.append(obj)
        return L[0]
    return inner
@single_ton
class leo:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('Enter Number of Tickets : '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('Tickets Booked Successfully')
        else:
            print('Tickets not Available')
@single_ton
class jawan:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('Enter Number of Tickets : '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('Tickets Booked Successfully')
        else:
            print('Tickets not Available')
@single_ton
class pushpa2:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('Enter Number of Tickets : '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('Tickets Booked Successfully')
        else:
            print('Tickets not Available')
@single_ton
class salar:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('Enter Number of Tickets : '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('Tickets Booked Successfully')
        else:
            print('Tickets not Available')

def Bookmyshow():
    print('1->LEO\n2->JAWAN\n3->PUSHPA 2\n4->SALAR')
    option=int(input('choose an option :'))
    if option==1:
        l1=leo()
        l1.booking()
    elif option==2:
        j1=jawan()
        j1.booking()
    elif option==3:
        p1=pushpa2()
        p1.booking()
    elif option==2:
        s1=salar()
        s1.booking()
    else:
        print('choose a valid option')
while True:
    Bookmyshow()
    print('_'*30)
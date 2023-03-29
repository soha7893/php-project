class Bus:
    def __int__(self,bus_num,destination,seat_count):
        self.bus_num=bus_num
        self.destination = destination
        self.seat_count = seat_count
bus1= Bus (1,'from Gaza to yafa',2)
bus2=Bus (2,'from gaza to Hebron',25)
bus3=Bus(3,'from gaza to Rafah',25)
bus4=Bus(4,'from gaza to Jersusalem',25)
bus5=Bus (5,'from gaza to khanyunis',25)
class Shuttlebus:
    seat = []
    def __init__(self,username,user_nu):
        self.username = username
        self.user_nu = user_nu

    def book_seats(self,seat):
       username = input('Enter your name :')
       user_nu = input('Enter your user number :')
       s1 = seat(username,user_nu)
       seat_num = 0
       if len(seat) < 25:
           seat . append(s1)
           for s1 in seat:
               seat_num=seat_num+1
           print('your seat has been booked successfully and your seat is ',s1.get_seat_num())
       else:
           print('you cant book, the seat is full')

    def see_seat_availability(self,seat):
           if len(seat)>25:
               print ('All seats have been booked')
           else:
               s1=int(input('Enter your seat ' ))
               found=0
               for s in seat:
                   if s.get_user_nu()==self.user_nu :
                       found=1
                       print('the user name is ,',s.get_user_nu(),s.get_seat_num())
               if found==0:
                   print('the user number dosent exist, please try later')

    def display_all(self,seat):
        if len(seat)==25:
            print('you cant book')
        else:
            for s in seat:
                print('the seat is ',s.get_user_nu(),s.get_seat_num())

def menu():
    print('Enter 1 if you want to book a seat')
    print('Enter 2 if you want to see availability of seat')
    print('Enter 3 if you want to display all seat')
    print('Enter 4 if you want to exit')


username=input('Enter your name ')
user_nu = int(input('Enter your number '))
obj = Shuttlebus(username,user_nu)
menu()

while (True):
    choice = int(input('Choose a number '))
    if choice == 1:
        obj.book_seats(Shuttlebus.seat)
        menu()
    elif   choice==2:
        obj.see_seat_availability(Shuttlebus.seat)
    elif choice==3:
        obj.display_all(Shuttlebus.seat)
    elif choice==4:
        break
    else:
        print("Wrong choice, please try again ")
        menu()
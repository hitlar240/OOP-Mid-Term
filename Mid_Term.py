class Star_Cinema:
    hall_list = [] # list of (Hall)objects

    def entry_hall(cls,hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.__show_list = [] 
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id,movie_name,time))
        self.seats[id] = [[0 for j in range(self.cols)] for i in range(self.rows)]

    def view_show_list(self):
        for show in self.__show_list:
            print(f'Movie:{show[1]} ID:{show[0]} Time:{show[2]}')

    def view_available_seats(self,id):
        for row in self.seats[id]:
            print(row)

    def book_seats(self,id,seat):
        for st in seat:
            self.seats[id][st[0]][st[1]] = 1

hall_01 = Hall(10,7,'A-111')
hall_01.entry_show('B101','Molla Barir Bou','04/12/23 at 3.00pm')
hall_01.entry_show('B102','Aynabaji','04/12/23 at 5.00pm')

hall_02 = Hall(12,8,'B-123')
hall_02.entry_show('E201','Spiderman','04/12/23 at 5.00pm')
hall_02.entry_show('E202','Superman','04/12/23 at 7.00pm')

hall_03 = Hall(8,10,'C-240')
hall_03.entry_show('H301','PK','04/12/23 at 7.00pm')
hall_03.entry_show('H302','KGF','04/12/23 at 9.00pm')


while(True):
    print('1. Running Shows')
    print('2. Avaiable Seats')
    print('3. Book Ticket')
    print('4. Exit')

    choise = int(input('Enter Option: '))
    if choise == 1:
        for hall in Hall.hall_list:
            print('---------------------------------')
            print(f'Hall No: {hall.hall_no}')
            hall.view_show_list()
            print('---------------------------------')

    elif choise == 2:
        flag = False
        id = input('Enter Show ID: ')
        for hall in Hall.hall_list:
            if id in hall.seats.keys():
                flag = True
                hall.view_available_seats(id)
        if flag == False:
            print('Invalid ID!')

    elif choise == 3:
        flag = False
        id = input('Enter Show ID: ')
        for hall in Hall.hall_list:
            if id in hall.seats.keys():
                flag = True
                seats = []
                n = int(input("Number of seats?: "))
                while(n != 0):
                    row = int(input("Enter Row:"))
                    col = int(input("Enter Col:"))
                    if row > hall.rows or col > hall.cols or row < 0 or col < 0:
                        print("Envalid row or col!")
                        continue
                    if hall.seats[id][row][col] == 1:
                        print("Already Booked!")
                        continue
                    seats.append((row,col))
                    n -= 1
                hall.book_seats(id,seats)
                print('Booked Successfully')
        if flag == False:
            print('Invalid ID!')

    else:
        break
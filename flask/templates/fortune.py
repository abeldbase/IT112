print("Fortune Teller!")
print("You will select a color listed bellow and a numer 1-4 and know your fortune !")
c = input("\nDo you want to know yor fortune! ('y' or 'n'): ")

while c == 'y':
    color = input("\nChoose a color from - Red,Yellow,Blue, Green,  : ")

    if color == 'Yellow' or color == 'yellow' or color == 'YELLOW' or color == 'Green' or color == 'green' or color == 'GREEN'
    'Blue' or color == 'blue' or color == 'BLUE' or color == 'Red' or color == 'red' or color == 'RED':

        while True:

            number = int(input("Select a number from - 1, 2, 3, 4: "))

            if number == 1:
                print("\nYou are very lucky!!")
                break
            elif number == 2:
                print("\nYou will become a reach person  soon!")
                break
            elif number == 3:
                print("\nYou will get a new job next year!")
                break
            elif number == 4:
                print("\nYou will visit Paris after 2 years!")
                break
            else:
                print("Numbers - 1, 2, 3, 4 are the only numbers allowed!")

        continue

    c = input("\nDo you want to try again? ('y' or 'n'): ")

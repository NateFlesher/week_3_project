from time import sleep

class Parking_Garage():
    def __init__(self, name, tickets, parkingSpaces, cost_per_hour):
        self.name = name
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.cost_per_hour = cost_per_hour


    def takeTicket(self):
        '''
        takeTicket starts the simulation by having the user enter the garage
        decrements tickets and parkingSpaces by 1 for the 1 user that has entered
        displays amount of parkingSpaces available prior and after entrance
        '''
        print(f"Welcome to the East Street Garage\n---------------------------------\nCurrent Rate: ${self.cost_per_hour} per hour\n---------------------------------")
        if self.parkingSpaces <= 0:
            print("Sorry, there are no spaces available at the moment... Please come back later. ")
            return
        else:
            print(f"There are {self.parkingSpaces} parking spaces available at the moment. Please take your ticket.")
            self.tickets -= 1
            self.parkingSpaces -= 1
            sleep(2)
            print(f"\n...There are now {self.parkingSpaces} parking spaces available. ")
            



    def payForParking(self):
        '''
        payForParking allows user to input amount of hours they stayed in garage
        displays the total cost based on amount of hours
        first 2 hours are free
        '''
        parking_time = int(input("\nThis is an honor system. How many HOURS were you parked in the garage? "))
        if parking_time > 2:
            parking_time -= 2
            print(f"\nThe first 2 hours were free! Your total today is ${self.cost_per_hour*parking_time}.")
            sleep(1)
            print("\n...All checked out! Have a great rest of your day!")
            sleep(2)
            print(f"\n...There are now {self.parkingSpaces} parking spaces available in the East Street Garage. ")
            return
        elif parking_time <=2:
            print(f"\nThe first 2 hours are free. You're good to go!\nHave a nice day! ")   
            return         
        else:
            print("This is not a valid time.")
        
    def garageInfomercial(self):
        '''
        this method interacts with the garage user and suggests local atttractions
        '''
        yes_or_no = input("Hey friend, while you're here in Orlando I'd like to suggest a few local attractions... are you interested? (Y/N) ")
        if yes_or_no.lower() == 'y':
            while True:
                topic = input("Let me know a topic you're interested in... (food/amusement park/nature): ")
                if topic.lower() == 'food':
                    print("Feel free to check out:\n - NYPD Pizza | 2589 S Hiawassee Rd, Orlando, FL 32835-6316\n - The Gnarly Barley | 1407 N Orange Ave, Orlando, FL 32804-6410\n - Sear+Sea | 14900 Chelonia Parkway JW Marriott Orlando Bonnet Creek, Orlando, FL 32821")
                    more = input("\nWould you like to explore one of the other suggested topics? (Y/N) ")
                    if more.lower() == 'y':
                        continue
                    elif more.lower() == 'n':
                        print("\nGreat, I'll see you when you're ready to leave. ")
                        break     
                elif topic.lower() == 'amusement park':
                    print("Feel free to check out:\n - Universal Studios \n - Disney World\n - SeaWorld")
                    more = input("\nWould you like to explore one of the other suggested topics? (Y/N) ")
                    if more.lower() == 'y':
                        continue
                    elif more.lower() == 'n':
                        print("Great, I'll see you when you're ready to leave. ")
                        break     
                elif topic.lower() == 'nature':
                    print("Feel free to check out:\n - Lake Eola Park\n - Harry P Leu Gardens\n - Tibet-Butler Nature Preserve ")
                    more = input("\nWould you like to explore one of the other suggested topics? (Y/N) ")
                    if more.lower() == 'y':
                        continue
                    elif more.lower() == 'n':
                        print("Great, I'll see you when you're ready to leave. ")
                        break     
        elif yes_or_no.lower() == 'n':
            print("Sounds good! We'll talk again when you're ready to leave the garage. ")
        else:
            print("Not a valid response.")


    def leaveGarage(self):
        '''
        leaveGarage simulates the exit
        invokes payForParking
        increments tickets and parkingSpaces by 1 for the 1 user if pay+exit is chosen
        '''
        print("\nOh...so you want to exit the garage now...")
        pay_now = input("Are you sure you would you like to pay right now and exit? (Y/N) ")
        if pay_now.lower() == 'y':
            print("***You have 15 minutes to exit, or risk having your car towed!*** ")
            self.tickets +=1
            self.parkingSpaces +=1
            self.payForParking()
        elif pay_now.lower() == 'n':
            print("Okay, let us know when you are ready to pay and exit.")
            return
        else:
            print("That is not a valid response")
    

    
    def run(self):
        '''
        Method that simulates garage entrance, pay, infomercial, exit
        '''
        self.takeTicket()
        sleep(2)
        self.garageInfomercial()
        sleep(4)
        self.leaveGarage()


##test
garage = Parking_Garage('East Street Garage', 200, 200, 1)
garage.run()


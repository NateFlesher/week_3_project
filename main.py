from time import sleep
# We are implementing this function for the sake of using breaks to represent information being processed


class Parking_Garage():
    # this class is being made in order to define as many functions as the program needs to run, then creating a function that runs said functions in a specific order
    def __init__(self, name, tickets, parkingSpaces, cost_per_hour):
        self.name = name
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.cost_per_hour = cost_per_hour
# Here we are using the init function to allow us to define certain attributes of the information we are going to be running through the program, these attributes will be used for different functions within the class
# Self is representative of the class itself which we will attach to a separate variable later. This is what is going to be ran through the functions, pulling and using the attributes set up when applicable.
# Name for the name of garage, tickets and parkingSpaces represent the available spots left in the garage, and the cost_per_hour is well cost per hour.

    def takeTicket(self):
        '''
        takeTicket starts the simulation by having the user enter the garage
        decrements tickets and parkingSpaces by 1 for the 1 user that has entered
        displays amount of parkingSpaces available prior and after entrance
        '''
        print(
            f"Welcome to the East Street Garage\n---------------------------------\nCurrent Rate: ${self.cost_per_hour} per hour\n---------------------------------")
        if self.parkingSpaces <= 0:
            print(
                "Sorry, there are no spaces available at the moment... Please come back later. ")
            return
        else:
            print(
                f"There are {self.parkingSpaces} parking spaces available at the moment. Please take your ticket.")
            self.tickets -= 1
            self.parkingSpaces -= 1
            sleep(2)
            print(
                f"\n...There are now {self.parkingSpaces} parking spaces available. ")

# Here, we are creating a function that allows a user to see the current rate to park in the garage, as well as if there are any available spots. If there is, it will print out a ticket for the user and record how many spots are now available.

    def payForParking(self):
        '''
        payForParking allows user to input amount of hours they stayed in garage
        displays the total cost based on amount of hours
        first 2 hours are free
        '''
        parking_time = int(input(
            "\nThis is an honor system. How many HOURS were you parked in the garage? "))
        if parking_time > 2:
            parking_time -= 2
            print(
                f"\nThe first 2 hours were free! Your total today is ${self.cost_per_hour*parking_time}.")
            sleep(1)
            print("\n...All checked out! Have a great rest of your day!")
            sleep(2)
            print(
                f"\n...There are now {self.parkingSpaces} parking spaces available in the East Street Garage. ")
            return
        elif parking_time <= 2:
            print(f"\nThe first 2 hours are free. You're good to go!\nHave a nice day! ")
            return
        else:
            print("This is not a valid time.")
# Here we are creating a function that has the user input how many hours they were parked in the garage. With this information, the code is able to determine if there is indeed a charge owed to the user because the first 2 hours are free.
# Once the program determines this, it will output the total charge for the user before they are able to leave the parking garage. It is assuming the person is paying after they inputs their hours.

    def garageInfomercial(self):
        '''
        this method interacts with the garage user and suggests local atttractions
        '''
        yes_or_no = input(
            "Hey friend, while you're here in Orlando I'd like to suggest a few local attractions... are you interested? (Y/N) ")
        if yes_or_no.lower() == 'y':
            while True:
                topic = input(
                    "Let me know a topic you're interested in... (food/amusement park/nature): ")
                if topic.lower() == 'food':
                    print("Feel free to check out:\n - NYPD Pizza | 2589 S Hiawassee Rd, Orlando, FL 32835-6316\n - The Gnarly Barley | 1407 N Orange Ave, Orlando, FL 32804-6410\n - Sear+Sea | 14900 Chelonia Parkway JW Marriott Orlando Bonnet Creek, Orlando, FL 32821")
                    more = input(
                        "\nWould you like to explore one of the other suggested topics? (Y/N) ")
                    if more.lower() == 'y':
                        continue
                    elif more.lower() == 'n':
                        print("\nGreat, I'll see you when you're ready to leave. ")
                        break
                elif topic.lower() == 'amusement park':
                    print(
                        "Feel free to check out:\n - Universal Studios \n - Disney World\n - SeaWorld")
                    more = input(
                        "\nWould you like to explore one of the other suggested topics? (Y/N) ")
                    if more.lower() == 'y':
                        continue
                    elif more.lower() == 'n':
                        print("Great, I'll see you when you're ready to leave. ")
                        break
                elif topic.lower() == 'nature':
                    print(
                        "Feel free to check out:\n - Lake Eola Park\n - Harry P Leu Gardens\n - Tibet-Butler Nature Preserve ")
                    more = input(
                        "\nWould you like to explore one of the other suggested topics? (Y/N) ")
                    if more.lower() == 'y':
                        continue
                    elif more.lower() == 'n':
                        print("Great, I'll see you when you're ready to leave. ")
                        break
        elif yes_or_no.lower() == 'n':
            print("Sounds good! We'll talk again when you're ready to leave the garage. ")
        else:
            print("Not a valid response.")

# Here we are creating a function that outputs infromation about the city the parking garage is in. If the user is interested in it, the program will output some options for the user to dive into.
# Based on the preference, it will output some local attractions and give the user the option to explore other options before quitting the function

    def leaveGarage(self):
        '''
        leaveGarage simulates the exit
        invokes payForParking
        increments tickets and parkingSpaces by 1 for the 1 user if pay+exit is chosen
        '''
        print("\nOh...so you want to exit the garage now...")
        pay_now = input(
            "Are you sure you would you like to pay right now and exit? (Y/N) ")
        if pay_now.lower() == 'y':
            print("***You have 15 minutes to exit, or risk having your car towed!*** ")
            self.tickets += 1
            self.parkingSpaces += 1
            self.payForParking()
        elif pay_now.lower() == 'n':
            print("Okay, let us know when you are ready to pay and exit.")
            return
        else:
            print("That is not a valid response")

# Here we are creating a function that will run once the use is ready to leave the garage. The programs confirms if the user is ready to leave, once they are, the program will update how many availble spots are left.
# The function then calls upon the pay for parking function we created earlier and runs that function within this function. Once that program is ran, the user has entered and left the parking garage, thus showing this is the end of the program.

    def run(self):
        '''
        Method that simulates garage entrance, pay, infomercial, exit
        '''
        self.takeTicket()
        sleep(2)
        self.garageInfomercial()
        sleep(4)
        self.leaveGarage()

# Here we are creating a function that is going to run the program in its intended order and logic flow. There is a break in between each function from what we imported at the top of the page.


# test
garage = Parking_Garage('East Street Garage', 200, 200, 1)
# Here we are assigning a variable to a class we want to run through this program. This class must have all the necessary attributes in the same order as the class established at the top of the page in order to work properly.
garage.run()

# function goes here

# checks users enter an integer
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a integer")


# main routine goes here
tickets_sold = 0
MAX_TICKETS = 3

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("go home kiddo")
        continue
    else:
        print("Error. looks like a typo, try again")
        continue

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulaitons you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
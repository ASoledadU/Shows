import datetime
import json

now = datetime.datetime.now()

SHOWS_FILE = "./shows.json"
TRANSACTIONS_FILE = "./transactions.txt"
TICKET_FILE = "./ticket.txt"
SALES_TAX = 0.07  # 7% Sales Tax


def main():
    while True:
        with open(SHOWS_FILE) as file:
            shows = json.load(file)

        print("Welcome to The Jefferson venue ticket purchasing tool!")
        print("Here are our performing artists! : ")
        artists = []
        for index in range(len(shows)):
            artists.append(shows[index]["artist"])
            print(shows[index]["artist"])
        ask = input("Which artist would you like to see?: ")

        user_index = 0
        for i in range(len(shows)):
            if shows[i]["artist"] == ask:
                user_index = i

        if ask in artists:
            print("GREAT! Lets get started buying your tickets!")
            name = input("What is your name?: ")

            how_many = int(input("How many tickets will you buy?: "))

            if how_many <= 4 or how_many <= shows[user_index]["tickets"]:
                price_of_tickets = how_many * shows[user_index]["price"]
                tax_amount = round(price_of_tickets * SALES_TAX, 2)
                print("Thank you for your business! Come again!")


                with open(TRANSACTIONS_FILE, "a") as file:
                    file.write(
                        "\n{}, {}, {}, {}, ${}.00, ${}, {}".format(
                            name,
                            ask,
                            shows[user_index]["code"],
                            how_many,
                            price_of_tickets,
                            tax_amount,
                            now,
                        )
                    )


                with open(SHOWS_FILE, "w") as jsonFile:
                    updated_tickets = shows[user_index]["tickets"] - how_many
                    shows[user_index]["tickets"] = [updated_tickets]
                    json.dump(shows, jsonFile)
            else:
                print(
                    f"ERROR!!! I'm sorry you either tried to buy more than 4 tickets and you have choosen to buy {how_many} OR we do not have enough tickets left for your amount."
                )
        else:
            print(
                f"I'm sorry we do not have a show with {artist}. Try a different artist."
            )


if __name__ == "__main__":
    main()

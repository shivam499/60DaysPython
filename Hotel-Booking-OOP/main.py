import pandas as pd

df = pd.read_csv("hotels.csv")
cc = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
cc_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:

    def __init__(self, id_hotel):
        self.id_hotel = id_hotel
        self.name = df.loc[df["id"] == self.id_hotel, "name"].squeeze()

    def book(self):
        """Book a Hotel and change the availability"""
        df.loc[df["id"] == self.id_hotel, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def isavailable(self):
        if df.loc[df["id"] == self.id_hotel, "available"].squeeze() == "yes":
            return True
        else:
            return False


class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content


class CreditCard:

    def __init__(self, cc_number):
        self.cc_number = cc_number

    def validate(self, expires, cvc, holder):
        card_data = {"number": self.cc_number, "expiration": expires, "cvc": cvc, "holder": holder}

        if card_data in cc:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):

    def authenticate(self, given_password):
        password = cc_security.loc[cc_security["number"] == self.cc_number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_id = int(input("Enter the Hotel Id: "))
hotel = Hotel(hotel_id)

if hotel.isavailable():
    creditCard = SecureCreditCard(cc_number="1234567890123456")
    if creditCard.validate(expires="12/26", holder="JOHN SMITH", cvc="123"):
        if creditCard.authenticate(given_password="mypass11"):
            hotel.book()
            name = input("Enter Customer Name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment.")
else:
    print("Hotel is not available.")

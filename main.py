import pandas
from hotel_object import Hotel
from reservation_ticket_object import ReservationTicket
from credit_card_object import CreditCard


hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id=hotel_ID)

if not hotel.match_id():
    print("No matching hotel")
    exit()

if not hotel.available():
    print("Hotel is unavailable now.")
    exit()

credit_card = CreditCard(number="1234567890123456")
if not credit_card.validate( expiration="12/26", holder="JOHN SMITH", cvc="123"):
    print("There was a problem with your payment.")
    exit()

hotel.book()
name = input("Enter your name: ")
reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
print(reservation_ticket.generate())



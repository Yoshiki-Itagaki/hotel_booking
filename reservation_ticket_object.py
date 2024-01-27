class ReservationTicket:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
Thank you for your revervation!
Here are your booking data:
Name: {self.customer_name}
Hotel Name: {self.hotel.name}
"""
        return content


class SpaTicket(ReservationTicket):

    def generate(self):
        content = f"""
    Thank you for your SPA reservation!
    Here are your SPA booking data:
    Name: {self.customer_name}
    Hotel Name: {self.hotel.name}
    """
        return content

class Payment:
    def __init__(self, repository):
        self.repository = repository
        self.acceptedPaymentDetails = False

    def add_new_payment(self, name, parkingstarted, parkingStopped, price_to_pay):
        pay_dict = {
            "name": name,
            "parkingStarted": parkingstarted,
            "parkingStopped": parkingStopped,
            "price": price_to_pay
        }
        self.repository.add_payment(pay_dict)

    def pay_all_payments(self):
        if self.acceptedPaymentDetails:
            self.repository.remove_all_payments()
            return True
        else:
            return False

    def change_accepted_payment_details(self, buttonValueBool):
        self.acceptedPaymentDetails = buttonValueBool

    def check_accepted_payment_details(self):
        return self.acceptedPaymentDetails



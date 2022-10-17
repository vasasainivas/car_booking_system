from abc import ABC, abstractmethod


class UpiValidater(ABC):
    @abstractmethod
    def pay_with_upi(self, upi_id):
        pass


class CardValidator(ABC):
    @abstractmethod
    def pay_with_card(self, card, cvv):
        pass


class PaymentWithUpi(UpiValidater):
    def pay_with_upi(self, upi_id):
        if "@" in upi_id:
            print("PAYMENT SUCCESSFUL")
            print()
            print("CLICK 1 TO GENERATE ACKNOWLEDGEMENT")
        else:
            print("PAYMENT FAILED")


class PaymentWithCard(CardValidator):
    def pay_with_card(self, card, cvv):
        if len(card) == 14 and len(cvv) == 3:
            print("PAYMENT SUCCESSFUL")
            print()
            print("CLICK 1 TO GENERATE ACKNOWLEDGEMENT")
        else:
            print("PAYMENT FAILED")


class PaymentWithCash:
    @staticmethod
    def pay_with_cash():
        print("PAY AT SHOWROOM AT THE TIME OF DELIVERY")
        print()
        print("CLICK 1 TO GENERATE ACKNOWLEDGEMENT")

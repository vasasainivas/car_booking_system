#  This is a small terminal design code for greeting user

class Greeting:
    @staticmethod
    def print_home():
        print()
        print("-"*50)
        print("|"+" "*12+"ONLINE CAR BOOKING SYSTEM"+" "*12+"|")
        print("-" * 50)
        print()
        print("Thank you for choosing car booking system \N{slightly smiling face}")
        print()
        print("TYPE NUMBER TO SELECT OPTION")


class ConsolePrints:
    @staticmethod
    def registration_and_login_print():
        print("1 REGISTER")
        print("2 PROCEED AS GUEST")

    @staticmethod
    def before_login_print():
        print()
        print("PRESS 1 TO CONTINUE TO LOGIN")

    @staticmethod
    def in_catalogue():
        print("1 TOYOTA")
        print("2 TATA")
        print("3 MARUTHI")
        print("4 HONDA")

    @staticmethod
    def print_car_model(car_model):
        print("-" * 80)
        for i in range(len(car_model)):
            if len(str(car_model[i])) % 2 != 0:          # To make all strings to even length
                car_model[i] += " "
        car_title = car_model[0] + " " + car_model[1]
        print("|" + " " * ((80 - len(car_title))//2) + car_title + " " * ((80 - len(car_title))//2) + "|")
        print("|" + "-" * 79 + "|")
        print("|" + " " * 16 + "PRICE " + " " * 16 + "|" + " " * 16 + "MILEAGE " + " " * 16 + "|")
        print("|" + " " * ((38 - len(car_model[2])) // 2) + car_model[2] + " " * ((38 - len(car_model[2])) // 2) + "|"
              + " " * ((40 - len(car_model[3])) // 2) + car_model[3] + " " * ((40 - len(car_model[3])) // 2) + "|")
        print("|" + "-" * 79 + "|")
        print("|" + " " * 16 + "ENGINE" + " " * 16 + "|" + " " * 16 + "FUEL TYPE" + " " * 15 + "|")
        print("|" + " " * ((38 - len(car_model[4])) // 2) + car_model[4] + " " * ((38 - len(car_model[4])) // 2) + "|"
              + " " * ((40 - len(car_model[5])) // 2) + car_model[5] + " " * ((40 - len(car_model[5])) // 2) + "|")
        print("|" + "-" * 79 + "|")
        print("|" + " " * 11 + "SEATING CAPACITY" + " " * 11 + "|" + " " * 16 + "AIR BAG" + " " * 17 + "|")
        print("|" + " " * ((38 - len(car_model[6])) // 2) + car_model[6] + " " * ((38 - len(car_model[6])) // 2) + "|"
              + " " * ((40 - len(car_model[7])) // 2) + car_model[7] + " " * ((40 - len(car_model[7])) // 2) + "|")
        print("-" * 80)
        print()
        print("CLICK 1 TO BOOK CAR")

    @staticmethod
    def print_before_payment():
        print("1 PAY WITH CASH")
        print("2 PAY WITH CARD")
        print("3 PAY WITH UPI")

    @staticmethod
    def print_acknowledgement(user_name, selected_model, price, payment_mode):
        payment_dict = {1: "CASH", 2: "CARD", 3: "UPI"}
        print("-" * 80)
        print("|" + " " * 27 + "ACKNOWLEDGEMENT RECEIPT" + " " * 28 + "|")
        print("-" * 80)
        if len(user_name) % 2 != 0:
            user_name += " "
        if len(selected_model) % 2 != 0:
            selected_model += " "
        print("|" + " " * 78 + "|")
        print("| CUSTOMER NAME : " + user_name.upper() + " " * (60 - len(user_name)) + " |")
        print("| SELECTED CAR : " + selected_model.upper() + " " * (61 - len(selected_model)) + " |")
        print("| PRICE : " + price + " " * (68 - len(price)) + " |")
        print("| PAYMENT MODE : " + payment_dict[payment_mode] + " " * (61 - len(payment_dict[payment_mode])) + " |")
        print("| PAYMENT STATUS : SUCCESSFUL" + " "*50 + "|")
        print("|" + " " * 78 + "|")
        print("|" + " " * 78 + "|")
        print("| THANK YOU FOR USING CAR BOOKING PORTAL" + " " * 39 + "|")
        print("| VISIT AGAIN \N{slightly smiling face}" + " " * 63 + "|")
        print("|" + " " * 78 + "|")
        print("-" * 80)

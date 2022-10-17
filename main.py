from user.greet_user import Greeting, ConsolePrints
from user.register import Register
from cars.car_catalogue import CarModels, PrintCars
from user.login import Login, LoginValidate
from payments.payment import PaymentWithCash, PaymentWithCard, PaymentWithUpi

if __name__ == '__main__':
    Greeting.print_home()  # Print greetings
    ConsolePrints.registration_and_login_print()  # print for registration and login
    user_selection_for_registration = int(input())
    user_logs_directory = {}
    if user_selection_for_registration == 1:
        user_logs_directory["user_confirmation_for_registration"] = "YES"
        print("TYPE USER NAME")
        username = input()
        print("TYPE PASSWORD")
        password = input()
        user_logs_directory["user_name_given_at_registration"] = username
        user_logs_directory["user_name_given_at_password"] = password
        register_object = Register(username, password)   # registering username and password
        print(register_object.print_status())
        ConsolePrints.before_login_print()        # print before login
        user_selection_for_login = int(input())
        if user_selection_for_login == 1:
            user_logs_directory["user_confirmation_for_login"] = "YES"
            print("TYPE YOUR USER NAME:")
            login_user_name = input()
            print("TYPE YOUR PASSWORD:")
            login_password = input()
            user_logs_directory["user_name_given_at_login"] = login_user_name
            user_logs_directory["password_given_at_login"] = login_password
            login_object = Login(login_user_name, login_password)
            if LoginValidate.validate_account(register_object, login_object):
                print("LOGIN SUCCESSFUL")
                print("CLICK 1 TO CONTINUE TO CAR CATALOGUE")
                user_selection_for_car_catalogue = int(input())
                if user_selection_for_car_catalogue == 1:
                    user_logs_directory["user_confirmation_to_view_catalogue"] = "YES"
                    ConsolePrints.in_catalogue()  # Print Statements
                    car_selection_in_catalogue = int(input())
                    user_logs_directory["car_selection_in_catalogue"] = str(car_selection_in_catalogue)
                    car_details = PrintCars()              # Creating car details object
                    car_details.print_car_models(car_selection_in_catalogue, CarModels())
                    print("SELECT CAR FOR MORE INFO:")
                    model_selection_in_catalogue = int(input())
                    user_logs_directory["model_selection_in_catalogue"] = str(model_selection_in_catalogue)
                    selected_car_model_details = car_details.show_car(car_selection_in_catalogue,
                                                                      model_selection_in_catalogue,
                                                                      CarModels())
                    ConsolePrints.print_car_model(selected_car_model_details)
                    user_selection_for_car_booking = int(input())
                    if user_selection_for_car_booking == 1:
                        user_logs_directory["user_selection_for_car_booking"] = "1"
                        ConsolePrints.in_catalogue()
                        user_selection_for_car_manufacturer_at_booking = int(input())
                        user_logs_directory["user_selection_for_car_booking"] =\
                            str(user_selection_for_car_manufacturer_at_booking)
                        car_details.print_car_models(user_selection_for_car_manufacturer_at_booking,
                                                     CarModels())
                        user_selection_for_car_model_at_booking = int(input())
                        user_logs_directory["user_selection_for_car_model_at_booking"] =\
                            str(user_selection_for_car_model_at_booking)
                        selected_model_object = car_details.show_car(user_selection_for_car_manufacturer_at_booking,
                                                                     user_selection_for_car_model_at_booking,
                                                                     CarModels())
                        selected_model = selected_model_object[0].upper() + " " + selected_model_object[1].upper()
                        print("You have selected " + selected_model)
                        print()
                        print("CLICK 1 TO CONFIRM AND GO TO PAYMENT")
                        user_selection_for_payment = int(input())
                        user_logs_directory["user_selection_for_payment"] = "YES"
                        if user_selection_for_payment == 1:
                            ConsolePrints.print_before_payment()
                            user_selection_in_payment = int(input())
                            user_logs_directory["user_selection_in_payment"] = user_selection_in_payment
                            if user_selection_in_payment == 1:
                                PaymentWithCash.pay_with_cash()
                                user_selection_for_acknowledgement = int(input())
                                if user_selection_for_acknowledgement == 1:
                                    ConsolePrints.print_acknowledgement(login_user_name, selected_model,
                                                                        selected_model_object[2], 1)
                                    print("TYPE ADMIN PASSWORD TO VIEW USER_LOGS_DIRECTORY:")
                                    admin_password = int(input())
                                    if admin_password == 123:
                                        for i in user_logs_directory:
                                            print(i + " : " + str(user_logs_directory[i]))
                            if user_selection_in_payment == 2:
                                print("TYPE YOUR CARD NUMBER")
                                card_number = input()
                                print("TYPE CVV")
                                cvv = input()
                                user_logs_directory["card_number"] = str(card_number)
                                user_logs_directory["cvv"] = str(cvv)
                                PaymentWithCard().pay_with_card(card_number, cvv)
                                user_selection_for_acknowledgement = int(input())
                                if user_selection_for_acknowledgement == 1:
                                    ConsolePrints.print_acknowledgement(login_user_name, selected_model,
                                                                        selected_model_object[2], 2)
                                    print("TYPE ADMIN PASSWORD TO VIEW USER_LOGS_DIRECTORY:")
                                    admin_password = int(input())
                                    if admin_password == 123:
                                        for i in user_logs_directory:
                                            print(i + " : " + str(user_logs_directory[i]))
                            if user_selection_in_payment == 3:
                                print("TYPE YOUR UPI ID")
                                upi_id = input()
                                PaymentWithUpi().pay_with_upi(upi_id)
                                user_selection_for_acknowledgement = int(input())
                                if user_selection_for_acknowledgement == 1:
                                    ConsolePrints.print_acknowledgement(login_user_name, selected_model,
                                                                        selected_model_object[2], 3)
                                    print("TYPE ADMIN PASSWORD TO VIEW USER_LOGS_DIRECTORY:")
                                    admin_password = int(input())
                                    if admin_password == 123:
                                        for i in user_logs_directory:
                                            print(i + " : " + str(user_logs_directory[i]))
                        else:
                            print("INVALID INPUT")

                    else:
                        print("INVALID INPUT")
                else:
                    print("INVALID INPUT")
            else:
                print("INVALID CREDENTIALS")
        else:
            print("INVALID INPUT")

    elif user_selection_for_registration == 2:
        ConsolePrints.in_catalogue()  # Print Statements
        car_selection_in_catalogue = int(input())
        car_details = PrintCars()  # Creating car details object
        car_details.print_car_models(car_selection_in_catalogue, CarModels().car_models())
        model_selection_in_catalogue = int(input())
        selected_car_model_details = car_details.show_car(car_selection_in_catalogue, model_selection_in_catalogue,
                                                          CarModels())
        ConsolePrints.print_car_model(selected_car_model_details)
        print("FOR BOOKING CAR YOU SHOULD BE REGISTERED WITH US")

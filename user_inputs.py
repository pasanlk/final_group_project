
user_input = input("please enter required method(email or show_now); ")
if user_input == "show":
    print_df()
elif user_input == "email":
    send_mail()

def show_submessage():
    print("This is the second function.")


def show_message():
    print("This is the first function.")
    show_submessage()


# Call to the first function
show_message()

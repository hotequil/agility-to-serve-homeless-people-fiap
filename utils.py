def calculate_time_to_serve(rm):
    minutes = 0
    rm = str(rm)
    number = int(f"{rm[3]}{rm[4]}")

    minutes += number % 3
    minutes += 1

    return minutes

def print_space():
    print("")

def print_bar():
    print_space()
    print("=========================================================================================================================================")
    print_space()

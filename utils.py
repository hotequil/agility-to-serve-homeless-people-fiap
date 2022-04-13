REMOVE_ONE_HOMELESS = 1
REMOVE_TWO_HOMELESS = 2
REMOVE_THREE_OR_MORE_HOMELESS = 3

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

def print_title(title):
    print(f"# {title}:")

def print_item(message, value):
    print(f"* {message}: {value};")

def print_message(message):
    print(f"- {message}.")

def print_data(index, minutes_running, queue):
    print_item("Voltas no looping", index)
    print_item("Minutos rodando", minutes_running)
    print_item("Número total de moradores de rua que ainda não foram servidos", queue.length())
    print_item("Quantidade de filas (estações) totais", queue.queues_quantity())

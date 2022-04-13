from utils import calculate_time_to_serve, print_bar, print_message, print_title, print_item, print_data
from homeless_queue import HomelessQueue

rm = 87808
minutes_to_serve = calculate_time_to_serve(rm)
minutes_to_enter_someone = 2
maximum_limit_people = 15
minutes_running = 0
index = 0

print_message("Bem-vindo ao algoritmo que irá ajudar você no processo de assistência a moradores de rua! Para iniciar, responda à pergunta abaixo, por favor")
print_bar()

people_initial_number = int(input("1) Quantos moradores de rua estão aguardando a preparação das filas (coloque um número inteiro e maior do que zero)? R: "))

print_bar()

queue = HomelessQueue(people_initial_number, maximum_limit_people)

print_title("Dados iniciais")
print_data(index, minutes_running, queue)
print_item("Minutos para servir até três moradores de rua simultaneamente", minutes_to_serve)
print_item("Quantidade de moradores de rua no início", people_initial_number)
print_item("Quantidade máxima de moradores de rua em cada fila (estação)", maximum_limit_people)
print_item("Minutos para entrar um novo morador de rua em uma fila (estação)", minutes_to_enter_someone)
print_bar()

while queue.has_length():
    if index != 0 and index % 10 == 0:
        minutes_running += 1

        queue.add(minutes_running, minutes_to_enter_someone)
        queue.delete(minutes_running, minutes_to_serve)

        print_title("Dados nessa volta")
        print_data(index, minutes_running, queue)
        print_bar()

    index += 1

print_message("Parabéns, nós conseguimos atender todos os moradores de rua")

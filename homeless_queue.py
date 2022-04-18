from uuid import uuid4
from math import ceil
from utils import print_bar, print_title, print_item, REMOVE_ONE_HOMELESS, REMOVE_TWO_HOMELESS, REMOVE_THREE_OR_MORE_HOMELESS

def can_modify_list(minutes_running, minutes_to_do_something):
    return minutes_running >= minutes_to_do_something and minutes_running % minutes_to_do_something == 0

class HomelessQueue:
    def __init__(self, people_initial_number, maximum_limit_people):
        self.people_initial_number = people_initial_number
        self.maximum_limit_people = maximum_limit_people
        self.list = []

        self.set_list()

    def has_length(self):
        return self.length() > 0

    def length(self):
        return len(self.list)

    def queues_quantity(self):
        return ceil(float(self.length() / self.maximum_limit_people))

    def set_list(self):
        index = 0

        while index < self.people_initial_number:
            self.add(None, None, True)

            index += 1

    def remove(self, turn_times):
        index = 0

        while index < turn_times:
            if self.has_length():
                self.list.pop(0)

                print_title("Remoção")
                print_item("Foi servido um morador de rua que estava em uma fila")
                print_bar()

            index += 1

    def delete(self, minutes_running, minutes_to_serve):
        if not can_modify_list(minutes_running, minutes_to_serve):
            return

        rest = self.length() % self.maximum_limit_people
        queues_quantity = self.queues_quantity()

        for queue in range(queues_quantity):
            is_last_queue = queues_quantity == (queue + 1)

            if is_last_queue and rest == REMOVE_ONE_HOMELESS:
                self.remove(REMOVE_ONE_HOMELESS)
            elif is_last_queue and rest == REMOVE_TWO_HOMELESS:
                self.remove(REMOVE_TWO_HOMELESS)
            else:
                self.remove(REMOVE_THREE_OR_MORE_HOMELESS)

    def add(self, minutes_running, minutes_to_enter_someone, skip_validation = False):
        if not skip_validation and not can_modify_list(minutes_running, minutes_to_enter_someone):
            return

        code = uuid4()

        print_title("Adição")
        print_item("Entrou um morador de rua em uma fila com o código", code)
        print_bar()

        self.list.append(code)

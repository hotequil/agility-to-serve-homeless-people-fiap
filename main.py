from utils import calculate_time_to_serve

rm = 87808
minutes_to_serve = calculate_time_to_serve(rm)
minutes_to_enter_someone = 2
minutes_running = 0
index = 0
people = 15
can_continue = True

while people > 0 or can_continue:
    if index % 10 == 0 and index != 0:
        minutes_running += 1

        if minutes_running != 0 and minutes_to_enter_someone % minutes_running == 0 and minutes_to_enter_someone <= minutes_running:
            people += 1
            can_continue = False

        if minutes_running != 0 and minutes_to_serve <= minutes_running and (minutes_to_serve % minutes_running == 0 or minutes_to_serve == 1):
            if people == 1:
                people -= 1
            elif people == 2:
                people -= 2
            elif people >= 3:
                people -= 3

    print(f"index: {index}")
    print(f"minutes_running: {minutes_running}")
    print(f"people: {people}")
    print("=======================")

    index += 1



print("ended")

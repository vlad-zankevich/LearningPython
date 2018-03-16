def run():
    # Dream vacation
    quiz_dict = {}
    # Setting the continuation flag
    quiz_active = True

    while quiz_active:

        name = input("Hello, what's your name? ")
        vacation_place = input("Where do you want to spend the vacation? ")
        quiz_dict[name] = vacation_place

        next_person_flag = True
        while next_person_flag:
            repeat = input("Wold you like to let another person respond? (yes/no) ")
            if repeat == 'yes':
                next_person_flag = False
            elif repeat == 'no':
                quiz_active = False
                next_person_flag = False
            else:
                print("Please, write 'yes' or 'no'.")

    # The quiz is done, output results
    print("\n--- Quiz result ---")
    for person, place in quiz_dict.items():
        print(person.title() + " wants to spend the vacation on " +
              place.title() + ".")


if __name__ == "__main__":
    run()


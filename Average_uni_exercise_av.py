my_list = []

grade = 0
ects = 0
sum_grade = 0
sum_ects = 0
counter = 0
prod_sum = 0
is_true = True
i = 1

print("Enter the Thematic Units that you want to calculate average: ")

while is_true:

    while True:
        lesson = input(f"Insert {i} Thematic Unit (Enter to exit): ").strip()

        if lesson == "":
            print("Program terminated by user.")
            exit()

        if lesson.isdigit():
            print("Numbers are not allowed. Insert Thematic Unit.")
            continue

        my_list.append(lesson)
        print("Valid lesson:", lesson)
        i+=1
        break

    while True:
        try:
            grade = float(input("Insert grade (5-10): "))
            if grade == 0:
                break
            elif grade < 5 or grade > 10:
                print("Invalid grade. Only 5–10 allowed.")
            else:
                my_list.append(grade)
                print("Grade accepted, you entered :", grade)
                break
        except ValueError:
            print("Give numbers please,not text.")

    while True:
        try:
            ects = int(input("Insert ECTS of lesson (5-20): "))
            if ects == 0:
                break
            elif ects < 5 or ects > 20:
                print("Invalid ects. Only 5–20 allowed.")
            else:
                my_list.append(ects)
                print("Valid ECTS :", ects)
                print("Summary: ", my_list)
                print("Your weighted average is: ",(grade * ects) / ects)
                break
        except ValueError:
            print("Enter numbers,not text.")

    sum_grade += grade
    counter += 1
    sum_ects += ects
    prod_ects = grade * ects
    prod_sum = prod_ects + prod_sum

    if counter > 0:
        average = sum_grade / counter
        ects_average = prod_sum / sum_ects
        print("Your average is:", round(average,2))
    else:
        print("No grades were inserted.")

    while True:
        choice = input("Do you want to continue with other Thematic Units? Yes = 1 , No = 0: ")
        my_list.append("Next Thematic Unit: ")
        if choice == "1":
            break


        elif choice == "0":
            is_true = False

            ects_average = prod_sum / sum_ects
            print("Your Total Weighted average:", round(ects_average, 2))

            if ects_average < 5:
                print("You did not pass the course.")
            else:
                print("You passed the course.")

                if ects_average < 6.5:
                    print("Grade classification: Good")
                elif ects_average < 8.5:
                    print("Grade classification: Very Good")
                else:
                    print("Grade classification: Excellent")

            break





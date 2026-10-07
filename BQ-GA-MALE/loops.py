
# for loop

# for i in range(100):
#     print("Abdus Subhan")

# for i in range(1,6):
#     print(i)

# course = "PYTHON"

# for i in course:
#     print(i)




# while loop

# 1- counter
# 2- while (condition)
# 3- increment/ demcrement

# counter = 0

# while (counter < 3):
#     print("Abdus Subhan")
#     counter +=1



# counter = 1

# while (counter < 11):
#     print(counter)
#     counter +=1


# counter = 10

# while (counter > 0):
#     print(counter)
#     counter -=1




for i in range(3):
    secret_number = 4

    guess_number = int(input("Guess Number: "))

    if secret_number == guess_number:
        print("You won!")
        break

    else:
        print("You lost!")
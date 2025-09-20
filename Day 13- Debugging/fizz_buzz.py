# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
                          #or
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        #if
        elif number % 3 == 0:
            print("Fizz")
        #if
        elif number % 5 == 0:
            print("Buzz")
        else:
          #[number]
            print(number)

fizz_buzz(15)

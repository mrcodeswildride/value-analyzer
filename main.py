print()

favorable_outcomes = int(input("How many favorable outcomes of first event? "))
possible_outcomes = int(input("How many possible outcomes of first event? "))

first_decimal = favorable_outcomes / possible_outcomes
percent = first_decimal * 100
print(f"The probability is {percent:.2f}%.\n")

favorable_outcomes = int(input("How many favorable outcomes of second event? "))
possible_outcomes = int(input("How many possible outcomes of second event? "))

second_decimal = favorable_outcomes / possible_outcomes
percent = second_decimal * 100
print(f"The probability is {percent:.2f}%.\n")

first_payoff = float(input("Enter payoff of first event: "))
second_payoff = float(input("Enter payoff of second event: "))

first_value = first_decimal * first_payoff
second_value = second_decimal * second_payoff
expected_value = first_value + second_value

print(f"\nThe expected value is {expected_value}.")

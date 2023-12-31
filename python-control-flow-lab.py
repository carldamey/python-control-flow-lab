# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

def check_vowel(letter):
  result = "vowel" if letter.lower() in "aeiou" else "consonant"
  print(f"{letter.upper()} is a {result}.")

check_vowel(input("Please Enter a Letter: ")[0])

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

def phrase_length():
  phrase = ""
  while phrase.lower() != "quit":
    phrase = input("Please enter a phrase or type 'quit' to exit: ")
    if phrase.lower() != "quit": print(f"What you entered is {len(phrase)} characters long.")

phrase_length()

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

def dog_years():
  dog_age = 0
  age = int(input("Enter a dog's age: "))
  for num in range(age):
    if num < 2: dog_age += 10
    else: dog_age += 7
  print(f"The dog's age in dog years is {dog_age}.")

dog_years()

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

def triangle_type():
  a = int(input("Enter length of side a: "))
  b = int(input("Enter length of side b: "))
  c = int(input("Enter length of side c: "))
  if a == b and a == c: result = "equilateral"
  elif a != b and a !=c and b !=c: result = "scalene"
  elif a == b or a == c or b == c: result = "isoceles"
  print(f"A triangle with side lengths of {a}, {b}, & {c} is a(n) {result} triangle.")

triangle_type()

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

def fibonacci_first_50():
  terms = [0, 1]
  while len(terms) < 50:
    new_term = terms[-1] + terms[-2]
    terms.append(new_term)
  print("\n".join(str(term) for term in terms))

fibonacci_first_50()

# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

def check_season():
  months = ["dec", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov"]
  month = input("Please enter the first 3 letters of the month: ")
  day = int(input("Please enter the day: "))

  if month.lower() == "mar" and day > 19: season = "Spring"
  elif month.lower() == "jun" and day > 20: season = "Summer"
  elif month.lower() == "sep" and day > 21: season = "Fall"
  elif month.lower() == "dec" and day > 20: season = "Winter"
  elif months.index(month) <= 3: season = "Winter"
  elif months.index(month) <= 6: season = "Spring"
  elif months.index(month) <= 9: season = "Summer"
  elif months.index(month) <= 11: season = "Fall"

  print(f"{month.title()} {day} is in {season}")


check_season()
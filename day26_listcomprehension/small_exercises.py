#list comprehension
#exercise 1: new_list = [new_item for item in list]
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

range = range(1,5)
range_list = [2*n for n in range]
print(range_list)

#with condition
#new_list = [new_item for item in list if test]

#exercise 2: squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number * number for number in numbers]
print(squared_numbers)

#exercise 3: equal numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)

#exercise 4 importing two lists and creating a new list with common values
file_one = open("file1.txt", "r")
file_two = open("file2.txt", "r")

data_one = file_one.read()
data_two = file_two.read()

list_one = data_one.split("\n")
list_one = [int(number) for number in list_one]

list_two = data_two.split("\n")
list_two = [int(number) for number in list_two]

print(list_one)
print(list_two)

result = [number for number in list_one if number in list_two]
print(result)


#for dictionaries 
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items()}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

#exercise 5: creating a new dictionary with length of each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
word_dict = {word:len(word) for word in words}
print(word_dict)

#exercise 6: from celcius to fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items() }
print(weather_f)
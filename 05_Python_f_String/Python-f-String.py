
# coding: utf-8

# Python-f-String Tutorial and why you should start using it
name = 'Frank'
age = 24
profession = 'Python Dev'
language = 'Python'

person = dict(name='Frank', age=24,
                profession='Python Dev', language='Python')

# 1. %s
print("My name is %s and I'm a %s. I'm currently being %s and my favourite language is %s" \
% (name, profession, age, language))


# 2. str.format()

# a.) Interpolation with empty curly braces

print("My name is {} and I'm a {} and I'm {} \
years old and My favourite lan is {}".format(name, profession, age, language))

# b.) Interpolation with tuple indexing
print("My name is {3} and I'm a {0} and I'm {1} \
years old and My favourite lan is {2}".format(profession, age, language, name))


# c.) Interpolation with dictionay key-value mapping
print("My name is {name} and I'm a {profession} and I'm {age} \
years old and My favourite lan is {language}".format(**person))






# 3. Python f-String - insert variables directly in a string object.
print(f"My name is {name} and I'm a {profession} and I'm {age} and I love {language}")



# Convert the parameter to a String
def stringfy(value):

    return str(value)


## Run a function in a f-string placeholder

print(f"Hello, my age is stringfied here as {stringfy(value=24)}")



## Other operations: dictionary key indexing in f-string placeholders.
print(f"My name is {person['name']} and I'm a {person['profession']}")

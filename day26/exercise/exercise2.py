sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = [ word for word in sentence.split()]
result = {word: len(word) for word in words}


print(result)
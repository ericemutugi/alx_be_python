# Check for current weather from user
current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Conditional check for appropriate response from input
if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I dont have recommendations for this weather.")

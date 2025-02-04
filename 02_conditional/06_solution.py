distance = input("Enter the distance: ")
distance = int(distance)

if distance <= 3:
    transportation = "walk"
elif distance <= 14:
    transportation = "bike"
elif distance >=15 :
    transportation = "car"

print(f"Distance: {distance} km, Transportation: {transportation}")
    
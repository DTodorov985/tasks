measurement = 0
count_larger_measurement = 0
Flag = True

while Flag:
    try:
        measurement_input = int(input())
    except ValueError:
        Flag = False
        continue

    if measurement == 0:
        measurement = measurement_input
        continue

    if measurement < measurement_input:
        count_larger_measurement += 1

    measurement = measurement_input

print(count_larger_measurement)

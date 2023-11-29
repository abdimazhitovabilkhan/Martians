cargo_weight = 713
boxes_found = 0
total_weight = 0

def check_box(kilometer, distance_list, weight_list):
    global boxes_found, total_weight
    if kilometer in distance_list:
        box_index = distance_list.index(kilometer)
        print(f"Found box at kilometer {kilometer} with weight {weight_list[box_index]} kg.")
        boxes_found += 1
        total_weight += weight_list[box_index]
        del distance_list[box_index]
        del weight_list[box_index]
    else:
        print(f"No box found at kilometer {kilometer}.")

# Main loop
while True:
    distance_list = []
    weight_list = []

    # input for kilometer marks
    for i in range(3):
        kilometer = int(input(f"Enter kilometer for box {i + 1}: "))
        distance_list.append(kilometer)

    # input for weights
    for i in range(3):
        weight = int(input(f"Enter weight for box {i + 1}: "))
        weight_list.append(weight)

    # Check for boxes
    for kilometer in distance_list:
        check_box(kilometer, distance_list, weight_list)

    # Check if all boxes are found
    if boxes_found == 3 and total_weight == cargo_weight:
        print("Cargo found successfully! All boxes are retrieved.")
        break

    # Reset variables for next try
    boxes_found = 0
    total_weight = 0
    print("Cargo not fully retrieved. Please try again with updated kilometer marks.")

print("End of program.")

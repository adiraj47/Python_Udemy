available_list =["computer", "monitor", "mouse", "Keyboard", "CPU", "Hdmi", "GPU", "joystick"]
current_choice = '-'
computer = []
valid_choice = []
for i in (1, len(available_list) + 1):
    valid_choice.append(str(i))
while current_choice != '0':
    if current_choice in valid_choice:
        index = int(current_choice) - 1
        current_choice = available_list[index]
        if current_choice in computer:
            print("Removing {}".format(current_choice))
            computer.remove(current_choice)
        else:
            print("Adding {}".format(current_choice))
            computer.append(current_choice)

    else:
        # print("1) Computer")
        # print("2) Monitor")
        # print("3) mouse")
        # print("4) keyboard")
        # print("5) cpu")
        # print("6)hdmi")
        # print("0) exit")
        for number,parts in enumerate(available_list):
            print("{0}: {1}".format(number + 1, parts))
    current_choice = input()
print(computer)

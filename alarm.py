getalinput = int(input("Vul een positief getal in:"))

if getalinput >= 0:
    for i in range(1, getalinput + 1):
        print(f"Alarm {i}!")
else:
    print("Getal moet positief zijn!")
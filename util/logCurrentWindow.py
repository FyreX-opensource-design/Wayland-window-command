import GetWindow, time

while True:
    with open("log.txt", "w") as file:
        file.write(GetWindow.getActiveWindowLinuxWayland())
        time.sleep(20)

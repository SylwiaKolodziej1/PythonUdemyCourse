names = {"arkadiusz", "Wioletta", "karol", "Bartłomiej", "Jakub"}

names = {
    name
    for name in names
    if name.startswith("B") == False
    }

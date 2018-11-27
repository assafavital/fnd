def log(message):
    FILE = "fnd\log.txt"
    prevContent = open(FILE, "r").read()
    with open(FILE, "w") as f:
        f.write("{}\n{}".format(prevContent, message))
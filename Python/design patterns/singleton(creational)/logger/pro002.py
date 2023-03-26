
def log_message(msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("{}\n".format(msg))


# log_message("inja ie error darim !")

# DRY -> Don't repeat yourself
# dont copy paste your code on your code .
# repackage
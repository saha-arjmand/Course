
# a :append
# w :write
# r :read

path = "singleton(creational)/logger/log/filename.txt"
with open(path, "a") as log_file:
    log_file.write("Log message.\n")
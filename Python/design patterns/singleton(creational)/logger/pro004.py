def critical(msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("[CRITICAL] {}\n".format(msg))

def error(msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("[ERROR] {}\n".format(msg))

def warning(msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("[WARNING] {}\n".format(msg))

def info(msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("[INFO] {}\n".format(msg))

def debug(msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("[DEBUG] {}\n".format(msg))
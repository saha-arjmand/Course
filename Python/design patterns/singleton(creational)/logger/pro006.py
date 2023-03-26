
def write_log(level, msg):
    path = "singleton(creational)/logger/log/filename.txt"
    with open(path, "a") as log_file:
        log_file.write("[{}] {}\n".format(level, msg))


def critical(msg):
    write_log("CRITICAL", msg)

def error(msg):
    write_log("ERROR", msg)

def warning(msg):
    write_log("WARNING", msg)

def info(msg):
    write_log("INFO", msg)

def DEBUG(msg):
    write_log("DEBUG", msg)
from pro011 import Logger

log_obj1 = Logger()
log_obj1.file_name = 'log.txt'
log_obj1.critical("this is with singleton critical obj")
print("print obj1: ",log_obj1)

print("-------------------------")

log_obj2 = Logger()
log_obj2.file_name = 'log.txt'
log_obj2.error("this error create with singleton critical obj")
print("print obj2: ",log_obj2)
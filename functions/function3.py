def can_drive(age, drv_age=16):
        return age >= drv_age

print(can_drive(15, drv_age=15)) ## Allows to modify value of driving age when calling the function; also set a default value ##
print(can_drive(15,15))
print(can_drive(15))
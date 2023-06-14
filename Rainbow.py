import time
# import ray
i = 1
n = 1
# ray.init()
# rainbow_colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']

def rainbow2_text(text):
    global n
    rainbow_colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    rainbow = ''
    for char in text:
        rainbow += (char + rainbow_colors[n]) *2
        if n < (len(rainbow_colors) - 1):
            n += 1
        else:
            n = 1
    return rainbow

# @ray.remote
def rainbow_text(text):
    global i
    rainbow_colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    # rainbow_colors = ['\033[35m', '\033[34m', '\033[36m', '\033[32m', '\033[33m', '\033[31m']
    rainbow = ''
    for char in text:
        rainbow += (char + rainbow_colors[i]) *2
        if i < (len(rainbow_colors) - 1):
            i += 1
        else:
            i = 1
    return rainbow
    # return f'{rainbow}\r'


text = "############################################"

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
############################################

# print("\n")
print("\33[2J",end='\n')
if __name__ == "__main__":
    flag = 1
    while True:
        time.sleep(0.01)
        rainbow = rainbow_text(text)
        print(f'\033[F{rainbow}',end='\n')
        time.sleep(0.05)
        print(f'{rainbow}',end='\r')
        print("\n",end='\033[A')

        time.sleep(0.06)
        print(f'\n{rainbow}',end='\033[F')


# import os
# import time
# # Clear the console
# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

# while True:
#     param1 = "Value 1"
#     param2 = "Value 2"
#     print(param1, param2, sep='\n', end='\r')
#     time.sleep(1)
#     # Update the values of param1 and param2
#     # You can replace these lines with your actual code that updates the parameters
    
#     param1 = "Updated Value 1"
#     param2 = "Updated Value 2"
    
#     # Clear the console
#     clear_console()
    
#     # Print the changes only
#     print(param1, param2, sep='\n', end='\r')
#     time.sleep(1)
#     clear_console()


# import time

# i = 0

# def rainbow_text(text):
#     global i
#     rainbow_colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
#     rainbow = ''
#     for char in text:
#         rainbow += (char + rainbow_colors[i]) * 3
#         # rainbow += char + rainbow_colors[i]
#         # if len(text) > 50:
#             # rainbow += char + rainbow_colors[i]
#         # if len(text) > 100:
#             # rainbow += char + rainbow_colors[i]
#         if i < (len(rainbow_colors) - 1):
#             i += 1
#         else:
#             i = 0
#     # print(len(text))
#     # print(len(rainbow))
#     return rainbow


# # lines = int(input('Enter how many lines:'))
# text = '###############################'
# sleep = 0.1
# if len(text) >= 30:
#     sleep = 0.05

# while True:
#     rainbow = rainbow_text(text)
#     # rainbow2 = 
#     print(rainbow, end='\r')
#     # print(rainbow)
#     time.sleep(sleep)

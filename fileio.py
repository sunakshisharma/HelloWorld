jabber = open("sample.txt", "r")

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()
print("*" * 40)

# # no need to write close buy using "with"
# with open("/Users/apple/Desktop/original.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line,end='')

# with open("/Users/apple/Desktop/original.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

with open("/Users/apple/Desktop/original.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

print("#" * 40)

with open("/Users/apple/Desktop/original.txt", "r") as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')
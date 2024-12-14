import sys

if len(sys.argv) < 2:
    fullName = sys.argv[1]
    split_fullName = fullName.split(' ')
    first_name = split_fullName[0]
    last_name = split_fullName[1:len(split_fullName) - 1]
else:
    first_name = ' '.join(sys.argv[1:len(sys.argv)-1])
    last_name = sys.argv[len(sys.argv)-1]

print(last_name + " " + first_name)
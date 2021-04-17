
PATH_INPUT_FILE = './input'
PATH_OUTPUT_FILE = './output'

def count_strings():
    ''' counting strings in the input file '''

    lines = 0
    all_content = input_file.read()
    CoList = all_content.split("\n")
    for i in CoList:
        lines += 1
    input_file.seek(0, 0)
    return lines

def count_disks():
    ''' counting all disks in input file bi ID string '''
    pDisks = 0
    all_content = input_file.read()
    CoList = all_content.split("\n")
    for i in CoList:
        if "ID                              :" in i:
            pDisks += 1
    input_file.seek(0, 0)
    return pDisks

def find_value(value):
    ''' Find Value and make a list. e.g. ['ID', '0:1:0'] '''
    if value in string:
        # print(f'[{string}]')
        data = string.rstrip().split(" : ")
        data[0] = data[0].strip()
        data[1] = data[1].strip()
        return data

# open input file
with open(PATH_INPUT_FILE, 'r') as input_file:
    lines = count_strings()
    pDisks = count_disks()

    # open output file
    with open(PATH_OUTPUT_FILE, 'w') as output_file:

        str1 = "Type| Bus  | Status | State| Endur | PrFail |  ID   |Capacity |   Serial No.   |"
        str2 = "--------------------------------------------------------------------------------"
        output_file.write(str1)
        output_file.write("\n")
        output_file.write(str2)
        output_file.write("\n")

        # create empty dict
        dictionary = {}

        # reading string by string the input file and check matches
        for i in range(lines):
            string = input_file.readline()

            ID = find_value("ID                              :")
            status = find_value("Status                          :")
            name = find_value("Name                            :")
            state = find_value("State                           :")
            bus_protocol = find_value("Bus Protocol                    :")
            media = find_value("Media                           :")
            endurance = find_value("Remaining Rated Write Endurance :")
            failure = find_value("Failure Predicted               :")
            capacity = find_value("Capacity                        :")
            serial_number = find_value("Serial No.                      :")

            # if the match is True - write values in the dict
            for i in ID, status, name, state, bus_protocol, media, endurance, failure, capacity:
                if i:
                    dictionary.update({i[0]:i[1]})


            # ===================================================
            if capacity:
                capacity[1] = capacity[1].split(" (")
                # capacity[1][0] = '1,787.88 GB'

                capacity_numbers = capacity[1][0].split(" ") # ['1,787.88', 'GB']

                if "," in capacity_numbers[0]:
                    capacity_numbers[0] = capacity_numbers[0].replace(",", "") # '1787.88'

                if "." in capacity_numbers[0]:
                    capacity_numbers[0] = capacity_numbers[0].split(".") # ['1787', '88']
                    capacity_numbers[0] = capacity_numbers[0][0]

                capacity_numbers[0] = round(int(capacity_numbers[0]), -2)
                final_capacity = f'{str(capacity_numbers[0])} {capacity_numbers[1]}'
                print(final_capacity)

                dictionary.update({capacity[0]:final_capacity})
            # ===================================================


            if serial_number:
                dictionary.update({serial_number[0]: serial_number[1]})

                output_file.write(str(dictionary.get("Media")))
                output_file.write(" | ")

                output_file.write(str(dictionary.get("Bus Protocol")))
                output_file.write(" | ")

                output_file.write(str(dictionary.get("State")))
                output_file.write(" |  ")

                output_file.write(str(dictionary.get("Status")))
                output_file.write("  |  ")

                output_file.write(str(dictionary.get("Remaining Rated Write Endurance")))
                output_file.write("  |   ")

                output_file.write(str(dictionary.get("Failure Predicted")))
                output_file.write("   | ")

                # output.write(str(dictionary.get("Name")))
                # output.write(" | ")

                output_file.write(str(dictionary.get("ID")))
                output_file.write(" | ")



                output_file.write(str(dictionary.get("Capacity")))
                output_file.write(" | ")

                output_file.write(str(dictionary.get("Serial No.")))
                output_file.write(" | ")

                output_file.write("\n")
        output_file.close()
            #print(dictionary)
    input_file.close()
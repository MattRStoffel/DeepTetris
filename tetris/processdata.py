import os


def parse_data(input_data):
    # Split the input data into lines
    lines = input_data.strip().splitlines()

    # Process the first line and keep its comma
    parsed_data = lines[0].strip()

    # Process the remaining lines
    for line in lines[1:-2]:
        # Remove all commas from each line and then add a comma at the end
        parsed_data += line.replace(",", "") + ""
    parsed_data += lines[-2].replace(",", "") + ","
    parsed_data += lines[-1].replace(",", "") + ",\n"

    return parsed_data.strip()


with open("data.csv", "w") as csvfile:
    # All the .txt files in the dir tetris
    for filename in os.listdir("tetris"):
        if filename.endswith(".txt"):
            with open("tetris/" + filename, "r") as f:
                data = f.read()
                # Pull the number from the file name EG: addresses_output686.txt will be 686
                number = filename.split("output")[1].split(".")[0]
                csvfile.write(number + ",")
                csvfile.write(parse_data(data) + "\n")
                # delete the file f
                os.remove("tetris/" + filename)

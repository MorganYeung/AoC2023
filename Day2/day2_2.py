import re
def parse_file(file_path):
    parsed_data = 0
    cubes = {
        "red": 0,
        "blue":0,
        "green":0
    }
    game = []
    ans = 0
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                words = line.split()
                for counter, word in enumerate(words):
                    if word == "red" or word == 'red,' or word == 'red;':
                        cubes["red"] = max(cubes["red"],int(words[counter-1]))
                    if word == "blue"or word == 'blue,' or word == 'blue;':
                        cubes["blue"] = max(cubes["blue"],int(words[counter-1]))
                    if word == "green"or word == 'green,' or word == 'green;':
                        cubes["green"] = max(cubes["green"],int(words[counter-1]))
                ans = ans + (cubes["green"] *  cubes["red"]*  cubes["blue"])
                cubes = {"red": 0, "blue":0, "green":0}
            return ans


    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An IO error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return parsed_data

# Example usage
file_path = 'input.txt'
print('Day2pt1')
result = parse_file(file_path)
print(result)
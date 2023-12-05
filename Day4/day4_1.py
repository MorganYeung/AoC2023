import re
def parse_file(file_path):
    ans = 0
    numMatches = []
    winningCard = []
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                line = line.split()
                #print(line[2:])
                winningNum = []
                swap = False
                numMatches.append(0)
                winningCard.append(False)
                for item in line[2:]:
                    if item == '|':
                        swap = True
                        continue
                    if not swap:
                        winningNum.append(item)
                    else:
                        if item in winningNum:
                            numMatches[count] = numMatches[count] + 1

                if numMatches[count] > 0:
                    ans = ans + pow(2,(numMatches[count]-1))
                    

        return ans                     
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An IO error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 69

# Example usage
file_path = 'input.txt'
print('Day3pt1')
result = parse_file(file_path)
print(result)
import re
from math import prod
def search(time,record):
    winRange = [0,0]
    velocity = 0
    timetoRace = 0
    for i in range(1,time):
        velocity = i
        timetoRace = time - i
        if timetoRace * velocity > record:
            if winRange[0] != 0:
                winRange[0] = min(winRange[0],i)
            else:
                winRange[0] = i

        velocity = time - i
        timetoRace = i
        if timetoRace * velocity > record:
            if winRange[1] != 0:
                winRange[1] = max(winRange[1],time - i)
            else:
                winRange[1] = time - i
                break
    
    return winRange

def parse_file(file_path):
    ans = 1
    times = ""
    distances = ""
    winWays = []
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                line = line.strip().split()
                if count == 0:
                    times += ''.join(str(element) for element in line[1:])
                if count == 1:
                    distances += ''.join(str(element) for element in line[1:])
            #print(times)
            #print(distances)
            time = int(times)
            distance = int(distances)
            temp = search(time,distance)
            if temp [0] != 0:
                winWays.append(temp[1]-temp[0]+1)
            else:
                winWays.append(0)

        ans = prod(element for element in winWays)
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
print('Day6pt2')
result = parse_file(file_path)
print(result)
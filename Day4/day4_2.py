import re
def parse_file(file_path):
    ans = 0
    numMatches = []
    winningCard = []
    numCards = []
    ogNumCards = 0
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                line = line.split()
                #print(line[2:])
                winningNum = []
                swap = False
                numMatches.append(0)
                winningCard.append(False)
                numCards.append(1)
                for item in line[2:]:
                    if item == '|':
                        swap = True
                        continue
                    if not swap:
                        winningNum.append(item)
                    else:
                        if item in winningNum:
                            numMatches[count] = numMatches[count] + 1
                            winningCard[count] = True
                ogNumCards = count + 1
            
            z = 0
            while z < ogNumCards:
                for k in range(z,numMatches[z]+z):
                    numCards[k+1] += (numCards[z])
                if z == 1:
                    print(numMatches)
                    print(numCards)
                z+=1
            ans = 0
            for cards in numCards:
                ans += cards
                
            
                
                
                    

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
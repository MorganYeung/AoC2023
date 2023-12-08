import re
from math import prod
def findSpot(handarray, orderArray, handIndex):
    length = len(orderArray)

    if length == 0:
        return [handIndex]

    for count, i in enumerate(orderArray):
        for j in range(5):
            if handarray[i][j] < handarray[handIndex][j]:
                return orderArray[:count] + [handIndex] + orderArray[count:]
            elif handarray[i][j] == handarray[handIndex][j]:
                continue
            else:
                break
        else:
            continue
    orderArray.append(handIndex)
    return orderArray

def parse_file(file_path):
    ans = 0
    hands = []
    dicthands = []
    bids = []
    order = []
    winOrder = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    letters = ['A','K','Q','J','T']
    numberHands = []
    fiveKind = []
    fourKind = []
    fullHouse = []
    threeKind = []
    twoP = []
    oneP = []
    highCard = []
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                line = line.strip().split()
                hands.append(line[0])
                bids.append(int(line[1]))

        for count,hand in enumerate(hands):
             dicthands.append({})
             numberHands.append([])
             for char in hand:
                if char in dicthands[count]:
                    dicthands[count][char] +=1
                else:
                    dicthands[count][char] = 1

                if char in letters:
                    if char == 'A':
                        numberHands[count].append(int(14))
                    elif char == 'K':
                        numberHands[count].append(int(13))
                    elif char == 'Q':
                        numberHands[count].append(int(12))
                    elif char == 'J':
                        numberHands[count].append(int(1))
                    elif char == 'T':
                        numberHands[count].append(int(10))
                else:
                    numberHands[count].append(int(char))
                
        #print(dicthands[0])
        #print(len(dicthands[0]))
        #print(numberHands[1])
        for count,hand in enumerate(dicthands):
            if 'J' in hand and hand['J'] !=5:
                temp = hand['J']
                del hand['J']
                max_key = max(hand, key=hand.get)
                hand[max_key] += temp
            dictLength = len(hand)
            if dictLength == 1:
                fiveKind.append(count)
            elif dictLength == 5:
                highCard.append(count)
            elif dictLength == 2:
                max_key = max(hand, key=hand.get)
                if hand[max_key] == 4:
                    fourKind.append(count)
                else:
                    fullHouse.append(count)
            elif dictLength == 3:
                max_key = max(hand, key=hand.get)
                if hand[max_key] == 3:
                    threeKind.append(count)
                else:
                    twoP.append(count)
            elif dictLength == 4:
                oneP.append(count)
        #total = len(fiveKind)+ len(highCard) + len(fourKind) + len(fullHouse) + len(threeKind) + len(twoP) + len(oneP)
        #print('total len',total)
        # sort winning hands
        print("FiveKind")
        for index in fiveKind:
            if len(order)==0:
                order.append(index)
            else:
                order = findSpot(numberHands,order,index)
        
        temp = []
        print("FourKind")
        #print(fourKind)
        for index in fourKind:
            if len(temp) == 0:
                temp.append(index)
            else:
                temp = findSpot(numberHands,temp,index)
        order += temp
        #print(order)

        temp = []
        print("FullHouse")
        for index in fullHouse:
            if len(temp) == 0:
                temp.append(index)
            else:
                temp = findSpot(numberHands,temp,index)
        order += temp
        
        temp = []
        print("ThreeKind")
        for index in threeKind:
            if len(temp) == 0:
                temp.append(index)
            else:
                temp = findSpot(numberHands,temp,index)

        order += temp
        temp = []
        print("TwoPair")   
        for index in twoP:
            if len(temp) == 0:
                temp.append(index)
            else:
                temp = findSpot(numberHands,temp,index)

        order += temp
        temp = []
        print("OnePair")
        for index in oneP:
            if len(temp) == 0:
                temp.append(index)
            else:
                temp = findSpot(numberHands,temp,index)
        order += temp
        temp = []
        print("HighCard")
        for index in highCard:
            if len(temp) == 0:
                temp.append(index)
            else:
                temp = findSpot(numberHands,temp,index)
        order += temp
        
        print(len(order))
        for count,index in enumerate(order):
            ans += (1000-count)* bids[index]
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
print('Day7pt 1 and 2')
result = parse_file(file_path)
print('ans',result)
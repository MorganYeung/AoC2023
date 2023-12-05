import re
def parse_file(file_path):
    x = []
    y = []
    indexX = 0;
    indexY = 0;
    coordinates = []
    numList = ["1","2","3","4","5","6","7","8","9","0","\n"," "]
    tempAns = []
    ans = 0
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                for char in line:
                    x.append(char)
                y.append(x)
                x = []
            for yIndex, arr in enumerate(y):
                for xIndex, char in enumerate(arr):
                    if char != '.' and char not in numList:
                        #print(char)
                        coordinate = (xIndex,yIndex)
                        coordinates.append(coordinate)
            #print(coordinates)
        for coordinatePoint in coordinates:
            aboveL = False
            above = False
            aboveR = False
            belowL = False
            below = False
            belowR = False
            right = False
            left = False
            leftEdge = False
            topEdge = False
            rightEdge = False
            botEdge = False
            if coordinatePoint[1] == 0:
                topEdge = True
            if coordinatePoint[0] == 0:
                leftEdge = True
            if coordinatePoint[1] == (len(y)-1):
                bottomEdge = True
            if coordinatePoint[0] == (len(y[0])-1):
                rightEdge = True
            
            #print(y[coordinatePoint[1]][coordinatePoint[0]])
            #Check above
            if not topEdge and y[coordinatePoint[1]-1][coordinatePoint[0]] in numList:
                #Search around for other numbers until '.'
                above = True
            #check diagonal up right    
            if not topEdge and not rightEdge and y[coordinatePoint[1]-1][coordinatePoint[0]+1] in numList:
                #Search around for other numbers until '.'
                aboveR = True    
            #check right  
            if not rightEdge and y[coordinatePoint[1]][coordinatePoint[0]+1] in numList:
                #Search around for other numbers until '.'
                right = True
            #check diagonal down right  
            if not botEdge and not rightEdge and y[coordinatePoint[1]+1][coordinatePoint[0]+1] in numList:
                #Search around for other numbers until '.'
                belowR = True
            #check down  
            if not botEdge and y[coordinatePoint[1]+1][coordinatePoint[0]] in numList:
                #Search around for other numbers until '.'
                below = True
            #check diagonal down left  
            if not botEdge and not leftEdge and y[coordinatePoint[1]+1][coordinatePoint[0]-1] in numList:
                #Search around for other numbers until '.'
                belowL = True
            #check left  
            if not leftEdge and y[coordinatePoint[1]][coordinatePoint[0]-1] in numList:
                #Search around for other numbers until '.'
                left = True
            #check diagonal up left  
            if not leftEdge and not topEdge and y[coordinatePoint[1]-1][coordinatePoint[0]-1] in numList:
                #Search around for other numbers until '.'
                aboveL = True

            if aboveL or above or aboveR or belowL or below or belowR or right or left:
                print(coordinatePoint)
            if above:
                print("above")
                if not aboveL and not aboveR:
                    tempAns.append(int(y[coordinatePoint[1]-1][coordinatePoint[0]]))
                if aboveL and not aboveR:
                    temp = ''
                    for i in range(coordinatePoint[0], -1, -1):
                        if y[coordinatePoint[1]-1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]-1][i]
                    tempAns.append(int(temp[::-1]))
                if aboveR and not aboveL:
                    #has to be just aboveR
                    #print('aboveR')
                    temp = ''
                    #print(coordinatePoint)
                    #print(len(y[coordinatePoint[1]]))
                    for i in range(coordinatePoint[0], len(y[coordinatePoint[1]]), 1):
                        if y[coordinatePoint[1]-1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]-1][i]
                    tempAns.append(int(temp))
                    #print(int(temp))
                if aboveR and aboveL:
                    temp = ''
                    for i in range(coordinatePoint[0], len(y[coordinatePoint[1]-1]), 1):
                        if y[coordinatePoint[1]-1][i] not in numList:
                            for j in range(i-1, -1, -1):
                                if y[coordinatePoint[1]-1][j] not in numList:
                                    break
                                temp = temp + y[coordinatePoint[1]-1][j]
                            break
                    #print('right above')
                    #print(coordinatePoint)
                    #print(int(temp[::-1]))
                    tempAns.append(int(temp[::-1]))

            elif aboveL or aboveR:
                if aboveL:
                    temp = ''
                    #go left
                    print("aleft")
                    #print(coordinatePoint)
                    for i in range(coordinatePoint[0]-1, -1, -1):
                        if y[coordinatePoint[1]-1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]-1][i]
                    tempAns.append(int(temp[::-1]))
                    #print(coordinatePoint)
                    #print(int(temp[::-1]))           
                if aboveR:
                    #has to be just aboveR
                    print('aboveR')
                    temp = ''
                    #print(coordinatePoint)
                    #print(len(y[coordinatePoint[1]]))
                    for i in range(coordinatePoint[0]+1, len(y[coordinatePoint[1]]), 1):
                        if y[coordinatePoint[1]-1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]-1][i]
                    tempAns.append(int(temp))
                    #print(int(temp))
                
            #Right is easy
            if right:
                temp = ''
                print("right")
                #print(coordinatePoint)
                #print(len(y[coordinatePoint[1]]))
                for i in range(coordinatePoint[0]+1, len(y[coordinatePoint[1]]), 1):
                    if y[coordinatePoint[1]][i] not in numList:
                        break
                    temp = temp + y[coordinatePoint[1]][i]
                tempAns.append(int(temp))
                #print(int(temp))
            #left is easy in reverse
            if left:
                temp = ''
                print("left")
                #print(coordinatePoint)
                #print(len(y[coordinatePoint[1]]))
                for i in range(coordinatePoint[0]-1, -1, -1):
                    if y[coordinatePoint[1]][i] not in numList:
                        break
                    temp = temp + y[coordinatePoint[1]][i]
                #print(int(temp[::-1]))
                tempAns.append(int(temp[::-1]))

            if below:
                print("below")
                if not belowL and not belowR:
                    tempAns.append(int(y[coordinatePoint[1]+1][coordinatePoint[0]]))
                if belowL and not belowR:
                    temp = ''
                    for i in range(coordinatePoint[0], -1, -1):
                        if y[coordinatePoint[1]+1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]+1][i]
                    tempAns.append(int(temp[::-1]))
                if belowR and not belowL:
                    #has to be just belowR
                    #print('belowR')
                    temp = ''
                    #print(coordinatePoint)
                    #print(len(y[coordinatePoint[1]]))
                    for i in range(coordinatePoint[0], len(y[coordinatePoint[1]]), 1):
                        if y[coordinatePoint[1]+1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]+1][i]
                    tempAns.append(int(temp))
                    #print(int(temp))
                if belowR and belowL:
                    temp = ''
                    for i in range(coordinatePoint[0], len(y[coordinatePoint[1]+1]), 1):
                        if y[coordinatePoint[1]+1][i] not in numList:
                            for j in range(i-1, -1, -1):
                                if y[coordinatePoint[1]+1][j] not in numList:
                                    break
                                temp = temp + y[coordinatePoint[1]+1][j]
                            break
                    #print('right below')
                    #print(coordinatePoint)
                    #print(int(temp[::-1]))
                    tempAns.append(int(temp[::-1]))

            elif belowL or belowR:
                if belowL:
                    temp = ''
                    #go left
                    print("belowL")
                    #print(coordinatePoint)
                    for i in range(coordinatePoint[0]-1, -1, -1):
                        if y[coordinatePoint[1]+1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]+1][i]
                    tempAns.append(int(temp[::-1]))
                    #print(coordinatePoint)
                    #print(int(temp[::-1]))           
                if belowR:
                    #has to be just aboveR
                    print('belowR')
                    temp = ''
                    #print(coordinatePoint)
                    #print(len(y[coordinatePoint[1]]))
                    for i in range(coordinatePoint[0]+1, len(y[coordinatePoint[1]]), 1):
                        if y[coordinatePoint[1]+1][i] not in numList:
                            break
                        temp = temp + y[coordinatePoint[1]+1][i]
                    tempAns.append(int(temp))
                    #print(int(temp))
            if len(tempAns) == 2:
                ans = ans + tempAns[0]*tempAns[1]
            tempAns = []
            aboveL = False
            above = False
            aboveR = False
            belowL = False
            below = False
            belowR = False
            right = False
            left = False
            leftEdge = False
            topEdge = False
            rightEdge = False
            botEdge = False
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
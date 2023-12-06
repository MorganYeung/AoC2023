import re
def parse_file(file_path):
    seeds = []
    soils = []
    fertilizers = []
    waters = []
    lights = []
    temperatures = []
    humiditys = []
    locations = []
    ans = 69
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                line = line.strip().split()
                #print(count,line)
                if count == 0:
                    for item in line[1:]:
                        seeds.append(int(item))
                    #print(seeds)
                if count == 1 or count == 2:
                    continue
                elif count > 3:
                    if(len(line) != 3):
                        continue
                    if count < 37:
                        for seed in seeds:
                            if seed >= int(line[1]) and seed <= int(line[1])+int(line[2]):
                                #print(line,seed)
                                soils.append(int(line[0])+seed-int(line[1]))
                                #print(soils)
                        #print("soils",soils)
                    elif count < 80:
                        for soil in soils:
                            if soil >= int(line[1]) and soil <= int(line[1])+int(line[2]):
                                fertilizers.append(int(line[0])+soil-int(line[1]))
                        #print("fertilizers",fertilizers)
                    elif count < 124:
                        for fertilizer in fertilizers:
                            if fertilizer >= int(line[1]) and fertilizer <= int(line[1])+ int(line[2]):
                                waters.append(int(line[0])+fertilizer-int(line[1]))
                        #print("waters",waters)                    
                    elif count < 153:
                        for water in waters:
                            if water >= int(line[1]) and water <= int(line[1])+ int(line[2]):
                                lights.append(int(line[0])+water-int(line[1]))
                        #print("lights",lights)
                    elif count < 193:
                        for light in lights:
                            if light >= int(line[1]) and light <= int(line[1]) + int(line[2]):
                                temperatures.append(int(line[0])+light-int(line[1]))
                        #print("temperatures",temperature)
                    elif count < 208:
                        for temperature in temperatures:
                            if temperature >= int(line[1]) and temperature <= int(line[1]) + int(line[2]):
                                humiditys.append(int(line[0])+temperature-int(line[1]))
                        #print("humiditys",humiditys)         
                    elif count > 208:
                        for humidity in humiditys:
                            if humidity >= int(line[1]) and humidity <= int(line[1]) + int(line[2]):
                                locations.append(int(line[0])+humidity-int(line[1]))
                        #print("locations",locations)                       
            ans = min(locations)
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
print('Day5pt1')
result = parse_file(file_path)
print(result)
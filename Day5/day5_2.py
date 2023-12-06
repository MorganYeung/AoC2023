import re
def calculate_overlap(base, offset, target_start, target_end):
    overlap_start = max(base, target_start)
    overlap_end = min(base + offset, target_end)

    # Check if there is an overlap
    if overlap_start < overlap_end:
        return [overlap_start,overlap_end]
    else:
        return []  # No overlap


def parse_file(file_path):
    seeds = []
    seedrange = []
    seedend = []
    soils = []
    soilrange = []
    fertilizers = []
    fertilizerrange = []
    waters = []
    waterrange = []
    lights = []
    lightrange = []
    temperatures = []
    temperaturerange = []
    humiditys = []
    humidityrange = []
    locations = []
    locationsrange = []
    ans = 69
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):
                line = line.strip().split()
                #print(count,line)
                if count == 0:
                    for count, item in enumerate(line[1:]):
                        if count %2 == 0:
                            seeds.append(int(item))
                        else:
                            seedrange.append(int(item))
                    print("SEEDS")
                    print(seeds)
                    print("SEED RANGE")                    
                    print(seedrange)
                    for seed,temp in zip(seeds,seedrange):
                        seedend.append(seed+temp)
                    #print("SEED MAX") 
                    #print(seedend)
                if count == 1 or count == 2:
                    continue
                elif count > 3:
                    if(len(line) != 3):
                        continue
                    if count < 37:
                        if count == 4:
                            print("SEED TO SOIL")
                        for index, seed in enumerate(seeds):
                            soilOverlap = calculate_overlap(seed,seedrange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(soilOverlap) != 0:
                                #print(seed,seedrange[index],int(line[1]),int(line[2]))
                                #print(soilOverlap)
                                soils.append(int(line[0])+soilOverlap[0] -int(line[1]))
                                soilrange.append(soilOverlap[1]-soilOverlap[0])
                        #print("soils",soils)
                    elif count < 80:
                        if count == 38:
                            print("SOIL2FERT")
                        for index, soil in enumerate(soils):
                            fertOverlap = calculate_overlap(soil,soilrange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(fertOverlap) != 0:
                                fertilizers.append(int(line[0])+fertOverlap[0] -int(line[1]))
                                fertilizerrange.append(fertOverlap[1]-fertOverlap[0])
                        #print("fertilizers",fertilizers)
                    elif count < 124:
                        for index, fert in enumerate(fertilizers):
                            waterOverlap = calculate_overlap(fert,fertilizerrange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(waterOverlap) != 0:
                                waters.append(int(line[0])+waterOverlap[0] -int(line[1]))
                                waterrange.append(waterOverlap[1]-waterOverlap[0])
                        #print("waters",waters)                    
                    elif count < 153:
                        for index, water in enumerate(waters):
                            lightOverlap = calculate_overlap(water,waterrange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(lightOverlap) != 0:
                                lights.append(int(line[0])+lightOverlap[0] -int(line[1]))
                                lightrange.append(lightOverlap[1]-lightOverlap[0])
                        #print("lights",lights)
                    elif count < 193:
                        for index, light in enumerate(lights):
                            tempOverlap = calculate_overlap(light,lightrange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(tempOverlap) != 0:
                                temperatures.append(int(line[0])+tempOverlap[0] -int(line[1]))
                                temperaturerange.append(tempOverlap[1]-tempOverlap[0])
                        #print("temperatures",temperature)
                    elif count < 208:
                        for index, temp in enumerate(temperatures):
                            humidOverlap = calculate_overlap(temp,temperaturerange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(humidOverlap) != 0:
                                humiditys.append(int(line[0])+humidOverlap[0] -int(line[1]))
                                humidityrange.append(humidOverlap[1]-humidOverlap[0])
                        #print("humiditys",humiditys)         
                    elif count > 208:
                        for index, humidity in enumerate(humiditys):
                            locationOverlap = calculate_overlap(humidity,humidityrange[index],int(line[1]),int(line[1])+int(line[2]))
                            if len(locationOverlap) != 0:
                                locations.append(int(line[0])+locationOverlap[0] -int(line[1]))
                                locationsrange.append(locationOverlap[1]-locationOverlap[0])
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
print('Day5pt2')
result = parse_file(file_path)
print(result)
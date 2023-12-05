import re
def parse_file(file_path):
    parsed_data = 0
    try:
        with open(file_path, 'r') as file:
            for count, line in enumerate(file):

                for character in line:
                    if character == 'o':
                        line = re.sub('one','o1e',line)
                    if character == 't':
                        line = re.sub('two','t2o',line)
                        line = re.sub('three','t3e',line)                        
                    if character == 'f':
                        line = re.sub('four','f4r',line)
                        line = re.sub('five','f5e',line)
                    if character == 's':
                        line = re.sub('six','s6x',line)
                        line = re.sub('seven','s7n',line)
                    if character == 'e':
                        line = re.sub('eight','e8t',line)
                    if character == 'n':
                        line = re.sub('nine','n9e',line)
                line = line.lower()
                print(line)
                stringNum = re.sub('[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]','',line).strip()
                #print(stringNum)
                stringLength = len(stringNum)
                num = int(stringNum[0]+stringNum[stringLength-1])
                print(count+1,num)
                parsed_data = parsed_data + num
                #print(parsed_data)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An IO error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return parsed_data

# Example usage
file_path = 'input.txt'
print('Day1pt2')
result = parse_file(file_path)
print(result)
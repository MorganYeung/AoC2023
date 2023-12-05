import re
def parse_file(file_path):
    parsed_data = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.lower()
                stringNum = re.sub('[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]','',line).strip()
                print(stringNum)
                stringLength = len(stringNum)
                #print(stringLength)
                parsed_data = parsed_data + int(stringNum[0]+stringNum[stringLength-1])
                print(parsed_data)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An IO error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return parsed_data

# Example usage
file_path = 'input.txt'
result = parse_file(file_path)
print(result)
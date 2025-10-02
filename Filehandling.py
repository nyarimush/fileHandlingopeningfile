# {Nyari Mushaikwa]
# Year 1 T level
# [03/10/2025]
# Filehandling.py

#[comment]
def two():
    pass 



#read information from file 

def readFile(filePath):
    try:
        print(filePath)
        with open(filePath, "r") as file:
            content = file.read()
            print('hello')
        file.close()
        return content
    
    except FileNotFoundError:
        print("File not found")
        
    except Exception as e:
        print("Error occured:", e)



#Excecute main program
def main():
    filePath = "country.txt"
    print(readFile(filePath))
    


if __name__ == "__main__":
    main()

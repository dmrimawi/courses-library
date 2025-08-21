def read_file(filename):
    lines = []
    try:
        file = open(filename, "r")
        lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")
    except Exception as exp:
        print("Error reading the file,", str(exp))
    finally:
        file.close()
    return lines

def write_file(filename, data):
    try:
        file = open(filename, "w")
        file.write(data)
    except FileNotFoundError:
        print("File does not exist")
    except Exception as exp:
        print("Error reading the file,", str(exp))
    finally:
        file.close()


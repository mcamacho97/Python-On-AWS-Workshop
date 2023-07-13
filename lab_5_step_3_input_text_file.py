def open_input(file):
    with open(file, "r") as f:
        text = f.read() # We use read() to read the entire file into a string
        print(text)

def main():
    open_input("text.txt")

if __name__ == "__main__":
    main()
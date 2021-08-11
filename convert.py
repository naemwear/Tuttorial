def string_to_binary(text): # Make a function
    bin_conv = [] # make an empty list
    for c in text: # loop throw each character in text(string)
        ascii_val = ord(c) # use ord() to get the values
        bin_val = bin(ascii_val) # get the binary values
        # store them in the list and use [2:] to convert it to a binary string 
        bin_conv.append(bin_val[2:])
    bin_str = ('').join(bin_conv) # join all of the strings into one binary string
    with open('test.bin', 'wb') as f: # Open a file as binary write
        # convert the string to an int and use to_bytes() to convert it to binary
        # the first argument depends on how large the binary string is
        f.write(int(bin_str).to_bytes(50, byteorder='big'))

# Create the main func
def main():
    text_str = 'Hello' # create the string
    string_to_binary(text_str) # call the method

# Driver code
if __name__ == "__main__":
    main()
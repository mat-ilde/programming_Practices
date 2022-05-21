import re

def matchingReplancing(txt_file_to_open,new_txt_file):

    with open(txt_file_to_open, 'r') as file:
        # list to add the changed lines
        newlines = []
        filedata=file.readlines()
        #iterate between of the lines as string
        for line in filedata :
            # searching the matching
            if re.search('b', line) or re.search('d', line):
                #replacing the values
                line = line.replace('bbbb', '2')
                line = line.replace('dddd', '4')
                #appending to the list
                newlines.append(line)
    # close file
    #open file writw mode
    with open(new_txt_file, 'w') as file:
        # iterating list
        for new_file_data in newlines:
            #adding the new data to new txt file
            file.write(new_file_data)
    return new_txt_file

if __name__ == '__main__':

    #calling the function with the txt file to read, and the new txt file
    matchingReplancing('/home/mati/Escritorio/two.txt','/home/mati/Escritorio/new_line.txt')
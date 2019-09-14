from collections import deque
import pickle
class CharacterNode:

    def __init__(self,  weight, value = None, child_left = None, child_right = None):
        self.value = value
        self.weight = weight
        self.child_left = child_left
        self.child_right = child_right

def sort_array(array):
    for i in range(len(character_count)):
        min_value = character_count[i].weight
        index = i
        for j in range(i, len(character_count)):
            if(character_count[j].weight < min_value):
                min_value = character_count[j].weight
                index = j
        temp = character_count[i]
        character_count[i] = character_count[index]
        character_count[index] = temp
    return character_count
    
def find_element(root, elem):
    stack = deque()
    stack.append(root)
    while(stack):
        element = stack.pop()
        if(element.value is None):
            stack.append(element.child_left)
            stack.append(element.child_right)
        elif(element.value == elem):
            return element
    print("DNE")
    return "DNE"

def Create_Dict(root, code, dict):
    if(root.value is None):
        Create_Dict(root.child_left, code + "0", dict)
        Create_Dict(root.child_right, code + "1", dict)
    else:
        dict[root.value] = code
    return dict   

def Write_To_File(rawFile, encodedFile, charDict):
    with open(encodedFile, "w") as outfile:
        outfile.write("")
    with open(rawFile) as infile:
        encodedLine = ""
        for line in infile:
            #print(line)
            for letter in line:
                code = charDict[letter]
                for oneorzero in code:
                    encodedLine += oneorzero
                    if(len(encodedLine) == 8):
                        binary = int(encodedLine, 2)
                        #print(binary)
                        with open(encodedFile, "ab") as outfile:
                            s = chr(binary).encode("UTF-8")
                            try:
                                outfile.write(bytes(s))
                            except:
                                #print(binary,chr(binary))
                                outfile.write(s)
                        encodedLine = ""
        while(len(encodedLine) != 8 and len(encodedLine) != 0):
            encodedLine+="0"
        binary = int(encodedLine, 2)
        s = chr(binary).encode("UTF-8")
        with open(encodedFile, "ab") as outfile:
            outfile.write(bytes(s))
##Go through the file in an efficient way and create a Node for each one, and
#Get the frequency of every character. Only ASCII values supported, if they do not appear, they are a None in the array.
character_count = [None] * 127
with open("TextFile1.txt") as infile: ##memory kept only as large as the line is
    for line in infile:
        for letter in line:
            if(character_count[ord(letter)] is None):
                character_count[ord(letter)] = CharacterNode(1, letter)
            else:
                character_count[ord(letter)].weight += 1

#Remove all of the unused characters
for element in character_count[:]:
    if(element is None):
        character_count.remove(element)
        #print('None')
    else:
        pass
        #print(element.value, element.weight)

#Sorted All elements
character_count = sort_array(character_count)

for element in character_count[:]:
    if(element is None):
        print('None')
    else:
        print(element.value, element.weight)

##build the Huffman Tree
while(len(character_count) > 1):

    parent = CharacterNode(character_count[0].weight + character_count[1].weight, None, character_count[0], character_count[1])
    
    character_count.remove(character_count[0])
    character_count.remove(character_count[0])
    
    character_count.append(parent)
    character_count = sort_array(character_count)

root = character_count[0]
Node = find_element(root, 'b')
print(Node.value)

##build dictionary
charDict = dict()
charDict = Create_Dict(root, "", charDict)

##Writes and encodes the file
Write_To_File("TextFile1.txt", "EncodedData.bnr", charDict)


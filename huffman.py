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
    

a = CharacterNode(1, 'a')
b = CharacterNode(2, 'b')
c = CharacterNode(3, None, a, b)

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

while(len(character_count) > 1):
    parent = CharacterNode(character_count[0].weight + character_count[1].weight, None, character_count[0], character_count[1])
    
    character_count.remove(character_count[0])
    character_count.remove(character_count[0])
    
    character_count.append(parent)
    character_count = sort_array(character_count)

print("Done?")


##build the Huffman Tree
#Part 2 Recursion
def sum_of_threes(x):
    if x <= 2:
        return 0
    if x % 3 == 0:
        return x + sum_of_threes(x - 1)
    else:
        return sum_of_threes(x - 1) 

def is_in_list(lis, x):
    if len(lis) == 0:
        return False
    else:
        return helper_in_list(lis,x,len(lis)-1)

def helper_in_list(lis, x, size):
    if size < 0:
        return False
    if lis[size] == x:
        return True
    else:
        return helper_in_list(lis, x, size - 1)

#Part 3 Dynamic Arrays
class ArrayList():
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    # appends an item to the array, when array is full then go double the size before being able to append more items
    def append(self, value):
        if self.size >= self.capacity:
            self.double_arr()
        self.arr[self.size] = value
        self.size += 1

    # silly way to remove the first item in the array by moving every item down by 1
    def remove_first(self):
        if self.size <= 0:
            return
        for i in range(self.size):
            self.arr[i] = self.arr[i+1]

    # Returns the size of the array
    def get_size(self):
        return self.size

    # Prints the array with space between each item in the array
    def print_list(self):
        print(*self.arr, sep=" ")
    
    # if the capacity of the arr is full, double its size
    def double_arr(self):
        new_size = self.capacity * 2
        tempArr = [None] * new_size
        for i in range(self.size):
            tempArr[i] = self.arr[i]
        self.arr = tempArr
        self.capacity = new_size

# Part 4: General Programming
class Animal():
    def __init__(self):
        self.id = " "
        self.species = " "
        self.weight = 0

    # Returns the animal's id number
    def get_id(self):
        return self.id
    
    # Returns the animal's species
    def get_species(self):
        return self.species
    
    # Returns the animal's weight
    def get_weight(self):
        return self.weight

    # Updates the animal's id number with the vlue in id
    def set_id(self, id):
        self.id = id

    # Updates the animal's species with the value in species
    def set_species(self, species):
        self.species = species

    # Updates the animal's weight with the value in weight
    def set_weight(self, weight):
        self.weight = weight

    # Format of the string should be "<id>: <species>, <weight> kilograms"
    def __str__(self):
        return ("{}: {}, {} kilograms".format(self.id,self.species,self.weight))

# I am totally lost here
class zoo():

    #Add a animal to the zoo with the id number, species and weight provided
    #If a animal already has this id, overwrite it
    def add_animal(self, id, species, weight):
        return 0

    #if an animal with this id number is in the zoo
        #Return an instance of the class Animal with the corresponding iformation
    #else return None
    def get_animal(self,id):
        return 0

    #If an animal with this id number is in the zoo, change its species to new_species
    def change_species(self, id, new_species):
        return 0

    #If an animal with this id number is in the zoo, change its weight to weight
    def change_weight(self, id, weight):
        return 0
    
    # Should return the string in same format as formatted for Animal, 
    # Each animal in the zoo in one line
    # Example for zoo with more than one animal:
    # 12345: my animal, 100 kilograms
    # 23456: your animal, 200 kilograms
    # etc....
    def __str__(self):
        return Animal.__str__(self)

# Example usage for Zoo and Animal Class
# zoo = Zoo()
# zoo.add_animal("12")
# animal = zoo.get_animal("12")
# animal.set_species("elephant")
# print(zoo)
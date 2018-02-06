# A simple fantasy text adventure demo

#############################################################
# GameObject super class from which other objects descend.
#############################################################
class GameObject:
    class_name = ""
    desc = ""
    objects = {} #empty dictionary

    def __init__(self, name):
        self.name = name
        # Add self to the objects dictionary
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

#############################################################
# Game Objects available in the game
#############################################################
# Goblin subclass
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature" # weakly private
        super().__init__(name)

    @property
    def desc(self): # rules for accessing desc
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

##############################################################
# Instantiate objects that are present during runtime
##############################################################
# Declare a goblin object
goblin = Goblin("Gobbly")

##############################################################
# Define verb actions
##############################################################
# Examine option looks at a noun for details
def examine(noun):
    if noun in GameObject.objects:
        # if the noun word exists, use its name as a key
        # and get its description
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)

#define hit verb
def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin: # hit changes based on class
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

# The basic speaking action
def say(noun):
    return 'You said "{}"'.format(noun)

# Dictionary containing all available actions
verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
}

################################################################
# Infrastructure code underneath the game loop
################################################################
def get_input():
    command = input(":").split() #split commands
    verb_word = command[0] #first word is verb
    if verb_word in verb_dict: #can action be done?
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return # exit if verb isn't doable

    if len(command) >= 2: # there is a noun too
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

################################################################
# Game loop
################################################################
while True:
    get_input()

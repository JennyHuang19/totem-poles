'''
Created on Sep 12, 2019

@author: JennyH
'''
#Yijian Jenny Huang 

import random 

def part_hair_flat():
    """
    Returns a string that is
    flat hair
    """
    a1 = r"012345678901234567"
    a2 = r" TTTTTTTTTTTTTTTT "
    return a2

def part_hair_curly():
    """
    Returns a string that is
    curly hair
    """
    a1 = r"012345678901234567"
    a2 = r" @@@@@@@@@@@@@@@@ "
    return a2

def part_hair_wild():
    """
    Returns a string that is
    wild hair
    """
    b  = r"012345678901234567"
    a  = r"       %          " + "\n"
    a += r"      ***         " + "\n"
    a += r"     ***%%        " + "\n"
    a += r"    %***%%&%      " + "\n"
    a += r"  &&%%****%%&&    " + "\n"
    a += r" %%&&%%****%%&%   "
    return a
      

def part_eyes_basic():
    """
    Returns a string that is 
    basic eyes.
    """
    a  = r"012345678901234567"
    a  = r" |   ~      ~   | " + "\n"
    a += r" |   0      0   | "
    return a

def part_eyes_spunkyglasses():
    """
    Returns a string that is
    eyes with glasses
    """
    a  = r"012345678901234567"
    a  = r" | *****  ***** | " + "\n"
    a += r" | | ~ |  | ~ | | " + "\n"
    a += r" | | 0 |--| 0 | | " + "\n"
    a += r" | *****  ***** | "
    return a
    
def part_eyes_winking():
    """
    Returns a string that is
    eyes winking
    """
    a  = r"012345678901234567"
    a  = r" |   ~       ~  | " + "\n"
    a += r" |  0        <  | " + "\n"
    a += r" | ---      --- | " 
    return a

def part_nose_pig():
    """
    Returns a string that is
    a pig nose
    """
    a  = r"012345678901234567"
    a  = r" |     _____    | " + "\n"
    a += r" |    / o o \   | " + "\n"
    a += r" |    \____ /   | " + "\n"
    return a


def part_nose_down():
    """
    Returns a string that is
    a nose pointed down
    """
    a  = r"012345678901234567"
    a  = r" |    \ --- /   | " + "\n"
    a += r" |     \ | /    | " + "\n"
    a += r" |      \|/     | " 
    return a

def part_nose_bowtie():
    """
    Returns a small bow tie-shaped 
    nose
    """
    a  = r"012345678901234567"
    a  = r" |     6> <3    | " 
    return a
    
def part_nose_star():
    """
    Returns a star-shaped nose
    """
    a  = r"012345678901234567"
    a  = r" |      <^>     | "
    return a

def part_mouth_surprised():
    """
    Returns a string that is 
    a surprised mouth
    """
    a  = r"012345678901234567"
    a  = r" |       _      | " + "\n"
    a += r" |      (_)     | "      
    return a    

def part_mouth_mustache(): 
    """
    Returns a string that is 
    a mouth with a mustache.
    """
    a  = r"012345678901234567"
    a  = r" |    _==_==_   | " + "\n"
    a += r" |      ---     | "      
    return a  


def part_mouth_braces(): 
    """
    Returns a string that is 
    a mouth with braces.
    """
    a  = r"012345678901234567"
    a  = r" |              | " + "\n"
    a += r" | [*][*][*][*] | " + "\n"
    a += r" | [*][*][*][*] | "      
    return a

def part_chin_basic():
    """
    Returns a string that is 
    a simple chin.
    """
    a  = r"012345678901234567"
    a  = r" |______________| "      
    return a

def part_chin_squiggle():
    """
    Returns a string that is 
    a squiggly chin
    """
    a  = r"012345678901234567"
    a  = r" |~~~~~~~~~~~~~~| "  
    return a 




def bird_head():
    """
    Print a head that looks a like
    a bird, with a down-turned nose
    and surprised mouth
    """
    print(part_hair_curly())
    print(part_eyes_basic())
    print(part_nose_down())
    print(part_mouth_mustache())
    print(part_chin_basic())
    
    
def cute_head():
    """
    Print a head that looks cute,
    with winking eyes, a bow tie
    nose, and a surprised mouth
    """
    print(part_hair_flat())
    print(part_eyes_winking())
    print(part_nose_bowtie())
    print(part_mouth_surprised())
    print(part_chin_squiggle())
    
def stars_head():
    """
    Print a head that has stars throughout,
    with spunky glasses, a star
    nose, and braces
    """
    print(part_hair_curly())
    print(part_eyes_spunkyglasses())
    print(part_nose_star())
    print(part_mouth_braces())
    print(part_chin_basic())
    
    
def head_with_hair(hairfunc):
    """
    Print a head that looks cute,
    with winking eyes, a bow tie
    nose, and a surprised mouth, 
    but hair specified by hairfunc
    """
    print(hairfunc())
    print(part_eyes_winking())
    print(part_nose_bowtie())
    print(part_mouth_surprised())
    print(part_chin_squiggle())
     
     
def head_with_mouth(mouthfunc):
    """
    Print a head that looks a like
    a bird, with a down-turned nose
    and mouth specified by mouthfunc
    """
    print(part_hair_curly())
    print(part_eyes_basic())
    print(part_nose_down())
    print(mouthfunc())
    print(part_chin_basic())
    
def head_with_eyes(eyesfunc):
    """
    Print a head that looks cute,
    with flat hair, a bow tie
    nose, a surprised mouth, 
    but eyes specified by eyesfunc
    """
    print(part_hair_flat())
    print(eyesfunc())
    print(part_nose_bowtie())
    print(part_mouth_surprised())
    print(part_chin_squiggle())
    
def selfie_band():
    """
    Generates a selfie band with
    my net ID yjh3.
    """
    a  = r"012345678901234567"
    a  = r" +--------------+ " + "\n"
    a += r" |yjh3      yjh3| " + "\n"
    a += r" +--------------+ "          
    return a

def selfie(hairfunc, mouthfunc): #when functions are in arguments, no need to put parenthesis. Inside the code block, but parenthesis.
    """
    prints a head that has a 
    selfie band, basic eyes, a down
    turned nose, a basic chin, and hair
    and mouth specified by hairfunc and
    mouthfunc.
    """
    
    print(hairfunc()) #hairfunc() is the function the argument will specify. Arguments can be functions.
    print(selfie_band())
    print(part_eyes_basic())
    print(part_nose_down())
    print(mouthfunc())
    print(part_chin_basic())
    

def head_with_two(eyesfunc, mouthfunc):
    """
    Print a cute head with randomly chosen
    hair and eyes
    """
    print(part_hair_flat())
    print(eyesfunc())
    print(part_nose_bowtie())
    print(mouthfunc())
    print(part_chin_squiggle())
    
def head_random():
    """
    Print a head with randomly chosen
    mouth and eyes
    """
    eyesfunc = part_eyes_basic
    mouthfunc = part_mouth_braces
    x = random.randint(1,3)
    if x == 1:
        mouthfunc = part_mouth_mustache
    elif x == 2:
        eyesfunc = part_eyes_winking
    else:
        mouthfunc = part_mouth_surprised
        eyesfunc = part_eyes_spunkyglasses
        
    head_with_two(eyesfunc, mouthfunc)


def totem_fixed():
        """
        Print the same totem pole with three
        heads, one a bird, one cute, one filled with stars
        """
        bird_head()
        cute_head()
        head_with_eyes(part_eyes_spunkyglasses)
        
def totem_selfie():
        """
        Print a totem pole with selfie band
        By calling the selfie() helper function
        """
        selfie(part_hair_curly, part_mouth_braces)
        selfie(part_hair_flat, part_mouth_mustache)
        selfie(part_hair_wild, part_mouth_surprised)
        
def totem_random():
        """
        Print a totem pole with randomly chosen
        mouth and eyes
        """
        head_random()
        head_random()
        head_random()

if __name__ == '__main__':  

#     print("\nfixed totem\n")
#                            
#     totem_fixed()
#          
#     print("\nself totem\n")
#                 
#    
#     totem_selfie()
#              
#     print("\nrandom totem\n")
#              
#               
#     totem_random()
    print(selfie_band())

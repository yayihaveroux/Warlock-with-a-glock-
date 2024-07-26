import os
import sys
import time
import random
import colorama
from pygame import mixer

# map for use when player views map
map = '''
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------*@@@@*-@@@@@@@@)-------------------------------------------**----------------------------*)--)@}-*-----------------------------------
--------------)@@@@@@@--@@@@@@@@@)-------------------------------------*@@@@@}---@@}-----------------*@}@@)@@@@)}@}@}---------------------------------
-------------*@@@@@@}*@@@@@@@@@@}--------------------------------------)@@))}*)@@@@@------------------)@})})})))))))}}@-*-----------------------------
----------------}}*--}*-}@@)-})-*---------------------------------------------@@@@@)--------------------@})}})})))))))})}@@}*-------------------------
----------------}@@------------------------------------------------------------------------------------)@}))))))))})))}))))}}@@@@@}-------------------
---------------------------------------------------------------------------------------------------------}@@))}}))))))))))))))))))@@*)}*--------------
-----------------------------------------------------------------------------------------------------------*@})))) Pyro Wizard)))})))}@*--------------
-------------------------------------------------------------------------------------------------------------@}))))}}))}})))))})))})@*----------------
-------------------------------------------------------------------------------------------------------------*@}))))))}}})}}))))))})@*----------------
-----------------)@}}**}**)@}--------------------------------------------------------------------------------)@))}))}))}))}))})})))))}@*--------------
-----------------*@@@@@@@@@@@@@@@)*}@@@@@---------------------------------------------------------------------}@}))}))})}}))))))}}))}})}@-------------
-----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@}------------------------------------------------------------------@@})))})}))}})))))))))))@}**----------
----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*------------------------------------------------------------------*@}}}))))))))}}}})})))))}}}@---------
----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@----------------------------------------------------------------------@})))))))}))))}}))}@@)*---------
----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*----------------------------------------------------------------------*@}))}))))))}))))}@*-----------
--------------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@----------------------------------------------------------*@@@@)--------*@))}) Ignisum }]@------------
-------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}*-*------------------------------------------------------)@@@@@@@@@@@@@@}})))})})})))))@-------------
------------)@@@@@@@@@@ Wizard King @@@@@@@@@@@@@@------------------------------------------------**@@@@@@@@@@@@@@@@@@@@@@@@})))}}}@}@@@--------------
------------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*----------------------------------------*}}}*-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}-*-----------------
--------------}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-----------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-----)}-----**------
----------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*--------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)---@@@@@-----@@*-----
---------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)*--------------------------------------*@@@@@@@@@@@@}@}@@-----@@@@@@@@@@@@@@@@)-----*}@@@}---@)------
---------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--------------------------------------}@@@@@@@@@@@ Shadow Wizard @@@@@@@@@@@})-------*@@@@)@@@*-@*------
-------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@---------------------------------------@@@@@@@@@@@@@@@@-----@@}--*)@@@@@@@@@}------@@* Hydro Wizard *@*--
------------)@@@@@@@@@@@@@@@ Wizard Casino @@@-------------------------------------)@@@@@@@@@@@@@@@)------)@@@@@@@@@@@@@@-------@@@*--)})@@)-*@@)@----
----------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*---------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*----------@@-@@@@@*@@@*@----
----------@@@@@@@@@@@@@@@@@@@@@)--*}@@@@@*-----------------------------------------}@@@@@@@@@@@ Tenebrius @@@@@@@@@@@@@@-)@--------)@@@*@@)@@}}-@)}@--
-------------****@@*-----@@@**-------**-------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-----*@} Humidum @@@*@@*-
--------------------------------------------------------------------------------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}----*@@*@*@@}@}--@)*----
------------------------------------------------------------------------------*)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-------@@@@))**}@-@*)---
------------------------------------------------------------------------------@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@---------*--*---)@}--@)}--
--------------------------------------------------------------------------*@@@@@@@@@@@@@@@@@@}@@}-----*@@@@@@@@@@@@@@@@@@@@@@-------------------------
--------------------------------------------------------------------------)@@@@@@@@@@@@@@@@@@@@@@}----)@@@@@@}@}@@@@@@@@@}}}@*------------------------
--------------------------------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@---------@@}} Air Wizard }}}@@------------------*)@@)
--------------------------------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@*---------@@@@@@@}@@@}@}@@}@@@)----------------@@@@@)*
-------------------------------------------------------------------------*@ Saxus Village @@@@@@@@)@--------*@@@@@@@@@}}}@@}@@@----------Ventus Bay---
-----------------------------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)------*----@@@@@@@@}}@@@@@@)----**@@@@@@@@@@-----
-----------------------------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)----------@@}@@@@}@@@@}}}@@@@-@@@@@@@@@}}@@*----
------------------------------*@@@@@*-----------------------------------)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-----------*@@@@@@@@@@@@@@@@}@@@@@@}}@@*------
---------------------------*}@@@@@@@}----------------------------------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-------------)@@@}@}@@@@@@@@@}}}@}@}@@@@@*------
---------------------------)@@@@@@@@)---------------------------------}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@--------------*@@@@}@}@@@@}}@@@@@@@@@@@}-------
----------------------------}@@@@@@@@---------------------------------)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@}-----------------*)}@*-*@@@@@@@@@@@@@@@@)------
-------------------------------)@@@@*-------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*---------------*-------*)*@@@@@@-*}@@@)------
-------------------------------------------------------------------------*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*------------------------------)}-------------
-----------------------------------------------------------------------------@@@@@@ Geo Wizard @@@@@@@@@)*--------------------------------------------
-----------------------------------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-------------------------------------------
------------------------------------------------------------------------------@@@@@@@@@@@@@@@@}***@)----*@--------------------------------------------
--------------------------------------------------------------------------------------@@@))}----------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------*---------------------------------
-------------------------------------------------------------------------------------------------------------------)@@@-------------------------------
--------------------------------------------------------------------------------------------------------------------*)--------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------'''
os.system('cls' if os.name == 'nt' else 'clear')

# set color to white upon startup
print(colorama.Fore.WHITE)


#any time you see an input(), its so that the user can press enter and continue

# initialising mixer to play music and sounds. can only play one song at once.
mixer.init()

#music must be loaded before playing.
mixer.music.load("assets/happy.mp3")
mixer.music.set_volume(0.7)

# use -1 to loop infinitely.
mixer.music.play(-1)



# If you want to add more sfx make sure you specify sound. sounds can use multiple channels
#initialising sounds
revolverSound = mixer.Sound("assets/revolver.mp3")
assaultRifleSound = mixer.Sound("assets/assaultrifle.mp3")
pistolSound = mixer.Sound("assets/pistol.mp3")
shotgunSound = mixer.Sound("assets/shotgun.mp3")
reloadSound = mixer.Sound("assets/reload.mp3")
wizardcry1 = mixer.Sound("assets/wizardcry1.mp3")
wizardcry2 = mixer.Sound("assets/wizardcry2.mp3")
wizardcry3 = mixer.Sound("assets/wizardcry3.mp3")
walmart = mixer.Sound("assets/walmart.mp3")
portal1 = mixer.Sound("assets/portal1.mp3")
portal2 = mixer.Sound("assets/portal2.mp3")
eagle = mixer.Sound("assets/eagle.mp3")
type = mixer.Sound('assets/type.mp3')



# creating player variables

playerName = str()
playerHealth = 100
playerDefence = 50
playerTempDefence = 0
playerActionPoints = 3
playerMoney = 0
playerHasArmour = False
playerHasGlasses = False
playerHasMap = False
playerOutfit = 0
playerOutfitsList = [
	'''

                                                                                
                                                                                
                                     :++~,,"                                    
                                 /i          <i                                 
                               ^               l                                
                               t                ]                               
                                                 _                              
                              t                   ,                             
                              ,                                                 
                              .                                                 
                               ^                 ^                              
                               1                 x                              
                                k_             xZ                               
                                 n             +                                
                                  >           0                                 
                                  _           @                                 
                                 '            ,                                 
                                w               J                               
                            +1                     ()'                          
                     f{]'                               ^1)|                    
                  (                                          .1                 
                 }                                             0                
                x                                               h               
                _                                               t               
                                                                +               
                _                                               #               
                -                                               #               
                                                                <               
                                                                <               
                .                                               }               
                -                                               #               
                                                                ~               
               W                                                 "              
               @                                                 _              
               _         f                             $         r              
                        oi                              [        X              
              -           ]                           Z !        'i             
              ;        0  >                           .  t        f             
             [        ;    ,                         l   ;         1            
            ~`        r   _                           I   n        t            
            -         `   j                           m   _         1           
            ,        t   ,                                 <        m           
           ~         _   ,                                 o        b           
           d        X    f                             "             i           
           b        !    -                             @    p        b          
           b       a    <                                    l       i          
           k      !     *                               _    ]       i          
           -     l      +                               Y     f      i          
                 _                                      I      0     0          
          +     X      _                                 _      [    z          
          t    c       t                                 ]      x    ;          
          1    z      l                                   :           [         
         {            }                                   0     #     t         
         )      _     /                                   <            t        
        r       t    .                 In                      _       _        
        i    z; ,:   t                 } i                 <   -  0     i       
        _   ' 1  +   t                 _ k                 <   ; O Y   ,        
        -    }+      t                 ! {                 #      C    I        
         _     ,     _                ;  ^                 #     I     -        
          X   x      _                O   _                #      + '(          
                     _                _   b                #                    
                     _                    ^                #                    
                     _               @     -               #                    
                     _               l     t               #                    
                     _              _       {              #                    
                     _              |       ~              #                    
                     _             )         z             *                    
                     t            '          '             +                    
                     1            f           +            ,                    
                     .            c           #                                 
                      /           [           O           ]                     
                      /                                   _                     
                      t          b             Q          _                     
                      t                         I         _                     
                      t         d               _         .                     
                                <               l                               
                     -         _                 x         <                    
                     /         t                 ;         o                    
                     +         (                 |         }                    
                    <          >                 n          '                   
                    b          ^                 ^          b                   
                    _           i               {           b                   
                    _           !               {           b                   
                    b          :                 `          d                   
                    k          -                 n          +                   
                    i          {                 <                              
                    ;         )                   i                             
                     ,        _                   d        _                    
                     _        ^                   >        *                    
                     t       ]                     -       <                    
                     .       O                     r                            
                      /      _                     b      -                     
                      /      _                     |      n                     
                      -                            i      n                     
                      ,                            !      `                     
                      _      [                     h      x                     
                      r      !                            J                     
                      }      /                     k      +                     
                     r       _                     b       Y                    
                   x         +                     b         t                  
                   X                               |         x                  
                                                                                
                                                                                
                                                                                
                                                                              ''',
	'''                                                                                
                                     l@@ai      I@@@@                           
                                     w@@@@@@@d]a@@l                             
                                    *@@@@@@@@@@@@_                              
                                    $@@@@@-                                     
                                   W@@@@@@@                                     
                                  .@@@@@@@@@o                                   
                                  @@@@@@@@@@@$                                  
                                  /@@@@@@@@@@@Y                                 
                                  c@@@@@@@@@@@@                                 
                                 >@@@@@@@@@@@@@                                 
                                *@@@@@@@@@@@@@@@                                
                               Z@@@@@@@@@@@@@@@@@"                              
                        ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B                      
                       W@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$'                      
                         x@@@@@@@@@@@@n|k@@@@@@@Ox   ;(I                        
                           i|/tZ///i             J                              
                               _                 J                              
                               ]                 v                              
                                l               >                               
                                 x             z                                
                                 ^{           p@$c                              
                              m$@@#           @@@@@$                            
                             m@@@@*           #@@@@@                            
                              c@@@            -@@@W                             
                            O@@@{               .@@@@,                          
                     ^C@@@@@@@@@d               {@@@@@@@vl                      
                   k@@@@@@@@@@@@@               O@@@@@@@@@@@@                   
                  }@@@@@@@@@@@@@@p              O@@@@@@@@@@@@@w                 
                 )@@@@@@@@@@@@@@@@>             M@@@@@@@@@@@@@@C                
                 @@@@@@@@@@@@@@@@@b            "@@@@@@@@@@@@@@@@                
                +@@@@@@@@@@@@@@@@@*            w@@@@@@@@@@@@@@@@c               
                +@@@@@@@@@@@@@@@@@W            @@@@@@@@@@@@@@@@@b               
                 @@@@@@@@@@@@@@@@@W           !@@@@@@@@@@@@@@@@@{               
                 @@@@@@@@@@@@@@@@@W           n@@@@@@@@@@@@@@@@@                
                 @@@@@@@@@@@@@@@@@W           0@@@@@@@@@@@@@@@@@                
                 B@@@@@@@@@@@@@@@@W           k@@@@@@@@@@@@@@@@@                
                 @@@@@@@@@@@@@@@@@M           c@@@@@@@@@@@@@@@@@.               
                 @@@@@@@@@@@@@@@@@a           ^@@@@@@@@@@@@@@@@@r               
                X@@@@@@@@@@@@@@@@@|            @@@@@@@@@@@@@@@@@/               
                @@@@@@@@@@@@@@@@@@|            @@@@@@@@@@@@@@@@@k               
               [@@@@@@@@@@@@@@@@@@k            @@@@@@@@@@@@@@@@@@/              
               k@@@@@@@@@vJ@@@@@@@@^           @@@@@@@B@@@@@@@@@@*              
              i@@@@@@@@@d @@@@@@@@@0          -@@@@@@@O-@@@@@@@@@$              
              M@@@@@@@@@p @@@@@@@@@M          ]@@@@@@@O B@@@@@@@@@a             
             d@@@@@@@@@@[n@@@@@@@@@J          ]@@@@@@@* O@@@@@@@@@@             
            ^@@@@@@@@@@Q @@@@@@@@@@n          ]@@@@@@@@IJ@@@@@@@@@@@            
            W@@@@@@@@@@  @@@@@@@@@@i          ]@@@@@@@@* @@@@@@@@@@@            
           x@@@@@@@@@@O ^@@@@@@@@@@           ]@@@@@@@@@ 1@@@@@@@@@@r           
           $@@@@@@@@@@| w@@@@@@@@@@           i@@@@@@@@@{ *@@@@@@@@@@           
           @@@@@@@@@@@"{@@@@@@@@@@@           !@@@@@@@@@$  @@@@@@@@@@h          
           @@@@@@@@@@B @@@@@@@@@@@@n          -@@@@@@@@@@  m@@@@@@@@@@_         
          ^@@@@@@@@@@ k@@@@@@@@@@@@@          v@@@@@@@@@@)  @@@@@@@@@@@:        
          @@@@@@@@@@vl@@@@@@@@@@@@@@          x@@@@@@@@@@$  #@@@@@@@@@@@        
         f@@@@@@@@@@ r@@@@@@@@@@@@@@          J@@@@@@@@@@@@ /@@@@@@@@@@@$       
         @@@@@@@@@@Y c@@@@@@@@@@@@@@          B@@@@@@@@@@@@@ M@@@@@@@@@@@$      
        $@@@@@@@@@@k +@@@@@@@@@@@@@@>        -@@@@@@@@@@@@@@,*@@@@#cB@@@@m      
      X@@@@@ >Z@@@@@ |@@@@@@@@@@@@@@n        [@@@@@@@@@@@@@@f@@@    t@B1        
        m@@-     @@@ @@@@@@@@@@@@@@@z         @@@@@@@@@@@@@@*@@      l          
          1      [l #@@@@@@@@@@@@@@@          Q@@@@@@@@@@@@@Y t      x          
          -         @@@@@@@@@@@@@@@@   t@/    J@@@@@@@@@@@@@Y 1       +         
              tr  d @@@@@@@@@@@@@@@t   C@Z    c@@@@@@@@@@@@@@l  }~    -         
          i   t 1x .@@@@@@@@@@@@@@@    *@w    m@@@@@@@@@@@@@@ -~ {    :         
          d     )  Q@@@@@@@@@@@@@@W    @@#    #@@@@@@@@@@@@@@   >    I          
           c    /  @@@@@@@@@@@@@@@o   <@@@    h@@@@@@@@@@@@@@*  +   `           
              l    @@@@@@@@@@@@@@@W   Z@@@p   f@@@@@@@@@@@@@@*   ;              
                  k@@@@@@@@@@@@@@@W   @@@@M    O@@@@@@@@@@@@@@"                 
                 ^@@@@@@@@@@@@@@@@@  r@@@@@>   ^@@@@@@@@@@@@@@@1                
                 W@@@@@@@@@@@@@@@@@^ h@@@@@@   1@@@@@@@@@@@@@@@o                
                d@@@@@@@@@@@@@@@@@@[ @@@@@@@   p@@@@@@@@@@@@@@@@)               
               >@@@@@@@@@@@@@@@@@@@xa@@@@@@@@  I@@@@@@@@@@@@@@@@!               
               X@@@@@@@@@@@@@@@@@@$,@@@@@@@@@   Z@@@@@@@@@@@@@@@/               
               M@@@@@@@@@@@@@@@@@@$@@@@@@@@@@$  O@@@@@@@@@@@@@@@@,              
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  m@@@@@@@@@@@@@@@@@              
              ,@@@@@@@@@@@@@@@@@@@w@@@@@@@@@@@; @@@@@@@@@@@@@@@@@@$             
              c@@@@@@@@@@@@@W/    m@@@@@@@@@@@*i@@#f((XooB@@@@@@@@@t            
              @@@@@@@@@cI`        @@@@@@@@@@@@@          j@@@@@@@@@@            
               /@@@@@@@{         v@@@@@@@@@@@@@t         ()   v@@dr             
                       _         +             _         [                      
                       ;        ,               }                               
                      .         x               _                               
                      t        i                 :        <                     
                      _        _                 {        d                     
                      `         '               :                               
                     X          /               _          v                    
                     c          _               t          @                    
                     _          _               t          @                    
                     n          f               +          @                    
                     J          i               :          +                    
                     l         -                 :                              
                     ^         {                 |                              
                      ,       .                           _                     
                      ]       f                   c       b                     
                      t       _                   1       !                     
                      .       ,                   >                             
                       _     ,                           _                      
                       -     v                     -     Y                      
                       1     J                     _     x                      
                       -     Y                     -     :                      
                       _      ,                   ]      Y                      
                       +      !                   (      _                      
                      .      :                                                  
                     t       {                             n                    
                    _        z                              d                   
                      :tr___f                       zJJJzv:                     
                                                                '''
]
# array used to store items the user has
items = []

# array used tto store message history
history = []


# class used for storing values related to player XP levels.
class spellLevels:
	def __init__(self, spellLevel, spellXP):
		self.spellLevel = spellLevel
		self.spellXP = spellXP


# clas used for creating towns and vilages, might not use this though.
class town:
	def __init__(self, name, shop, center, building1, building2, building3):
		self.shop = shop
		self.name = name
		self.center = center
		self.building1 = building1
		self.building2 = building2
		self.building3 = building3
		
# setting up player's starter spell level. spell level 1 is required to let them use shield spell.
playerSpells = spellLevels(1, 0)


# menuloop controls while statements
menuLoop = 1

# controls who is attacking in a battle. 1 = player, 2 = wizard, 5 = player has died, 0 = battle has ended

battleTurn = 1



# enemy class, max health is used to compare against current health and determine percentage
class Enemy:
	def __init__(self, name, health, maxHealth, defence, atk, accuracy, spell1, spell2, spell3):
		self.name = name
		self.health = health
		self.maxHealth = maxHealth
		self.defence = defence
		self.atk = atk
		self.accuracy = accuracy
		self.spell1 = spell1
		self.spell2 = spell2
		self.spell3 = spell3

# class for body parts that will be shot.
class Target:
	def __init__(self, accuracy, damage):
		self.accuracy = accuracy
		self.damage = damage


#class for guns. makes accessing info about the gun easier
class Gun:
	def __init__(self, attack, ammo, maxAmmo, accuracy, sound):
		self.attack = attack
		self.ammo = ammo
		self.maxAmmo = maxAmmo
		self.accuracy = accuracy
		self.sound = sound

# menu update is specifically for menus where the user enters an option. 4 possible options, if you want an option removed just add a blank string in its place.

def menuUpdate(description, description2,  option1, option2, option3, option4):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(description)
	print(description2)
	print("___________________________________________________________________________________\n")
	print(option1, "     ", end=' ')
	print(option2, "     ", end=' ')
	print(option3, "     ", end=' ')
	print(option4, "\n \n")
	return input()


# viewing stats in battle.
def statcheck(stat):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(stat.name, "'s stats: \n")
	print("HEALTH = ", stat.health)
	print("DEFENCE = ", stat.defence)
	print("ATTACK = ", stat.atk)
	input()

#dialogue lines for enemies plus ability for enemies to speak function
hitLines = ["ARGH, I'll make you pay for that!", "OW! curse you!", "OW! What dark magic fuels that wretched thing??", "OWIE! Where the hell did you get that thing?", "OUCH, wait until the wizard king hears about this!"]
missLines = ["AHAHAHA! No amount of magic will fix your terrible aim!", "Imagine not being able to guide your shots using sorcery, loser!", "Even with that thing, you're no match for a wizard!", "No matter how hard you try, your resistance will be in vain.", "That thing is no match against our magic."]
def enemyMessage(message, name):
	if message == "hit":
		return (colorama.Fore.RED + name + colorama.Fore.WHITE + ": " + hitLines[random.randint(0, 4)] )
	elif message == "miss":
		return (colorama.Fore.RED + name + colorama.Fore.WHITE + ": " + missLines[random.randint(0, 4)])
	else:
		return (colorama.Fore.RED + name + colorama.Fore.WHITE + ": " + message)




# plays sound whe wizard gets hit
def enemyPain():
	randomSoundChooser = random.randint(1, 3)
	if randomSoundChooser == 1:
		return wizardcry1
	if randomSoundChooser == 2:
		return wizardcry2
	if randomSoundChooser == 3:
		return wizardcry3


# spell menu for casting spells
def spellMenu(description1, description2):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(description1)
	print(description2)
	print("___________________________________________________________________________________\n")
	if playerSpells.spellLevel >= 1:
		print("SHIELD: adds 10+ defence for one turn. \n")
	if playerSpells.spellLevel >= 2:
		print("GUIDED BULLETS: adds 10+ accuracy for one turn. \n")
	if playerSpells.spellLevel >= 3:
		print("FIREBALL: next turn's bullets are turned molten as they exit the barrel. each bullet that hits inflicts 5 fire damage for the next 3 turns. Cant be cast while already in effect.\n")
	if playerSpells.spellLevel >= 4:
		print("HEALING: gain 15 HP. \n")
	if playerSpells.spellLevel >= 5:
		print(colorama.Fore.BLUE + "STARS" + colorama.Fore.WHITE +  " AND " + colorama.Fore.RED + "STRIPES " + colorama.Fore.WHITE + "FINISHER: Finishing move that can be performed on opponents with less then 20 health. \n")
	return input()


#displays fancy message on screen. clears screen beforehand
def prompt(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	history.append(str + "\n")
	for word in str.split():
		time.sleep(0.05)
		mixer.Sound.play(type)
		print(f'{word:>1} ', end='')
		sys.stdout.flush()
	time.sleep(0.01)
	print("\n")
	promptContinue = input()
	if promptContinue.lower() == "history":
		historyPrint()
		input()
		os.system('cls' if os.name == 'nt' else 'clear')
		for word in str.split():
			time.sleep(0.05)
			print(f'{word:>1} ', end='')
			sys.stdout.flush()
		time.sleep(0.01)
		print("\n")
		promptContinue = input()
		return(promptContinue)
	elif promptContinue.lower() == "inventory":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("What do you want to look at? \n")
		print("Outfit          Items          Back")
		playerOption = input()
		if playerOption.lower() == "outfit":
			os.system('cls' if os.name == 'nt' else 'clear')
			print("You are wearing: ", end="")
			if playerOutfit == 0:
				print("Default outfit")
			elif playerOutfit == 1:
				print("Wizard outfit")
			print(playerOutfitsList[playerOutfit])
			input()
	else:
		return promptContinue



# Prompt code except slower for dramatic effect
def promptSlow(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	history.append(str + "\n")
	for word in str.split():
		time.sleep(0.4)
		mixer.Sound.play(type)
		print(f'{word:>1} ', end='')
		sys.stdout.flush()
	time.sleep(0.01)
	print("\n")
	promptContinue = input()
	if promptContinue.lower() == "history":
		historyPrint()
		input()
		os.system('cls' if os.name == 'nt' else 'clear')
		for word in str.split():
			time.sleep(0.05)
			print(f'{word:>1} ', end='')
			sys.stdout.flush()
		time.sleep(0.01)
		print("\n")
		promptContinue = input()
		return(promptContinue)
	elif promptContinue.lower() == "inventory":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("What do you want to look at? \n")
		print("Outfit          Items          Back")
		playerOption = input()
		if playerOption.lower() == "outfit":
			os.system('cls' if os.name == 'nt' else 'clear')
			print(playerOutfitsList[playerOutfit])
			input()
	


def oldPrompt(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(str)
	return input()


# history print function for use when player types 'history'
def historyPrint():
	for x in range(0,len(history)):
		print(history[x])


# function to start battles. ill be honest: this code sucks lmao. 
def fight(wizard1, menuLoopValue, message, music):
	
	#changing the wizard's name to appear red.
	wizard1.name = colorama.Fore.LIGHTRED_EX + wizard1.name + colorama.Fore.WHITE
	
	# resetting player ammo values.
	weapon.ammo = weapon.maxAmmo

	# miss turn was used to control when the wizard misses a turn due to being hit in the legs.
	missTurn = 0


	global playerHealth
	battleTurn = 1

	# my stupid ass forgot that i need to make menuLoop global for this to do anything. everything still works, this is just kinda pointless now.
	menuLoop = menuLoopValue

	# the playr can only cast one spell per turn. once they cast a spell this turns True, and they cant cast another spell until their turn is over.
	playerCastSpell = False

	# playerTempAccuracy is used to store default accuracy values during temporary accuracy stat buffs.
	playerTempAccuracy = 0

	# I forgot what this does lmfao i think it just stores what spell the player has chosen for some reason 
	# im so good at coding 
	playerSpellEffect = ""

	# keeps track of how many turns the fireball spell lasts for.
	playerFireballCount = 0

	# used for storing randomsied valused during the wizard's turn.
	wizardPercent = 0

	# same as playerTempAccuracy but for the wizard. dunno why it has a different name lol
	wizardAccuracyMemory = wizard1.accuracy
	global playerDefence

	# plays cool battle music to kill wizards to
	mixer.music.stop()
	mixer.music.load(music)
	mixer.music.play(-1,)

	# heres where things really go downhill
	# the battle ends once local menuLoop != menuLoopValue.
	while menuLoop == menuLoopValue:


		while wizard1.health > 0:


			# if battleTurn = 5 the player death sequence starts.
			if playerHealth <= 0:
				battleTurn = 5


			# the player's turn.
			while battleTurn == 1:
				
				# same as playerTempAccuracy but for defence.
				playerTempDefence = 0


				# setting PTA to standard player accuracy. same for wizard accuracy too.
				playerTempAccuracy = weapon.accuracy
				wizard1.accuracy = wizardAccuracyMemory
				wizardAccuracyMemory = wizard1.accuracy


				# prints menu for player to choose their option.
				# side note; make sure if you want to print an integer variable you convert it to a string first.
				playerOption = menuUpdate( message + "\n \nyour ammo:" + str(weapon.ammo) + " / " + str(weapon.maxAmmo),
										  "Your health: " + str(int(playerHealth)) + "\nEnemy health: " + str(int(wizard1.health)) + "\n \nChoose an action: (currently only fighting works. Wizard doesnt fight back yet.) ", "FIGHT",
										  "SPELLS", "EXTRA", "RUN AWAY")
				# funny little cheat code used to kill the player instantly. i made this to test what happens when you die easily.
				if playerOption == "kill yourself NOW":
					battleTurn = 5
					playerHealth = 0


				# if playerOption.lower() equals any valid option, the code beneath this will execute. otherwise the menu will just reprint itself and the player can choose again.
				if playerOption.lower() == "fight" or playerOption.lower() == "spells" or playerOption.lower() == "extra" or playerOption == "kill yourself NOW":
					

					# same deal as above except with areas the player can shoot. funny thing is, the player is told to type back to go back, but typing anything that isnt a body part works too.
					if playerOption.lower() == "fight":


						playerHit = menuUpdate("Where do you want to hit? \n accuracy = " + str(weapon.accuracy) + "/ 100", "Type 'back' to go back.", "head", "torso", "legs",
											   "arms")
						if playerHit.lower() == "head" or playerHit.lower() == "torso" or playerHit.lower() == "legs" or playerHit.lower() == "arms":



							# If the player has no ammo and tries to shoot they will miss a turn.
							if weapon.ammo == 0:
								prompt("No ammo! reloading skips your turn.")
								weapon.ammo = weapon.maxAmmo
								mixer.Sound.play(reloadSound)
								battleTurn = 2
							else:


								# i am an idiot. 
								# i made a unique chunk of code for what happens when you shot each limb, and not only that, a SECOND set of code for each limb purely for when you use
								# the assault rifle, which shoots 3 times. there is definitely ways i could have done this WAY better, and i am sorry you have to deal with this lmao

								# to save time ill only comment the first one since theyre all the same, and any that have unique pieces of code.
								if playerWeapon != "assault rifle":









									# if player shoots the head without an assault rifle
									if playerHit.lower() == "head":

										# two variables get randomised valus these will be used to caclulate wether or not a shot lands.
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)

										# if the hit percent is under its .accuracy counterpart, the hit has landed. playerHitPercent and bodyHitpercent need to be successful.
										if playerHitPercent < weapon.accuracy and bodyHitPercent < head.accuracy:
											mixer.Sound.play(enemyPain())

											# damage is calculated by adding the damage of the body part plus the attack stat of the weapon, and then minusing by the wizard's defence stat.
											wizard1.health = wizard1.health - ((head.damage + weapon.attack) - wizard1.defence)

											# printing out message that the wizard has been hit successfully.
											prompt("hit! enemy health: " + str(int(wizard1.health)) + " / " + str(wizard1.maxHealth))

											#printing randomly picked hit message from wizard.
											prompt(enemyMessage("hit", wizard1.name))

											# set's next turn to be the wizard's.
											battleTurn = 2

											# If the player used fireball, thats activated now.
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""

										# If the player missed, print out message informing player and then set turn to wizard's.
										else:
											prompt("miss! enemy health: " + str(int(wizard1.health)) + " / " + str(
												wizard1.maxHealth))
											prompt(enemyMessage("miss", wizard1.name))
											battleTurn = 2











									elif playerHit.lower() == "torso":

										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)

										weapon.ammo = weapon.ammo - 1

										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < torso.accuracy:
											mixer.Sound.play(enemyPain())

											wizard1.health = wizard1.health - ((torso.damage + weapon.attack) - wizard1.defence)

											prompt("hit! enemy health: " + str(int(wizard1.health)) + " / " + str(wizard1.maxHealth))

											battleTurn = 2

											prompt(enemyMessage("hit", wizard1.name))

											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""

										else:
											battleTurn = 2
											prompt("miss! enemy health: " + str(int(wizard1.health)) + " / " + str(wizard1.maxHealth))
											prompt(enemyMessage("miss", wizard1.name))
											










									elif playerHit.lower() == "legs": 

										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										
										mixer.Sound.play(weapon.sound)

										if playerHitPercent < weapon.accuracy and bodyHitPercent < legs.accuracy:

											mixer.Sound.play(enemyPain())

											wizard1.health = wizard1.health - ((legs.damage + weapon.attack) - wizard1.defence)
											prompt("hit! enemy misses turn! enemy health: " + str(int(wizard1.health)) + " / " + str(wizard1.maxHealth))
											
											#since hitting the legs makes the enemy miss a turn, battle turn is unaffected and instead missTurn = 1
											#this is probably a stupid way of doing this since battleTurn could just equal 1 but whatever
											missTurn = 1

											prompt(enemyMessage("hit", wizard1.name))
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""
											
										else:
											prompt("miss! enemy health: " + str(int(wizard1.health)) + " / " + str(
												wizard1.maxHealth))
											prompt(enemyMessage("miss", wizard1.name))
											missTurn = 0
											battleTurn = 2










									elif playerHit.lower() == "arms":

										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1

										mixer.Sound.play(weapon.sound)

										if playerHitPercent < weapon.accuracy and bodyHitPercent < arms.accuracy:

											mixer.Sound.play(enemyPain())

											wizard1.health = wizard1.health - ((arms.damage + weapon.attack) - wizard1.defence)

											prompt("hit! enemy accuracy decreased! enemy health: " + str(int(wizard1.health)) + " / " + str(wizard1.maxHealth))

											# wizard accuracy is decreased by 10 since the arms were hit.
											wizard1.accuracy = wizard1.accuracy - 10
											battleTurn = 2

											prompt(enemyMessage("hit", wizard1.name))
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""
										else:
											prompt("miss! enemy health: " + str(wizard1.health) + " / " + str(
												wizard1.maxHealth))
											battleTurn = 2
											prompt(enemyMessage("miss", wizard1.name))



								# This is where the assault rifle variation starts
								else:
									if playerHit.lower() == "head":

										# this line makes the code loop 3 times for each shot.
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < head.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - ((head.damage + weapon.attack) - wizard1.defence)
												prompt("hit! enemy health: " + str(int(wizard1.health)) + " / " + str(
													wizard1.maxHealth))
												battleTurn = 2
												prompt(enemyMessage("hit", wizard1.name))
												if playerSpellEffect == "fireball":
													playerFireballCount = 3
													playerSpellEffect = ""
											else:
												prompt("miss! enemy health: " + str(int(wizard1.health)) + " / " + str(
													wizard1.maxHealth))
												battleTurn = 2
												prompt(enemyMessage("miss", wizard1.name))









									elif playerHit.lower() == "torso":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < torso.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - ((torso.damage + weapon.attack) - wizard1.defence)
												prompt("hit! enemy health: " + str(int(wizard1.health)) + " / " + str(
													wizard1.maxHealth))
												battleTurn = 2
												prompt(enemyMessage("hit", wizard1.name))
												if playerSpellEffect == "fireball":
													playerFireballCount = 3
													playerSpellEffect = ""
											else:
												prompt("miss! enemy health: " + str(int(wizard1.health)) + " / " + str(
													wizard1.maxHealth))
												battleTurn = 2
												prompt(enemyMessage("miss", wizard1.name))










									elif playerHit.lower() == "legs":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < legs.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - ((legs.damage + weapon.attack) - wizard1.defence)
												prompt("hit! enemy misses turn! enemy health: " + str(int(wizard1.health)) + " / " + str(wizard1.maxHealth))
												missTurn = 1
												prompt(enemyMessage("hit", wizard1.name))
												if playerSpellEffect == "fireball":
													playerFireballCount = 3
													playerSpellEffect = ""
											else:
												prompt("miss! enemy health: " + str(int(wizard1.health)) + " / " + str(
													wizard1.maxHealth))
												prompt(enemyMessage("miss", wizard1.name))
												battleTurn = 2
												missTurn = 0










									elif playerHit.lower() == "arms":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < arms.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - ((arms.damage + weapon.attack) - wizard1.defence)
												prompt("hit! enemy accuracy decreased! enemy health: " + str(
													int(wizard1.health)) + " / " + str(wizard1.maxHealth))
												
												wizard1.accuracy = wizard1.accuracy - 10
												battleTurn = 2
												prompt(enemyMessage("hit", wizard1.name))
												if playerSpellEffect == "fireball":
													playerFireballCount = 3
													playerSpellEffect = ""
											else:
												prompt("miss! enemy health: " + str(wizard1.health) + " / " + str(
													wizard1.maxHealth))
												battleTurn = 2
												prompt(enemyMessage("miss", wizard1.name))



								
						# error handling
						elif playerHit == "back":
							battleTurn = 1
						else:
							prompt("invalid selection!")

					# if the player chooses to cast a spell this code executes.
					elif playerOption.lower() == "spells":

						# in case the player levels up, this code activates. 
						if playerSpells.spellXP > 100:
							prompt("You leveled up in spell level!")
							playerSpells.spellLevel += 1
							playerSpells.spellXP -= 100

						# prints menu for player to choose spells.
						playerOption  = spellMenu("Choose a spell. More spells become available to you the higher level you are.", "You can only use one spell per turn. using spells will not end your turn.\n Type 'back' to go back.")
						if playerOption.lower() == "back":
							battleTurn = 1

						# when a spell is picked, playerCastSpell = true
						# if playerCastSpell = true then the player cant casts any more spells
						if playerCastSpell == True:
							prompt("You already cast a spell this turn!")

							# if playerSpells.spellLevel is less then one the player cant choose shield. this continues for every spell is the level requirement being raised by one
						if playerOption.lower() == "shield" and playerCastSpell == False and playerSpells.spellLevel >= 1:
							playerCastSpell = True
							playerTempDefence = playerDefence
							playerDefence += 10
							prompt("You cast shield! Your defence is increased by 10 for this turn.")
							playerSpells.spellXP += 30


						if playerOption.lower() == "guided bullets" and playerCastSpell == False and playerSpells.spellLevel >= 2:
							playerCastSpell = True
							playerTempAccuracy = weapon.accuracy
							weapon.accuracy += 10
							prompt("You cast guided bullets! Your accuracy is increased by 10 for this turn.")
							playerSpells.spellXP += 30


						if playerOption.lower() == "fireball" and playerCastSpell == False and playerSpells.spellLevel >= 3 and playerFireballCount <= 0:
							playerCastSpell = True
							playerSpellEffect = "fireball"
							prompt("You cast fireball! Your bullets fired this turn inflict fire damage that lasts for 3 turns.")
							playerSpells.spellXP += 30
						if playerOption.lower == "fireball" and playerFireballCount > 0:
							prompt("Fireball is already in effect!")


						if playerOption.lower() == "healing" and playerCastSpell == False and playerSpells.spellLevel >= 4:
							playerCastSpell = True
							prompt("You cast healing! You gained 15 health.")
							playerHealth += 15
							if playerHealth > 100:
								playerHealth = 100
							playerSpells.spellXP += 30

						# SAS finisher has a special condition that your opponent must be less then 20 health in order to cast it.
						# once cast the SAS finisher ends the battle.
						if playerOption.lower() == "stars and stripes finisher" and playerCastSpell == False and playerSpells.spellLevel >= 5 and wizard1.health < 20000:
							playerCastSpell = True
							prompt("You cast the stars and stripes finisher.")
							mixer.music.fadeout(2000)
							time.sleep(2)
							mixer.music.load("assets/thelandofthefree.mp3")
							mixer.music.set_volume(1)
							mixer.music.play()
							prompt("Your look down at your wand. its flashing " + colorama.Fore.RED + "red, " + colorama.Fore.WHITE + "white, and " + colorama.Fore.BLUE + "blue." + colorama.Fore.WHITE)
							prompt("You can feel the pure patriotism in your veins, pulsing from the wand.")
							mixer.Sound.play(eagle)
							prompt("In the distance, you hear the mighty Bald Eagle, a symbol of American freedom.")
							prompt("You raise your wand into the air, calling out.")
							prompt(playerName + ": UNCLE SAM! DESTROY MY ENEMIES, AND MY OIL IS YOURS!")
							prompt("Suddenly, your opponent cries out in pain as he gets 13 slashes across his neck, one for each stripe on the American flag.")
							prompt(enemyMessage("W-WHAT?? WHAT SPELL IS THAT, I'VE NEVER SEEN IT!", wizard1.name,))
							prompt("From the sky, 50 stars start to descend from the heavens.")
							prompt(playerName + ": Taste the might of PURE, UNFILTERED FREEDOM.")
							prompt("The stars land on the enemy. They explode in a blinding flash of white, leaving just a crater.")
							mixer.music.fadout(5000)
							wizard1.health = 0
							playerSpells.spellXP += 30
					elif playerOption.lower() == "extra":
						playerOption = menuUpdate("Do you want to view info or items?", "type 'back' to go back.", "Info", "			", "			", "Items" )
						if playerOption.lower() == "info":
							prompt("Enemy defence: " + str(wizard1.defence) + "\n Enemy accuracy: " + str(wizard1.accuracy) + "\n Enemy health: " + str(wizard1.health))
							prompt("Your defence: " + str(playerDefence) + "\n Your accuracy: " + str(weapon.accuracy) + "\n Your health: " + str(playerHealth))
					else:
						prompt("invalid selection!")
			while battleTurn == 5:
				os.system('cls' if os.name == 'nt' else 'clear')
				mixer.music.fadeout(3000)
				mixer.music.load("assets/confrontation.mp3")
				mixer.music.play()
				prompt("You have died.")
				promptSlow(colorama.Fore.RED + "YOU HAVE FAILED ME." + colorama.Fore.WHITE)
				promptSlow(colorama.Fore.RED + "YOU HAVE FAILED YOUR COUNTRY." + colorama.Fore.WHITE)
				os.system('cls' if os.name == 'nt' else 'clear')
				time.sleep(3)
				promptSlow(colorama.Fore.RED + "GOODBYE." + colorama.Fore.WHITE)
				sys.quit()
			if playerFireballCount > 0:
				wizard1.health -= 5
				playerFireballCount -= 1
				prompt("Your enemy takes fire damage! -5 hp!")
			if missTurn == 0:
				battleTurn = 2
			else:
				battleTurn = 1
				missTurn = 0
				playerCastSpell = False
			if wizard1.health <= 0:
				playerCastSpell = False
				prompt("Congratulations, you win!")
				battleTurn = 0
				menuLoop = menuLoopValue + 1
			else:
				while battleTurn == 2:
					playerCastSpell = False
					playerSpellEffect = ""
					weapon.accuracy = playerTempAccuracy
					
					if wizard1.health <= 70:
						wizardPercent = random.randint(0,100)
						if wizardPercent > 50:
							prompt("Wizard casts healing!")
							wizard1.health += 10
							if wizard1.health > 100:
								wizard1.health = 100
							prompt("Enemy health: " + str(wizard1.health))
					os.system('cls' if os.name == 'nt' else 'clear')
					waiter = random.randint(1,4)
						
					while waiter > 0:
						print("The enemy chooses their attack")
						time.sleep(0.20)
						os.system('cls' if os.name == 'nt' else 'clear')
						print("The enemy chooses their attack.")
						time.sleep(0.20)
						os.system('cls' if os.name == 'nt' else 'clear')
						print("The enemy chooses their attack..")
						time.sleep(0.20)
						os.system('cls' if os.name == 'nt' else 'clear')
						print("The enemy chooses their attack...")
						time.sleep(0.50)
						os.system('cls' if os.name == 'nt' else 'clear')
						waiter -= 1
						wizardAttack = ""

					if wizard1.spell1 == "fireball":
						if random.randint(0,100) < (wizard1.accuracy + 10):
							wizardAttack = "fireball"
							playerHealth = playerHealth - (wizard1.atk + random.randint(0,15) - (playerDefence / 2))
							prompt("Wizard casts fireball! Your health:" + str(playerHealth))
							battleTurn = 1
					if wizardAttack == "" and wizard1.spell2 == "windgust":
						if random.randint(0,100) < (wizard1.accuracy - 40):
							wizardAttack = "windgust"
							playerHealth = playerHealth - (wizard1.atk + random.randint(0,5) - (playerDefence / 2))
							prompt("Wizard casts wind gust! Your health:" + str(playerHealth))
							prompt("The wind gust blew you over, and ou lost your footing. You miss a turn!")
							battleTurn = 2
					if wizardAttack == "" and wizard1.spell3 == "spiritaid":
						if random.randint(0,100) < (wizard1.accuracy - 15):
							wizardAttack = "spiritaid"
							prompt("Wizard casts spirit aid! Enemy defence increases by 10!")
							wizard1.defence += 10
							battleTurn = 1
					if wizardAttack == "":
						wizardAttack = "lightning"
						playerHealth = playerHealth - (wizard1.atk - (playerDefence / 2))
						prompt("Wizard casts lightning! Your health:" + str(playerHealth))
						battleTurn = 1
					playerDefence = playerTempDefence

testenemy = Enemy("testwizard", 100, 100, 10, 15, 70, "fireball", "windgust", "spiritaid")
head = Target(50, 60,) #35
torso = Target(90, 15) #50
legs = Target(60, 20) #45
arms = Target(75, 20)#45

devcode = prompt("enter devcode")
if devcode == "spells":
	playerSpells.spellLevel = 5
	prompt("devcode recieved")



prompt("WELCOME TO WARLOCK WITH A GLOCK, BY FEDBEAN INTERACTIVE")

prompt("YOUR JOURNEY IS ABOUT TO BEGIN.")
playerName = prompt("BUT FIRST, WHAT IS YOUR NAME? TYPE IT BELOW.")
playerName = playerName
playerOption = prompt("IS " + playerName + " YOUR NAME? YES OR NO")
while playerOption != "yes":
    playerName = prompt("REENTER YOUR NAME BELOW.")
    playerOption = prompt("IS " + playerName + " YOUR NAME? YES OR NO")
prompt(playerName + " IS YOUR NAME.")
prompt("Your story is about to begin.")
os.system('cls' if os.name == 'nt' else 'clear')


npcName = (colorama.Fore.YELLOW + colorama.Back.BLUE + "Walmart Employee" + colorama.Fore.WHITE + colorama.Back.RESET)
playerName = (colorama.Fore.LIGHTBLUE_EX + playerName + colorama.Fore.WHITE)


prompt("You are a true " + colorama.Fore.BLUE + "A" + colorama.Fore.WHITE + "M" + colorama.Fore.RED + "E" + colorama.Fore.BLUE + "R" + colorama.Fore.WHITE + "I" + colorama.Fore.RED + "C" + colorama.Fore.BLUE + "A" + colorama.Fore.WHITE + "N"  + " patriot. Recently, whilst hunting for oil, your gun broke. This was devastating, but not to worry! Your local Walmart sells firearms.")
prompt("You run as fast as you can to your gigantic pick-up truck, decorated with stickers of the American flag and a picture of a bald eagle laying a grenade like its an egg.")
prompt("You can't waste a single second. After all, what will you do if 4 ruffians break into your home to steal your oil?")
prompt("After a 15 minute drive and multiple run-over pedestrians, you finally reach the beautifiul Walmart. You step out of your truck and walk into the Walmart.")
mixer.Sound.play(walmart, -1, 0, 2000,)
mixer.Sound.set_volume(walmart, 0.5)
prompt("Dozens of aisles line your view, each filled with the typical items and people you'd expect to find in a Walmart. In one, a 400 pound beast in a mobility scooter is stuffing a seventeenth bag of cheetos into their poor shopping cart.")
prompt("In another aisle, you see a Karen screaming at an employee because the 10 year old expired coupon they have isnt valid.")
prompt("All of it, it reminds you that you are in the land of the Free. \n America.")
prompt(npcName + ": 'Welcome to Walmart, how can I help you today?'")
prompt(playerName + ": 'Hey, do you know what aisle has guns?'")
prompt(npcName + ": 'Certainly! come with me to aisle 27.'")
prompt("The " + npcName + " leads you to aisle 27. There on the wall are dozens of guns lined up on display. You thank the " + npcName + " and begin browsing. After a while, you've narrowed down what you want to just 4 options.")

playerOption = " "
playerWeapon = " "
while menuLoop == 1:
	playerWeapon = menuUpdate("Pick your weapon.", "weapons have different stats. this choice is irreversible. type your desired weapon.", "pistol", "revolver", "assault rifle", "shotgun")
	if playerWeapon.lower() == "pistol" or playerWeapon.lower() == "revolver" or playerWeapon.lower() == "assault rifle" or playerWeapon.lower() == "shotgun":
		if playerWeapon.lower() == "pistol":
			playerOption = str(menuUpdate("The" + colorama.Fore.LIGHTRED_EX + " pistol " + colorama.Fore.WHITE + "can hold 12 bullets, deals 10 dmg when shot, shoots once per turn, and has a 70% accuracy. do you want it?", "      ,_________\n     Y II_____==|\n     )  /J\n    /__/", "yes", " ", " ", "no"))
			if playerOption.lower() == "yes":
				playerWeapon = "pistol"
				weapon = Gun(10, 12, 12, 80, pistolSound)
				menuLoop = 2
		elif playerWeapon.lower() == "revolver":
			playerOption = str(menuUpdate("The" + colorama.Fore.LIGHTRED_EX + " revolver " + colorama.Fore.WHITE + "can hold 6 bullets, deals 20 dmg when shot, shoots once per turn, and has a 70% accuracy. do you want it?", "      __ _______,\n    _Y__]-------'\n   / _/J\n  |_|\n", "yes", " ", " ", "no"))
			if playerOption.lower() == "yes":
				playerWeapon = "revolver"
				weapon = Gun(20, 6, 6, 80, revolverSound)
				menuLoop = 2
		elif playerWeapon.lower() == "assault rifle":
			playerOption = str(menuUpdate("The" + colorama.Fore.LIGHTRED_EX + " assault rifle " + colorama.Fore.WHITE + "can hold 30 bullets, deals 15 dmg when shot, shoots thrice per turn, and has a 40% accuracy. do you want it?", "                 ___\n                [_-_]\n      _________,-'-'--_______/|\n     |       _     ___|_.......-------=\n     |__...'' / /J|  |\n             /_/   \\__\\", "yes", " ", " ", "no"))
			if playerOption.lower() == "yes":
				playerWeapon = "assault rifle"
				weapon = Gun(5, 30, 30, 70, assaultRifleSound)
				menuLoop = 2
		elif playerWeapon.lower() == "shotgun":
			playerOption = str(menuUpdate("The" + colorama.Fore.LIGHTRED_EX + " shotgun " + colorama.Fore.WHITE + "can hold 2 rounds, deals 35 dmg when shot, shoots once per turn, and has a 50% accuracy. do you want it?", "                      _,______________________________,\n       _______..... Y.____|___|______________________|\n      |             _____.......------'\n      |        ..'''   J\n      |___...''\n", "yes", " ", " ", "no"))
			if playerOption.lower() == "yes":
				playerWeapon = "shotgun"
				weapon = Gun(30, 2, 2, 60, shotgunSound)
				menuLoop = 2
	else:
		prompt("that was not a valid selection!")
		menuLoop = 1





prompt("you have picked the " + playerWeapon + ".")
prompt(playerName + ": This is quite the fine weapon if I do say so myself!")
prompt("You pull it off the wall and admire it.")
prompt("You head to the checkout, purchase the gun, and get back in your truck.")
os.system('cls' if os.name == 'nt' else 'clear')
mixer.Sound.fadeout(walmart, 2000)
mixer.music.fadeout(2000)
time.sleep(2)
prompt("Why not visit the shooting range and give your gun a try?")
prompt("You drive to the shooting range and go inside.")
dummy = Enemy("Practice Dummy", 50, 50, 0, 0, 0, "", "", "")
missTurn = 0
menuLoop = 1
battleTurn = 1
mixer.music.fadeout(2000)
time.sleep(2)
mixer.music.load("assets/battle1.mp3")
mixer.music.play(-1,)
while menuLoop == 1:
	while battleTurn == 1:
			playerOption = menuUpdate( "The practice dummy stands before you." + "\n \nyour ammo:" + str(weapon.ammo) + " / " + str(weapon.maxAmmo),
									  "Your health: " + str(playerHealth) + "\nEnemy health: " + str(dummy.health) + "\n \nThis is a battle. During your turn in a battle, you get various options.\nFighting ends your turn and attacks your enemy.\nThe extra menu lets you use items and view information about your opponent. It does not use your turn up.\nRunning away gives you a chance to escape dangerous situations. If you fail when attempting to run away, the battle continues and you miss a turn. \nChoose your action:", "FIGHT",
									  "EXTRA", "RUN AWAY", "")
			if playerOption.lower() == "fight" or playerOption.lower() == "extra":
				if playerOption.lower() == "fight":
					playerHit = menuUpdate("Where do you want to hit? \nDifferent areas have different chances to be hit, as well as dealing different amounts of damage.\nHitting the arms lowers you enemy's accuracy, and hitting their leg causes them to miss a turn. \n accuracy = " + str(weapon.accuracy) + "/ 100", "Type 'back' to go back.", "head", "torso", "legs",
										   "arms")
					if playerHit.lower() == "head" or playerHit.lower() == "torso" or playerHit.lower() == "legs" or playerHit.lower() == "arms":
						if weapon.ammo == 0:
							prompt("No ammo! reloading skips your turn.")
							weapon.ammo = weapon.maxAmmo
							mixer.Sound.play(reloadSound)
							battleTurn = 2
						else:
							if playerWeapon != "assault rifle":
								if playerHit.lower() == "head":
									playerHitPercent = random.randint(1, 100)
									bodyHitPercent = random.randint(1, 100)
									weapon.ammo = weapon.ammo - 1
									mixer.Sound.play(weapon.sound)
									if playerHitPercent < weapon.accuracy and bodyHitPercent < head.accuracy:
										
										dummy.health = dummy.health - (head.damage + (
													(1 - dummy.defence) * weapon.attack))
										prompt("hit! enemy health: " + str(dummy.health) + " / " + str(
											dummy.maxHealth))
										
										battleTurn = 2
										
									else:
										prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
											dummy.maxHealth))
										
										battleTurn = 2
								elif playerHit.lower() == "torso":
									playerHitPercent = random.randint(1, 100)
									bodyHitPercent = random.randint(1, 100)
									weapon.ammo = weapon.ammo - 1
									mixer.Sound.play(weapon.sound)
									if playerHitPercent < weapon.accuracy and bodyHitPercent < torso.accuracy:
										
										dummy.health = dummy.health - (torso.damage + (
													(1 - dummy.defence) * weapon.attack))
										prompt("hit! enemy health: " + str(dummy.health) + " / " + str(
											dummy.maxHealth))
										battleTurn = 2
										
									else:
										battleTurn = 2
										prompt("miss! enemy health: " + str(dummy.health) + " / " + str(dummy.maxHealth))
										
										
								elif playerHit.lower() == "legs": 
									playerHitPercent = random.randint(1, 100)
									bodyHitPercent = random.randint(1, 100)
									weapon.ammo = weapon.ammo - 1
									mixer.Sound.play(weapon.sound)
									if playerHitPercent < weapon.accuracy and bodyHitPercent < legs.accuracy:
										
										dummy.health = dummy.health - (legs.damage + (
													(1 - dummy.defence) * weapon.attack))
										prompt("hit! enemy misses turn! enemy health: " + str(
											dummy.health) + " / " + str(dummy.maxHealth))
										missTurn = 1
										
									else:
										prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
											dummy.maxHealth))
										
										battleTurn = 2
								elif playerHit.lower() == "arms":
									playerHitPercent = random.randint(1, 100)
									bodyHitPercent = random.randint(1, 100)
									weapon.ammo = weapon.ammo - 1
									mixer.Sound.play(weapon.sound)
									if playerHitPercent < weapon.accuracy and bodyHitPercent < arms.accuracy:
										
										dummy.health = dummy.health - (arms.damage + (
													(1 - dummy.defence) * weapon.attack))
										prompt("hit! enemy accuracy decreased! enemy health: " + str(
											dummy.health) + " / " + str(dummy.maxHealth))
										dummy.accuracy = dummy.accuracy - 10
										battleTurn = 2
										
									else:
										prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
											dummy.maxHealth))
										battleTurn = 2
										
							else:
								if playerHit.lower() == "head":
									for x in range(0, 3):
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < head.accuracy:
											dummy.health = dummy.health - (head.damage + ((1 - dummy.defence) * weapon.attack))
											prompt("hit! enemy health: " + str(dummy.health) + " / " + str(
												dummy.maxHealth))
											battleTurn = 2
											
											
										else:
											prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
												dummy.maxHealth))
											battleTurn = 2
											
								elif playerHit.lower() == "torso":
									for x in range(0, 3):
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < torso.accuracy:
											
											dummy.health = dummy.health - (torso.damage + (
														(1 - dummy.defence) * weapon.attack))
											prompt("hit! enemy health: " + str(dummy.health) + " / " + str(
												dummy.maxHealth))
											battleTurn = 2
											
											
										else:
											prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
												dummy.maxHealth))
											battleTurn = 2
											
								elif playerHit.lower() == "legs":
									for x in range(0, 3):
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < legs.accuracy:
											
											dummy.health = dummy.health - (legs.damage + ((1 - dummy.defence) * weapon.attack))
											prompt("hit! enemy misses turn! enemy health: " + str(
												dummy.health) + " / " + str(dummy.maxHealth))
											missTurn = 1
											
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""
										else:
											prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
												dummy.maxHealth))
											
								elif playerHit.lower() == "arms":
									for x in range(0, 3):
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < arms.accuracy:
											
											dummy.health = dummy.health - (arms.damage + (
														(1 - dummy.defence) * weapon.attack))
											prompt("hit! enemy accuracy decreased! enemy health: " + str(
												dummy.health) + " / " + str(dummy.maxHealth))
											dummy.accuracy = dummy.accuracy - 10
											battleTurn = 2
											
										else:
											prompt("miss! enemy health: " + str(dummy.health) + " / " + str(
												dummy.maxHealth))
											battleTurn = 2			
						# else:
					elif playerHit == "back":
						battleTurn = 1
					else:
						prompt("invalid selection!")
				
				elif playerOption.lower() == "extra":
					playerOption = menuUpdate("Do you want to view info or items?", "type 'back' to go back.", "Info", "			", "			", "Items" )
					if playerOption.lower() == "info":
						os.system('cls' if os.name == 'nt' else 'clear')
						print("Enemy defence: " + str(dummy.defence) + "\n Enemy accuracy: " + str(dummy.accuracy) + "\n Enemy health: " + str(dummy.health))
						input()
						print("Your defence: " + str(playerDefence) + "\n Your accuracy: " + str(weapon.accuracy) + "\n Your health: " + str(playerHealth))
						input()
					if playerOption.lower() == "items":
						prompt("You have no items!")
				
	if missTurn == 0:
		battleTurn = 2
	else:
		battleTurn = 1
		missTurn = 0
	if dummy.health <= 0:
		prompt("the dummy has been destroyed.")
		battleTurn = 0
		mixer.music.fadeout(2000)
		menuLoop = 2
	else:
		while battleTurn == 2:
			playerDefence = playerTempDefence
			prompt("the dummy stares at you.")
			battleTurn = 1




prompt(playerName + ": 'Hell yeah, this thing awesome!'")
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(3)
prompt("Suddenly, you hear a noise.")
mixer.Sound.play(portal1)
prompt(playerName + ": Huh??")
prompt("A sort of... puddle has formed on the floor suddenly. It wasn't there before.")
prompt("You lean over it to get a better look, still clutching the gun in your hands. The puddle is a bright shade of blue and has a sort of swirling pattern to it.")
prompt("You go to touch it, but you accidentally drop your gun! As you attempted to grab it, you fell onto the puddle.")
prompt("You didn't hit the floor though. You fell through it!")
os.system('cls' if os.name == 'nt' else 'clear')
mixer.Sound.play(portal2) 
time.sleep(8)
mixer.music.load("assets/unnerve.mp3")
mixer.music.play(-1, 0, 2000)
prompt(enemyMessage("'Where did you send the damn portal to?'", "???? 1"))
prompt(enemyMessage("'Hang on, I'll check the spellbook again...'", "???? 2"))
time.sleep(2)
prompt(enemyMessage("'It says... someplace called Earth... do you happen to know where that is?'", "???? 2"))
time.sleep(1)
mixer.Sound.play(portal1)
prompt(playerName + ": AAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH")
prompt("You fall out of the hole, and land on a floor made of wood.")
prompt("Looking around, you can see desks covered in strange objects made of glass, and filled with colourful liquid.")
prompt("Directly in front of you there are two strange looking men. They each have long beards, robes, and weird jagged hats. One of them is holding a book.")
prompt("These must be wizards!")
prompt(enemyMessage("'Who are you? What are you doing here?'", "Wizard 1"))
prompt("The wizards seem both mad and confused.")
prompt(playerName + ": Well, my name is " + playerName + ", and I come from the glorious United States of America, a land of freedom and prosperity.")
mixer.Sound.play(eagle)
time.sleep(2)
prompt("The wizards turn around and begin whispering to eachother.")
prompt(enemyMessage("'I think this is just a filthy commoner from where they're from, what should we do?'", "Wizard 2"))
prompt(enemyMessage("'Lets just kill him, is not like anyones going to care that a commoner is gone. Besides, we can't let outsiders know this world exists.'", "Wizard 1"))
prompt("The wizards turn back towards you.")
prompt(enemyMessage("'We have come to a decision. You are to be disposed of so that you cannot speak of what you have seen here.'", "Wizard 1"))
mixer.music.play(-1)
prompt(playerName + ": 'Disposed of? You mean you're killing me? I didn't even do anything!'")
prompt("The wizards both raise their wands to you and begin chanting something in an unknown language.")
prompt("You begin to panic, but you suddenly remember. You still have that gun!")
prompt("You pick the gun up off the floor, and right before theyre able to finish their chanting...")
mixer.Sound.play(weapon.sound)
time.sleep(0.5)
mixer.Sound.play(weapon.sound)
time.sleep(1.5)
prompt("Both wizards were shot in the head and died before they could finish their spell.")
prompt(playerName + ": That was close... God bless the second amendment.")
prompt("You walk over to the two wizard corpses.")
prompt(playerName + ": I wonder if these wands actually do anything...")
prompt("You walk over to one of the wizards and pick up his wand.")
prompt("The second you pick up the wand, a strange feeling flows through your veins.")
prompt("Your vision goes dark, And you fall over as the feeling grows stronger.")
os.system('cls' if os.name == 'nt' else 'clear')
mixer.music.fadeout(3000)
time.sleep(3)
mixer.music.load("assets/confrontation.mp3")
mixer.music.play(-1)
prompt('Out of nowhere, you hear someone speak to you. Their voice is deafeningly loud.')
promptSlow(colorama.Fore.RED + "I WANT YOU." + colorama.Fore.WHITE)
prompt(playerName + ": 'Huh?? Who's there?'")
prompt(colorama.Fore.RED + "I WANT YOU TO GO FORTH AND SPREAD FREEDOM." + colorama.Fore.WHITE)
prompt(playerName + ": 'Seriously, who the hell are you?")
prompt(colorama.Fore.RED + "IN TIME I WILL REVEAL MYSELF TO YOU." + colorama.Fore.WHITE)
prompt(colorama.Fore.RED + "COMPLETE YOUR MISSION AND I WILL REWARD YOU." + colorama.Fore.WHITE)
prompt(playerName + ": No way, you don't even want to tell me your name, why should i help you?")
prompt(colorama.Fore.RED + "YOU MUST." + colorama.Fore.WHITE)
prompt(colorama.Fore.RED + "FOR YOUR COUNTRY." + colorama.Fore.WHITE)

menuLoop = 0
voices = ["YOU MUST DO IT.", "YOU HAVE BEEN COMMANDED.", "YOUR COUNTRY NEEDS YOU.", "SPREAD FREEDOM ACROSS THIS LAND.", "YOU WILL DESTROY THEM ALL.", "YOU ARE DESTINED FOR GREATNESS.", "AMERICA WILL RISE.", "AMERICA WAS DESTINED TO RULE.", "YOU ARE DESTINED TO RULE.", "ALL WHO OPPOSE US WILL FALL.", "THIS TASK IS MORE IMPORTANT THEN YOU."]
while menuLoop < 100:
	print(colorama.Fore.RED, end="")
	print(voices[random.randint(0, 9)])
	mixer.Sound.play(type)
	time.sleep(0.07)
	os.system('cls' if os.name == 'nt' else 'clear')
	time.sleep(0.03)
	menuLoop += 1
	print(colorama.Fore.WHITE, end="")


prompt(playerName + ": 'ALRIGHT FINE I'LL DO IT!'")
prompt(colorama.Fore.RED + "GOOD. DO THIS FOR ME AND I WILL GRANT YOU POWER." + colorama.Fore.WHITE)
prompt(colorama.Fore.RED + "USE THIS WAND TO CAST SPELLS. I HAVE ENGRAVED THE TECHNIQUE INTO YOUR MIND." + colorama.Fore.WHITE)
prompt(colorama.Fore.RED + "THERE IS SOMEBODY COMING. USE THIS NEW POWER TO ELIMINATE THEM." + colorama.Fore.WHITE)
mixer.music.fadeout(5000)
prompt("All of a sudden, the voices stop. your vision is normal, and you feel fine.")
prompt(playerName + ": ...")
prompt(playerName + ": What the hell was that???")
prompt(playerName + ": What did that voice even want me to do?????")
prompt("Suddenly, you notice the faint sound of footsteps approaching.")

prompt(playerName + ": Oh crap, That must be who the voice was talking about!")
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)

prompt(enemyMessage("'Whats all the ruckus in here, I'm trying to brew a potion of enlargeme-'", "Wizard 3"))
prompt(enemyMessage("'What the- What the hell have you done?? Who are you?'", "Wizard 3"))
prompt(playerName + ": I-I killed them, and I'll kill you too if you don't leave!")
prompt(enemyMessage("'Nonsense! I'm not leaving after what I just witnessed. You're going to die where you are standing.'", "Wizard 3"))

wizard3 = Enemy("Wizard", 100, 100, 10, 15, 70, "fireball", "windgust", "spiritaid")
fight(wizard3, 1, "The wizard approaches!", "assets/battle1.mp3")

prompt(playerName + ": Phew... I hope hes the last one...")
prompt(playerName + ": Lets see what he had on him...")
prompt("You search through his pockets and find a map inside one of them.")
os.system('cls' if os.name == 'nt' else 'clear')
print(map)
input()

prompt("You decide to search the room for anything useful. In a closet, you find some fancy wizard clothes.")
playerOption = input("Wear the wizard clothes? Yes or no")
if playerOption.lower() == "yes":
	prompt(playerName + ": Well... they may have tried to kill me, but they have good taste in fashion.")
	playerOutfit = 1
	prompt("You take the wizard clothes and put them on. Theyre quite comfortable!")
else:
	prompt("You decided not to wear the wizard clothes.")
	playerOutfit = 0
prompt(playerName + ": Those wizards mentioned something about a portal, I guess thats what I fell through.")
prompt(playerName + ": If its a portal that brought me here, I'll probably need a portal to take me back.")
prompt(playerName + ": Unfortunately, I don't know how to make one.")

prompt(playerName + ": I should ask around and see if I can get one.")
prompt("You walk outside and see that you're near a coast.")
prompt("In the distance, you see a small collection of buildings by the ocean, it must be a village.")
playerOption = prompt("Do you want to visit the town? yes or no")
if playerOption == "yes":
	prompt("You began to make your way towards the town")
	os.system('cls' if os.name == 'nt' else 'clear')
	time.sleep(2)
	prompt("On your way towards the town, you are approached by another wizard.")
	prompt(enemyMessage("You, you there!", "Wizard"))
	playerOption = prompt("It seems he is trying to get your attention. Do you talk to him? yes or no")
	if playerOption.lower() == "yes":
		prompt(enemyMessage("You there, come over here!", "Wizard"))
		prompt("You cautiously walk towards the wizard, stopping about 3 metres away.")
		prompt(playerName + ": hey, uh, can I help you with anything?")
		if playerOutfit == 1:
			prompt(enemyMessage("You, you're a wizard, correct?"))
			prompt(playerName + ": uhhhhhhh, yeah, yeah I am a wizard, why do you ask?")
		else:
			prompt(enemyMessage("Traveller, I have a deal I wish to make with you."))
		prompt(enemyMessage("My name is Galdon, and I enjoy challenging people to my games.", "Galdon"))
		prompt(playerName + ": Games, huh? What kind of games?")
		prompt(enemyMessage("A game of wits! All you need to do is answer my question, and if you're right, you win!", "Galdon"))
		prompt(playerName + ": And what do I get for winning?")
		prompt(enemyMessage("If you manage to beat my game, I shall reward you with 15 gold coins.", "Galdon"))
		playerOption = prompt("Do you want to participate in Galdon's game? yes or no")
		if playerOption.lower() == "yes":
			prompt(playerName + ": alright then, I'll play.")
			prompt(enemyMessage("Woohoo! Alright then, lets play. My question is:", "Galdon"))
			prompt(enemyMessage("I bring light to the night, both bright and grand.", "Galdon"))
			prompt(enemyMessage("My life is brief, but my beauty stands.", "Galdon"))
			prompt(enemyMessage("In celebrations or quiet, I take my place.", "Galdon"))
			prompt(enemyMessage("What am I, that brightens the darkest place?", "Galdon"))
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Pick an answer: ")
			print("Lantern \nCandle\n4th of July fireworks")
			playerOption = input()
			prompt(playerName + ": The answer is... {playerOption}!")
			if playerOption.lower() == "candle":
				prompt(enemyMessage("Yes, you got it right!", "Galdon"))
				prompt(enemyMessage("Congratulations, Here's your prize!", "Galdon"))
				prompt("Galdon gave you 15 gold coins.")
				prompt(playerName + ": Wow, thanks!")
				playerMoney += 15
			if playerOption.lower() == "4th of july fireworks":
				prompt(enemyMessage("What- no, what the hell even is that? its a candle you idiot!", "Galdon"))
			else:
				prompt(enemyMessage("Unfortunately, you got it wrong. Better luck next time.", "Galdon"))
			prompt(enemyMessage("Well, thanks for playing with me! I'm going home now."))
			prompt(playerName + ": Alright then, see you later I guess.")
			prompt("Galdon walks back home.")
			prompt("Speaking of walking, you still need to make your way over to that village.")
		else:
			prompt(playerName + ": No thanks, I'm good. I have things to sort out.")
	os.system('cls' if os.name == 'nt' else 'clear')
	time.sleep(2)
	prompt("After a short walk you finally reach the town.")
	menuLoop = 1
	while menuLoop == 1:
		prompt("Welcome to ")
		os.system('cls' if os.name == 'nt' else 'clear')
		print("What do you want to do?")
		print("________________________")
		print("Enter", "			", "Leave")
		playerOption = input()
		if playerOption.lower() == "enter":
			menuLoop = 2
			while menuLoop == 2:
				os.system('cls' if os.name == 'nt' else 'clear')
				print("What building do you want to visit? \n Type 'back' to go back.")
				print("________________________")
				print("Shop", "	", "Town center", "	", "House 1", "	", "House 2", "	", "House 3")
				playerOption = input()
				if playerOption.lower == town.shop:
					menuLoop = 3
					while menuLoop == 3:
						prompt("You walk inside the shop.")
						playerOption = menuUpdate("Welcome to the " + colorama.Fore.LIGHTGREEN_EX + "shop!" + colorama.Fore.WHITE, "Select your course of action. \nType 'back' to go back.", "Health Potion", "Armour", "Glasses", "Map")
						if playerOption.lower() == "health potion":
							playerOption = prompt("Health potion - 5 gold - heals 10 hp \nYour gold: "+ str(playerMoney) + "\nWant to purchase it? yes or no")
							if playerOption.lower() == "yes":
								if playerMoney > 5:
									prompt("You can't buy this!")
								else:
									playerMoney -= 5
									items.append("Health Potion")
									prompt("You bought a health potion!")
						if playerOption.lower() == "armour":
							playerOption = prompt("Armour - 15 gold - +10 defence - one tme purchase\nYour gold: "+ str(playerMoney) + "\nWant to purchase it? yes or no")
							if playerOption.lower() == "yes":
								if playerMoney > 15 or playerHasArmour == True:
									prompt("You can't buy this!")
								else:
									playerMoney -= 15
									playerHasArmour = True
									playerDefence += 10
									prompt("You bought the armour!")
						if playerOption.lower() == "glasses":
							playerOption = prompt("Glasses - 15 gold - +10 accuracy - one tme purchase\nYour gold: "+ str(playerMoney) + "\nWant to purchase it? yes or no")
							if playerOption.lower() == "yes":
								if playerMoney > 15 or playerHasGlasses == True:
									prompt("You can't buy this!")
								else:
									playerMoney -= 15
									playerHasGlasses = True
									weapon.accuracy += 10
									prompt("You bought the glasses!")
						if playerOption.lower() == "map":
							playerOption = prompt("Map - 0 gold - Lets you travel and see surrounding area - one tme purchase\nYour gold: "+ str(playerMoney) + "\nWant to purchase it? yes or no")
							if playerOption.lower() == "yes":
									
									playerHasMap = True
									weapon.accuracy += 10
									prompt("You bought the glasses!")
									


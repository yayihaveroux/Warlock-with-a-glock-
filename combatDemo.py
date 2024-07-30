import os
import sys
import time
import random
import colorama
from pygame import mixer

#Map made using inkarnate.com [online software for DND and such]
#Detail layers hidden and contrast increased to allow for easier conversion to ASKII via online converter
#'map' already exists in python, changed to avoid overwrite
#~96**2 (is 9270, 96*96 = 9216)
worldMap = '''
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
#Initialises music engine and loads exploration track
mixer.init()
mixer.music.load("game/assets/happy.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

#Sounds effects stored as variables for ready use
dryFireSound = mixer.Sound("game/assets/dryFire.mp3")
revolverSound = mixer.Sound("game/assets/revolver.mp3")
assaultRifleSound = mixer.Sound("game/assets/assaultrifle.mp3")
pistolSound = mixer.Sound("game/assets/pistol.mp3")
shotgunSound = mixer.Sound("game/assets/shotgun.mp3")
reloadSound = mixer.Sound("game/assets/reload.mp3")
wizardcry1 = mixer.Sound("game/assets/wizardcry1.mp3")
wizardcry2 = mixer.Sound("game/assets/wizardcry2.mp3")
wizardcry3 = mixer.Sound("game/assets/wizardcry3.mp3")
walmart = mixer.Sound("game/assets/walmart.mp3")
portal1 = mixer.Sound("game/assets/portal1.mp3")
portal2 = mixer.Sound("game/assets/portal2.mp3")
eagle = mixer.Sound("game/assets/eagle.mp3") #Fun fact: not the actual call, it's a Red-tailed Hawk's
typeClick = mixer.Sound("game/assets/type.mp3") #'type' already exists in python, changed to avoid overwrite

#Array to be appended with messages to display save progress
history = []

#Prints history array
def historyPrint():
	for x in range(0,len(history)):
		print(history[x])

#Prints string after clearing terminal
#Mimics typing by printing words rapidly instead of all at once
#Emulates early text adventures with typeClick sound effect played per word
#Allows for historyPrint to be used
def prompt(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	history.append(str)
	for word in str.split():
		time.sleep(0.05)
		mixer.Sound.play(typeClick)
		print(f'{word:>1} ', end='')
		sys.stdout.flush()
	time.sleep(0.01)
	print("\n")
	promptContinue = input()
	if promptContinue.lower() != "history":
		return promptContinue
	else:
		historyPrint()
		input()
		for word in str.split():
			time.sleep(0.05)
			print(f'{word:>1} ', end='')
			sys.stdout.flush()
		time.sleep(0.01)
		print("\n")
		promptContinue = input()
		return(promptContinue)

#Same as prompt by has higher sleep intervals
#Used when dramatic effect is needed
def promptSlow(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	history.append(str + "\n")
	for word in str.split():
		time.sleep(0.4)
		mixer.Sound.play(typeClick)
		print(f'{word:>1} ', end='')
		sys.stdout.flush()
	time.sleep(0.01)
	print("\n")
	promptContinue = input()
	if promptContinue.lower() != "history":
		return promptContinue
	else:
		historyPrint()
		input()
		for word in str.split():
			time.sleep(0.05)
			print(f'{word:>1} ', end='')
			sys.stdout.flush()
		time.sleep(0.01)
		print("\n")
		promptContinue = input()
		return(promptContinue)

#Function to colour input in Blue, Red, White
#Used to give flair and drama when talking about America due to theme
def america(text):
    counter = 0
    colour = colorama.Fore.RED
    colouredText = ""
    for word in text.split():
        colouredText += colour + word + " "
        counter += 1
        if counter % 3 == 0:
            colour = colorama.Fore.RED
        elif counter % 3 == 1:
            colour = colorama.Fore.WHITE
        else:
            colour = colorama.Fore.BLUE
    return colouredText.rstrip() + colorama.Fore.RESET #.rstrip removes space at end

#Displays 2 strings seperated by newline, then a line of _
#Prints 6 strings seperated by a large space, then 2 newline
#Input returned to allow for selection from display
#Defaults to allow only description strings
def menuUpdate(description, description2,  option1="", option2="", option3="", option4="", option5="", option6=""):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(description)
	print(description2)
	print("____________________________________________________________________________________________________________\n")
	print(f"{option1}     {option2}     {option3}     {option4}     {option5}     {option6}\n\n")
	return input()

#Defines Class for player's main weapon and its stats
class Gun:
	def __init__(self, name, attack, ammo, maxAmmo, accuracy, sound):
		self.name = name
		self.attack = attack
		self.ammo = ammo
		self.maxAmmo = maxAmmo
		self.accuracy = accuracy
		self.sound = sound

#Defines Class for attack options and their stats
class Target:
	def __init__(self, hitChance, damage):
		self.hitChance = hitChance
		self.damage = damage

#Dictionary of Target Class with keys used to label respective stats
limbs = {
	"head": Target(50, 20),
	"torso": Target(90, 10),
	"arms": Target(75, 15),
	"legs": Target(60, 15)}

#Defines Class for player to allow for more straightforward coding instead of many discrete variables
#temp[Stat]s used to allow for combat to not overwrite permanent stats when player is buffed
class PlayerStats():
	def __init__(self, name, health, maxHealth, hitChance, defence, tempDefence, tempAccuracy, actionPoints, maxActionPoints, spellLevel, spellXP, gold, mana, spellEffect, fireBoltCount):
		self.name = colorama.Fore.CYAN + name + colorama.Fore.RESET #Colours player's name to CYAN
		self.health = health
		self.maxHealth = maxHealth
		self.hitChance = hitChance
		self.defence = defence
		self.tempDefence = tempDefence
		self.tempAccuracy = tempAccuracy
		self.actionPoints = actionPoints
		self.maxActionPoints = maxActionPoints
		self.spellLevel = spellLevel
		self.spellXP = spellXP
		self.gold = gold
		self.mana = mana #Mana is spellcasting cooldown
		self.spellEffect = spellEffect #SpellEffect tracks spells with continuous effects
		self.fireBoltCount = fireBoltCount #FireBoltCount is used to ensure Firebolt is maintained for proper amount of turns

#Default stats for player
#None types present due to combat resetting stats to default at start; not needed to be defined until 1st combat
player = PlayerStats("PLAYER", None, 100, 80, 50, None, None, None, 3, 5, 0, 0, None, None, None)

#Defines Class for enemies to allow stats to be stored with single variable
class Enemy:
	def __init__(self, name, xp, gold, health, maxHealth, attack, accuracy, defence, tempDefence, tempAccuracy, supportSpell, offensiveSpell0, offensiveSpell1, defensiveSpell0, defensiveSpell1):
		self.name = colorama.Fore.RED + name + colorama.Fore.RESET #Colours enemy name to RED
		self.xp = xp
		self.gold = gold
		self.health = health
		self.maxHealth = maxHealth
		self.attack = attack #Non-spells attack power
		self.accuracy = accuracy #Non-spells attack hit chance	
		self.defence = defence
		self.tempDefence = tempDefence
		self.tempAccuracy = tempAccuracy
		self.supportSpell = supportSpell #Healing and recovery spell
		self.offenseSpell = [offensiveSpell0, offensiveSpell1] #Array of attack spells
		self.defenceSpell = [defensiveSpell0, defensiveSpell1] #Array of buff spells

#Basic enemy stats
#Named wizard[Strength] for organised variable naming
wizardApprentice = Enemy("Apprentice Mage", 25, 2, None, 100, 14, 70, 15, None, None, "Spirit-Aid", "Fireball", "Magic Missile", "Windgust", "Levitate")

#Function for playing hurt noises for enemy when hit
def enemyPain():
	randomSound = random.randint(1, 3)
	if randomSound == 1:
		return wizardcry1
	if randomSound == 2:
		return wizardcry2
	if randomSound == 3:
		return wizardcry3

#Selection of player's gun
#Informs of stats of each option if picked but not confirmed
menuLoop = True
while menuLoop == True:
	playerOption = menuUpdate("Pick your weapon.", "Weapons have different stats. This choice is irreversible.", "Pistol", "Revolver", "Assault rifle", "Shotgun")
	if playerOption.lower() in ("pistol", "revolver", "assault rifle", "shotgun"):
		if playerOption.lower() == "pistol":
			playerOption = menuUpdate(f"The{colorama.Fore.LIGHTRED_EX} Pistol{colorama.Fore.WHITE} holds 12 Rounds, has 10 Power, and has 80% accuracy. Confirm?", "      ,_________\n     Y II_____==|\n     )  /J\n    /__/", "Yes", "No")
			if playerOption.lower() == "yes":
				weapon = Gun("Pistol", 10, None, 12, 80, pistolSound)
				menuLoop = False
		elif playerOption.lower() == "revolver":
			playerOption = menuUpdate(f"The{colorama.Fore.LIGHTRED_EX} Revolver{colorama.Fore.WHITE} holds 6 Rounds, has 20 Power, and has 80% accuracy. Confirm?", "      __ _______,\n    _Y__]-------'\n   / _/J\n  |_|\n", "Yes", "No")
			if playerOption.lower() == "yes":
				weapon = Gun("Revolver", 20, None, 6, 80, revolverSound)
				menuLoop = False
		elif playerOption.lower() == "assault rifle":
			playerOption = menuUpdate(f"The{colorama.Fore.LIGHTRED_EX} Assault Rifle{colorama.Fore.WHITE} holds 30 Rounds, has 15 Power, shoots a 3 Round burst each Turn, and has 65% accuracy. Confirm?", "                 ___\n                [_-_]\n      _________,-'-'--_______/|\n     |       _     ___|_.......-------=\n     |__...'' / /J|  |\n             /_/   \\__\\", "Yes", "No")
			if playerOption.lower() == "yes":
				weapon = Gun("Assault Rifle", 15, None, 30, 65, assaultRifleSound)
				menuLoop = False
		elif playerOption.lower() == "shotgun":
			playerOption = menuUpdate(f"The{colorama.Fore.LIGHTRED_EX} shotgun{colorama.Fore.WHITE} holds 2 Rounds, has 35 Power, and has 50% accuracy. Confirm?", "                      _,______________________________,\n       _______..... Y.____|___|______________________|\n      |             _____.......------'\n      |        ..'''   J\n      |___...''\n", "Yes", "No")
			if playerOption.lower() == "yes":
				weapon = Gun("Shotgun", 35, None, 2, 50, shotgunSound)
				menuLoop = False
	else:
		prompt("INVALID!")

#Lines for enemies to say in combat depending on hit/miss state
#attack + miss for player attacking
#hit + defence for enemy attacking
attackLines = ["It's only a matter of time until we win!", "I will pry that wand back into our hands!", "Seems like that thing will be mine!", "Victory is mine!", "*STARES INTENSELY*"]
missLines = ["You sure are lucky... for now!", "How did you dodge that?!?", "Looks like I should get serious!", "We won't lose!", "I'm starting to get the hang of this fight!"]
hitLines = ["ARGH, I'll make you pay for that!", "OW! curse you!", "OW! What dark magic fuels that wretched thing??", "OWIE! Where the hell did you get that thing?", "OUCH, wait until the wizard king hears about this!"]
defenceLines = ["AHAHAHA! No amount of magic will fix your terrible aim!", "Imagine not being able to guide your shots using sorcery, loser!", "Even with that thing, you're no match for a wizard!", "No matter how hard you try, your resistance will be in vain.", "That thing is no match against our magic."]

#Function to provide enemy dialogue
def enemyMessage(message, name):
	if message == "attack":	
		return (f"{name}: {attackLines[random.randint(0,4)]}")
	elif message == "miss":
		return (f"{name}: {missLines[random.randint(0,4)]}")
	elif message == "hit":
		return (f"{name}: {hitLines[random.randint(0,4)]}")
	elif message == "defence":
		return (f"{name}: {defenceLines[random.randint(0,4)]}")
	else:
		return (f"{name}: {message}") #Needs to be string for prompt to accept

#Defines Class for element types to attack with
class DamageType:
	def __init__(self, name, power):
		self.name = name
		self.power = power

#List of elements used by player
#Currently only Fire for Firebolt spell 
playerDamageElement = [DamageType("Fire", 0)]

#Function for attacking by player or enemy
#2d100 needed to avoid max(attacker, defender) because lower value would be fully ignored
#Target, limb default to "" to allow enemy attack to require only 1 input; player always needs 3
#random.binomialvariate() is a normal curve (bell) to make damage different between attacks
def attack(attacker, target="", limb=""):
	hitPercent = random.randint(1, 100) #d100 to check if attacker's accuracy succeeds
	bodyHit = random.randint(1, 100) #d100 to check if defender avoids full hit
	if attacker == "player": #Checks if player or enemy and runs appropriate code
		if weapon.name == "Assault Rifle": #Gives the 3 Round burst
			burst = 3
		else:
			burst = 1
		if player.spellEffect == "Boom-arang": #Runs code for 1 Turn spell
			burst += 1
			weapon.ammo += 2
			player.spellEffect = None
		for i in range(burst): #Loops attack to allow for effects above to give extra hits
			targetDebuff = ""
			if player.spellEffect == "Firebolt": #Runs code to constrain Firebolt amount to proper
				if player.fireboltCount == 0:
					player.spellEffect = None
					playerDamageElement[0].power = 0
				player.fireboltCount -= 1
			weapon.ammo -= 1
			mixer.Sound.play(weapon.sound)
			if hitPercent <= player.tempAccuracy and bodyHit <= limb.hitChance:
				mixer.Sound.play(enemyPain())
				damageNumber = ((limb.damage + weapon.attack + sum(element.power for element in playerDamageElement) + random.binomialvariate(5)) - target.tempDefence) #Saves damage to be displayed to player
				target.health -= damageNumber
				if limb.hitChance == 75: #Checks if hit arms and gives debuff; has to use hitChance due to quirks of dict formatting (can't get key itself easily)
					target.tempAccuracy -= 10
					targetDebuff = "; Arms Hit! -10 Accuracy to Target"
				elif limb.hitChance == 60: #Checks if hit legs and gives buff
					player.actionPoints += 1
					targetDebuff = "; Legs Hit! +1 AP"
				prompt(f"Hit {target.name}! -{damageNumber} Enemy Health: {target.health} / {target.maxHealth}{targetDebuff}")
				prompt(enemyMessage("hit", target.name))
			else:
				if player.tempAccuracy >= random.randint(target.tempDefence, limb.hitChance): #Checks if player can get minor damage
					damageNumber = max(1, int(random.binomialvariate(10) * (weapon.attack / target.tempDefence))) #Grazes always deal at least 1 damage
					target.health -= damageNumber
					prompt(f"Glanced {target.name}! -{damageNumber} Enemy health: {target.health} / {target.maxHealth}")
				else:
					prompt(f"Missed {target.name}! Enemy health: {target.health} / {target.maxHealth}")
				prompt(enemyMessage("defence", target.name))
	else: #Same as prior but for enemy
		if hitPercent <= attacker.tempAccuracy and bodyHit <= player.hitChance:
			damageNumber = (attacker.attack + random.binomialvariate(8) + 50 - player.tempDefence) #+50 to negate default player defence but allow for defence buff bonuses
			player.health -= damageNumber
			prompt(f"Hit {player.name}! -{damageNumber} Health: {player.health} / {player.maxHealth}")
			prompt(enemyMessage("attack", attacker.name))
		else:
			if attacker.tempAccuracy >= random.randint(player.tempDefence, player.hitChance):
				damageNumber = max(1, int(random.binomialvariate(10) * (attacker.attack / player.tempDefence)))
				player.health -= damageNumber
				prompt(f"Glanced {player.name}! -{damageNumber} Health: {player.health} / {player.maxHealth}")
			else:
				prompt(f"Missed {player.name}! Health: {player.health} / {player.maxHealth}")
			prompt(enemyMessage("miss", attacker.name))

#Defines class for spells with all stats in spell itself
class Spell:
	def __init__(self, name, level, mana, description, message):
		self.name = name
		self.level = level
		self.mana = mana
		self.description = description
		self.message = f"You cast {name}! {message}" #Message when spell is cast

	#Logic for executing spells
	def cast(self, select, wizard1, timer): #Timer is needed to control Stars and Stripes
		if select.lower() == "shield":
			player.tempDefence += 2 * player.spellLevel + 10
		elif select.lower() == "firebolt":
			player.spellEffect = "Firebolt"
			player.fireboltCount = 3
			playerDamageElement[0].power = 2 + 2 * player.spellLevel
		elif select.lower() == "guided bullets":
			player.tempAccuracy += 10
			playerDamageElement[0].power = (5 + (player.spellLevel * 2))
		elif select.lower() == "boom-arang":
			player.spellEffect = "Boom-arang"
		elif select.lower() == "healing":
			player.health = min(player.maxHealth, player.health + 15)
		elif select.lower() == "stars and stripes finisher":
			if timer != 0: #If not ready, wastes an AP
				prompt("The spell fizzles and fails to cast! Your wand is not ready.")
			else:
				mixer.music.fadeout(2000)
				time.sleep(2)
				mixer.music.load("game/assets/thelandofthefree.mp3")
				mixer.music.set_volume(1)
				mixer.music.play()
				prompt(f"Your look down at your wand. It's flashing with {america("RED, WHITE, BLUE!")}")
				prompt("You can feel the pure patriotism in your veins, pulsing from the wand.")
				mixer.Sound.play(eagle)
				prompt("In the distance, you hear the mighty Bald Eagle, a symbol of American freedom.")
				prompt("You raise your wand into the air, calling out.")
				prompt(f"{player.name}: UNCLE SAM! DESTROY MY ENEMIES, AND MY OIL IS YOURS!")
				prompt("Suddenly, your opponent cries out in pain as he gets 13 slashes across his neck, one for each stripe on the American flag.")
				prompt(enemyMessage("W-WHAT?? WHAT SPELL IS THAT, I'VE NEVER SEEN IT!", wizard1.name))
				prompt("From the sky, 50 stars start to descend from the heavens.")
				prompt(f"{player.name}: Taste the might of PURE, UNFILTERED FREEDOM.")
				prompt(f"The stars land on the enemy. They explode in a blinding flash of {america("THE AMERICAN UNION")}, leaving just a crater.")
				mixer.music.fadeout(5000)
				wizard1.health = 0
		player.mana += self.mana
		prompt(self.message)

#List of spells and their defined stats
spells = [
	Spell("Firebolt", 1, 3, "Rounds are turned molten as they exit the barrel. For the next 3 Shots, each Rounds hits inflict Fire Damage. Fire Damage = 2 x Level, +2.", "Your next 3 Rounds inflict Fire Damage."),
	Spell("Shield", 1, 1, "Magic Armour spreads attacks over your body. Absorbs damage for 1 Turn. Defence Buff = 2 * Level, +10.", "Your Defence is increased for this Turn."),
	Spell("Guided Bullets", 2, 2, "Rounds predict enemy movement. Shots are more accurate for 1 Turn. Accuracy Buff = +10.", "Your Accuracy is increased for this Turn."),
	Spell("Healing", 2, 4, "Patriotism calms your heart, soul, and mind. Recover up to 15% Health. +15 Health", "You gained 15 health."),
	Spell("BOOM-arang", 3, 3, "The next Round returns to you, attacking on the way back. The next Shot doesn't consume Ammo and attacks twice.", "Your next Round returns to the chamber."),
	Spell("Stars and Stripes Finisher", 5, 0, "Finishing move that can be performed once charged. Instant Kill.", f"{america("GOD BLESS AMERICA!")}")]

#Function to display available spells to player
#Effectively a modified menuUpdate
def spellMenu(description1, description2):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(description1)
	print(description2)
	print("____________________________________________________________________________________\n")
	for spell in spells: #Only displays spells player can cast
		if player.spellLevel >= spell.level:
			print(f"{spell.name} [{spell.mana} MP]: {spell.description} \n")
	return input()

#List of items carried by player
items = []

#Function to display items list and allow use of applicable items
def inventory():
	if not items: #If items is empty
		prompt("You have no items.")
	else:
		prompt("You have the following items:")
		for item in items:
			print(item)
		print("\n")
		use = input("Use item: ")
		if not use:
			return
		else:
			if use.lower() in [item.lower() for item in items]: #Checks if player has item before running effects; Action Point logic included to avoid wasting turns for checking items available
				if use.lower() == "health potion":
					if player.health == player.maxHealth:
						prompt("You already have full Health.")
					else:
						player.health = min(player.maxHealth, player.health + 15)
						prompt("You drink a Health Potion, You gain 15 health!")
						items.remove("Health Potion")
						player.actionPoints -= 1
				elif use.lower() == "mana potion":
					if player.mana == 0:
						prompt("You have full Mana.")
					else:
						player.mana = max(0, player.mana - 3)
						prompt("You drink a Mana Potion, You gain 3 mana!")
						items.remove("Mana Potion")
						player.actionPoints -= 1
				elif use.lower() == "map":
					print(worldMap)
					print()
				else:
					prompt("You cannot use that item.") #If item has no associated logic
			else:
				prompt("You don't have that item.") #If player wants to use item not in items list

#Function to process combat
def fight(wizard1, message, music):
	#Sets temp[Stat] values to defaults.
	weapon.ammo = weapon.maxAmmo
	player.health = player.maxHealth
	player.mana = 0
	player.tempAccuracy = weapon.accuracy
	player.tempDefence = player.defence
	player.actionPoints = player.maxActionPoints
	wizard1.health = wizard1.maxHealth
	wizard1.tempAccuracy = wizard1.accuracy
	wizard1.tempDefence = wizard1.defence
	#If player has unlocked Stars and Stripes before fight, it counts down until cast
	if player.spellLevel == 5:
		timer = 7
	else:
		timer = None
	#Sets turn to player
	battleTurn = 2
	# plays cool battle music to kill wizards to
	mixer.music.stop()
	mixer.music.load(music)
	mixer.music.play(-1,)
	# the battle ends when battleTurn is False.
	#0 counts as false; that's why it starts at 1
	while battleTurn != False:
		while battleTurn == 1: #Player death logic
			os.system('cls' if os.name == 'nt' else 'clear')
			mixer.music.fadeout(3000)
			mixer.music.load("game/assets/death.mp3")
			mixer.music.play(-1)
			prompt("You have died.")
			promptSlow(f"{colorama.Fore.RED}YOU HAVE FAILED ME.")
			promptSlow("YOU HAVE FAILED YOUR COUNTRY.")
			os.system('cls' if os.name == 'nt' else 'clear')
			time.sleep(3)
			promptSlow(f"GOODBYE.{colorama.Fore.RESET}")
			mixer.music.fadeout(5000)
			time.sleep(5)
			sys.exit(0)
		# the player's turn.
		while battleTurn == 2:
			#If player.health is 0 or -, the death sequence starts
			#If enemy is dead the loop ends
			#If AP = 0, enemy turn
			if player.health <= 0 or wizard1.health <= 0 or player.actionPoints == 0:
				battleTurn = 1 if player.health <= 0 else False if wizard1.health <= 0 else 3
				break
			#Adds Stars and Stripes counter to display if applicable
			if timer is not None:
				finisher = f"Finisher in: {timer}" if timer else "STARS AND STRIPES IS READY!"
			else:
				finisher = ""
			# Prints menu for player to choose their option.
			#Includes key info, including Action Economy
			playerOption = menuUpdate(f"{message}\n\n {finisher}\n Your Action Points: {player.actionPoints}\n Mana Cooldown: {player.mana}\n Your Ammo: {weapon.ammo} / {weapon.maxAmmo}\n Your Health: {player.health}", f" Enemy Health: {wizard1.health}\n\nChoose an action:", "FIGHT [2 AP]", "SPELLS [1 AP]", "ITEMS [1 AP]","INFO [0 AP]", "RELOAD [2 AP]", "SKIP")
			# if playerOption.lower() equals any valid option, the code beneath this will execute. otherwise the menu will just reprint itself and the player can choose again.
			if playerOption.lower() in ("fight", "spells", "items", "info", "reload", "skip"):
				#Displays extended info
				if playerOption.lower() == "info":
					menuUpdate("", f"{wizard1.name} Health: {wizard1.health}\n{wizard1.name} Defence: {wizard1.tempDefence}\n{wizard1.name} Accuracy: {wizard1.tempAccuracy}", f"Health: {player.health}\nDefence: {player.tempDefence}\nAccuracy: {player.tempAccuracy}\nSpellcasting Level: {player.spellLevel}\nActive Spell Effect: {player.spellEffect}\nAgility: {player.hitChance}")
				#If no option left, can skip to enemy
				elif playerOption.lower() == "skip":
					battleTurn = 3
				#If player has at least 1 AP
				elif player.actionPoints >= 1:
					if playerOption.lower() == "spells":
						if player.mana == 0: #If mana is available
							playerOption = spellMenu("Choose a Spell. More become available at higher Levels.", "You can only use one spell at a time.\n Type 'back' to go back.")
							for magic in spells:
								if playerOption.lower() == magic.name.lower() and player.spellLevel >= magic.level:
									magic.cast(playerOption, wizard1, timer)
									player.actionPoints -= 1
									break
						else:
							prompt("You cannot cast another spell yet!")
					elif playerOption.lower() == "items":
						inventory()
				#If player has 2 or more AP
				if player.actionPoints >= 2:
					if playerOption.lower() == "fight":
						if weapon.ammo == 0: #Prevents fight and returns to menu
							mixer.Sound.play(dryFireSound)
							prompt("No ammo!")
						else:
							playerOption = menuUpdate(f"Where do you want to hit? \n Accuracy: {weapon.accuracy} / 100", "Type 'back' to go back.", f"Head: {limbs["head"].hitChance}%", f"Torso: {limbs["torso"].hitChance}%", f"Arms: {limbs["arms"].hitChance}%", f"Legs: {limbs["legs"].hitChance}%")
							if playerOption in limbs:
								attack("player", wizard1, limbs[playerOption.lower()])
								player.actionPoints -= 2
					elif playerOption.lower() == "reload":
						mixer.Sound.play(reloadSound)
						prompt("RELOADING")
						weapon.ammo = weapon.maxAmmo
						player.actionPoints -= 2
			else:
				prompt("INVALID!")
		#Enemy's turn
		if battleTurn == 3:
			prompt(f"{wizard1.name}'s turn!")
			wizard1Buff = False #Deactivates enemy buff themself protection
			wizard1.tempDefence = wizard1.defence #Resets enemy defence
			if random.randint(1,8) <= 3: #3/8 chance to cast a spell
				wizardMagicChance = random.randint(1,100)
				if wizard1.health != wizard1.maxHealth and wizardMagicChance * (wizard1.health / wizard1.maxHealth) <= 25: #Can't heal at max health
					if wizard1.supportSpell == "Spirit-Aid":
						wizard1.health = min(wizard1.maxHealth, wizard1.health + 10)
						prompt(f"{wizard1.name} casts Spirit-Aid! They recover 10 Health.")
				elif wizardMagicChance >= 60:
					hitChance = random.randint(1,100)
					if hitChance <= (100 - player.tempDefence):
						offenseSpell = wizard1.offenseSpell[random.randint(0,1)]
						if offenseSpell == "Fireball":
							damageNumber = max(10, random.randint(60, 75) - player.tempDefence) #Deals at least 10
							player.health -= damageNumber
							prompt(f"{wizard1.name} casts Fireball! -{damageNumber} Health: {player.health} / {player.maxHealth}!")
						elif offenseSpell == "Magic Missile":
							damageNumber = wizard1.tempAccuracy // 4 #Guaranteed to hit because that's the point of Magic Missiles
							player.health -= damageNumber
							prompt(f"{wizard1.name} casts Magic Missile! -{damageNumber} Health: {player.health} / {player.maxHealth}")
					else:
						prompt(f"You dodge {wizard1.name}'s Spell!")
				else:
					defenceSpell = wizard1.defenceSpell[random.randint(0,1)]
					if defenceSpell == "Windgust":
						wizard1Buff = True #Enables buff protection
						wizard1.tempAccuracy += 10
						prompt(f"{wizard1.name} casts Windgust! Their Accuracy increases by 10!")
					elif defenceSpell == "Levitate":
						wizard1.tempDefence += 5
						prompt(f"{wizard1.name} casts Levitate! Their Defence increases by 5!")
			else:
				attack(wizard1)
			#Resetting stats
			player.tempAccuracy = weapon.accuracy
			player.tempDefence = player.defence
			player.mana = max(0, player.mana - 1) #Counts mana down to 0
			player.actionPoints = player.maxActionPoints
			if wizard1Buff == False: #Buff protection needed to keep until next attack
				wizard1.tempAccuracy = wizard1.accuracy
			if player.spellLevel == 5: #Counts down Stars and Stripes timer
				timer = max(0, timer - 1)
			battleTurn = 2 #Player's turn now
	#Victory state
	player.spellXP += wizard1.xp
	player.gold += wizard1.gold
	prompt(f"YOU WON! + {wizard1.xp} XP + {wizard1.gold} GP")
	xpCheck = player.spellLevel * 50
	if player.spellXP >= xpCheck: #Rewards a Level up if XP is high enough
		player.spellXP -= xpCheck
		player.spellLevel += 1
		prompt(f"You have Levelled Up! Level: {player.spellLevel}")

#Test fight
fight(wizardApprentice, "Wizard approaches", "game/assets/infectedMushroom.mp3")
print("END")

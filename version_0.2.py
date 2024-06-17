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
#any time you see an input() like this, its so that the user can press enter and continue


# initialising music to play later. can only play one song at once.
mixer.init()
mixer.music.load("assets/happy.mp3")
mixer.music.set_volume(0.7)

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
# creating player variables
playerName = " "
playerHealth = 100
playerDefence = 50
playerTempDefence = 0
playerActionPoints = 3


history = []
class spellLevels:
	def __init__(self, spellLevel, spellXP):
		self.spellLevel = spellLevel
		self.spellXP = spellXP

playerSpells = spellLevels(1, 0)
# menuloop controls while statements
menuLoop = 1

# battle-specific variables/ functions

colorama.Style.DIM

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
		print("HEALING: heal 15% damage. \n")
	if playerSpells.spellLevel >= 5:
		print(colorama.Fore.BLUE + "STARS" + colorama.Fore.WHITE +  " AND " + colorama.Fore.RED + "STRIPES " + colorama.Fore.WHITE + "FINISHER: Finishing move that can be performed on opponents with less then 10% health. \n")
	return input()


#displays fancy message on screen. clears screen beforehand
def prompt(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	history.append(str)
	for word in str.split():
		time.sleep(0.05)
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



def oldPrompt(str):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(str)
	return input()

def historyPrint():
	for x in range(0,len(history)):
		print(history[x])


testenemy = Enemy("testwizard", 100, 100, 0.2, 30, 70, "fireball", "healing", "spirit's aid")
head = Target(50, 40,) #35
torso = Target(90, 10) #50
legs = Target(75, 15) #45
arms = Target(75, 15)#45


devcode = prompt("enter devcode")
if devcode == "spells":
	playerSpells.spellLevel = 5
	prompt("devcode recieved")



prompt("WELCOME TO WARLOCK WITH A GLOCK, BY FEDBEAN INTERACTIVE")

prompt("YOUR JOURNEY IS ABOUT TO BEGIN.")
#playerName = prompt("BUT FIRST, WHAT IS YOUR NAME? TYPE IT BELOW.")
#playerOption = prompt("IS " + playerName + " YOUR NAME? YES OR NO")
#while playerOption != "yes":
#    playerName = prompt("REENTER YOUR NAME BELOW.")
#    playerOption = prompt("IS " + playerName + " YOUR NAME? YES OR NO")
#prompt(playerName + " IS YOUR NAME.")
#prompt("Your story is about to begin.")
#os.system('cls' if os.name == 'nt' else 'clear')


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
	playerWeapon = menuUpdate("Pick your weapon.", "weapons have different stats. this choice is irreversible. type the number of your desired weapon.", "1. pistol", "2. revolver", "3. assault rifle", "4. shotgun")
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

# FIGHT TIME
prompt("you have picked the " + playerWeapon + ".")
prompt(playerName + ": This is quite the fine weapon if I do say so myself!")
prompt("You pull it off the wall and admire it.")
mixer.Sound.fadeout(walmart, 2000)
mixer.music.fadeout(2000)
time.sleep(2)
prompt("Suddenly, you hear a noise.")
mixer.Sound.play(portal1)
prompt(playerName + ": Huh??")
prompt("A sort of... puddle has formed on the floor suddenly. It wasn't there before.")
prompt("You lean over it to get a better look, still clutching the gun in your hands. The puddle is a bright shade of blue and has a sort of swirling pattern to it.")
prompt("You go to touch it, but you accidentally drop the gun you were holding! As you attempted to grab it, you fell into the puddle.")
prompt("You didn't hit the floor though. Somehow you fell through it!")
mixer.Sound.play(portal2)
time.sleep(12)

prompt(enemyMessage("''Where did you send the damn portal to?'", "Unknown person 1"))
prompt(enemyMessage("''Hang on, let me check the spellbook again...'", "Unknown person 2"))
time.sleep(2)
prompt(enemyMessage("''It says... someplace called Earth... do you happen to know where that is?'", "Unknown person 2"))
time.sleep(1)
mixer.Sound.play(portal1)
prompt(playerName + ": AAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH")


def fight(wizard1, menuLoopValue, message, music):
	wizard1.name = colorama.Fore.LIGHTBLUE_EX + wizard1.name + colorama.Fore.WHITE
	missTurn = 0
	battleTurn = 1
	menuLoop = menuLoopValue
	playerCastSpell = False
	playerTempAccuracy = 0
	playerSpellEffect = ""
	playerFireballCount = 0
	mixer.music.stop()
	mixer.music.load(music)
	mixer.music.play(-1,)
	while menuLoop == menuLoopValue:
		while wizard1.health > 0:
			while battleTurn == 1:
				playerSpell = " "
				playerTempDefence = 0
				playerTempAccuracy = weapon.accuracy
				global playerHealth
				
				playerOption = menuUpdate( message + "\n \nyour ammo:" + str(weapon.ammo) + " / " + str(weapon.maxAmmo),
										  "Your health: " + str(playerHealth) + "\nEnemy health: " + str(wizard1.health) + "\n \nChoose an action: (currently only fighting works. Wizard doesnt fight back yet.) ", "FIGHT",
										  "SPELLS", "EXTRA", "RUN AWAY")
				if playerOption.lower() == "fight" or playerOption.lower() == "spells" or playerOption.lower() == "extra" or playerOption.lower() == "run away":
					if playerOption.lower() == "fight":
						playerHit = menuUpdate("Where do you want to hit? \n accuracy = " + str(weapon.accuracy) + "/ 100", "Type 'back' to go back.", "head", "torso", "legs",
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
											mixer.Sound.play(enemyPain())
											wizard1.health = wizard1.health - (head.damage + (
														(1 - wizard1.defence) * weapon.attack))
											prompt("hit! enemy health: " + str(wizard1.health) + " / " + str(
												wizard1.maxHealth))
											prompt(enemyMessage("hit", wizard1.name))
											battleTurn = 2
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""

										else:
											prompt("miss! enemy health: " + str(wizard1.health) + " / " + str(
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
											wizard1.health = wizard1.health - (torso.damage + (
														(1 - wizard1.defence) * weapon.attack))
											prompt("hit! enemy health: " + str(wizard1.health) + " / " + str(
												wizard1.maxHealth))
											battleTurn = 2
											prompt(enemyMessage("hit", wizard1.name))
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""
										else:
											battleTurn = 2
											prompt("miss! enemy health: " + str(wizard1.health) + " / " + str(wizard1.maxHealth))
											prompt(enemyMessage("miss", wizard1.name))
											
									elif playerHit.lower() == "legs": 
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < legs.accuracy:
											mixer.Sound.play(enemyPain())
											wizard1.health = wizard1.health - (legs.damage + (
														(1 - wizard1.defence) * weapon.attack))
											prompt("hit! enemy misses turn! enemy health: " + str(
												wizard1.health) + " / " + str(wizard1.maxHealth))
											missTurn = 1
											prompt(enemyMessage("hit", wizard1.name))
											if playerSpellEffect == "fireball":
												playerFireballCount = 3
												playerSpellEffect = ""
										else:
											prompt("miss! enemy health: " + str(wizard1.health) + " / " + str(
												wizard1.maxHealth))
											prompt(enemyMessage("miss", wizard1.name))
											battleTurn = 2
									elif playerHit.lower() == "arms":
										playerHitPercent = random.randint(1, 100)
										bodyHitPercent = random.randint(1, 100)
										weapon.ammo = weapon.ammo - 1
										mixer.Sound.play(weapon.sound)
										if playerHitPercent < weapon.accuracy and bodyHitPercent < arms.accuracy:
											mixer.Sound.play(enemyPain())
											wizard1.health = wizard1.health - (arms.damage + (
														(1 - wizard1.defence) * weapon.attack))
											prompt("hit! enemy accuracy decreased! enemy health: " + str(
												wizard1.health) + " / " + str(wizard1.maxHealth))
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
								else:
									if playerHit.lower() == "head":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < head.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - (head.damage + (
															(1 - wizard1.defence) * weapon.attack))
												prompt("hit! enemy health: " + str(wizard1.health) + " / " + str(
													wizard1.maxHealth))
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
									elif playerHit.lower() == "torso":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < torso.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - (torso.damage + (
															(1 - wizard1.defence) * weapon.attack))
												prompt("hit! enemy health: " + str(wizard1.health) + " / " + str(
													wizard1.maxHealth))
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
									elif playerHit.lower() == "legs":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < legs.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - (legs.damage + ((1 - wizard1.defence) * weapon.attack))
												prompt("hit! enemy misses turn! enemy health: " + str(
													wizard1.health) + " / " + str(wizard1.maxHealth))
												missTurn = 1
												prompt(enemyMessage("hit", wizard1.name))
												if playerSpellEffect == "fireball":
													playerFireballCount = 3
													playerSpellEffect = ""
											else:
												prompt("miss! enemy health: " + str(wizard1.health) + " / " + str(
													wizard1.maxHealth))
												prompt(enemyMessage("miss", wizard1.name))

									elif playerHit.lower() == "arms":
										for x in range(0, 3):
											playerHitPercent = random.randint(1, 100)
											bodyHitPercent = random.randint(1, 100)
											weapon.ammo = weapon.ammo - 1
											mixer.Sound.play(weapon.sound)
											if playerHitPercent < weapon.accuracy and bodyHitPercent < arms.accuracy:
												mixer.Sound.play(enemyPain())
												wizard1.health = wizard1.health - (arms.damage + (
															(1 - wizard1.defence) * weapon.attack))
												prompt("hit! enemy accuracy decreased! enemy health: " + str(
													wizard1.health) + " / " + str(wizard1.maxHealth))
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
						# else:
						elif playerHit == "back":
							battleTurn = 1
						else:
							prompt("invalid selection!")
					elif playerOption.lower() == "spells":
						playerOption  = spellMenu("Choose a spell. More spells become available to you the higher level you are.", "You can only use one spell per turn. using spells will not end your turn.\n Type 'back' to go back.")
						if playerOption.lower() == "back":
							battleTurn = 1
						elif playerCastSpell == True:
							prompt("You already cast a spell this turn!")
						elif playerOption.lower() == "shield" and playerCastSpell == False and playerSpells.spellLevel >= 1:
							playerCastSpell = True
							playerTempDefence = playerDefence
							playerDefence += 10
							prompt("You cast shield! Your defence is increased by 10 for this turn.")
							playerSpells.spellXP += 10
						elif playerOption.lower() == "guided bullets" and playerCastSpell == False and playerSpells.spellLevel >= 2:
							playerCastSpell = True
							playerTempAccuracy = weapon.accuracy
							weapon.accuracy += 10
							prompt("You cast guided bullets! Your accuracy is increased by 10 for this turn.")
							playerSpells.spellXP += 10
						elif playerOption.lower() == "fireball" and playerCastSpell == False and playerSpells.spellLevel >= 3 and playerFireballCount <= 0:
							playerCastSpell = True
							playerSpellEffect = "fireball"
							prompt("You cast fireball! Your bullets fired this turn inflict fire damage that lasts for 3 turns.")
							playerSpells.spellXP += 10
						elif playerOption.lower == "fireball" and playerFireballCount > 0:
							prompt("Fireball is already in effect!")
						elif playerOption.lower() == "healing" and playerCastSpell == False and playerSpells.spellLevel >= 4:
							playerCastSpell = True
							prompt("You cast healing! You gained 15 health.")
							playerHealth += 15
							if playerHealth > 100:
								playerHealth = 100
							playerSpells.spellXP += 10
						elif playerOption.lower() == "stars and stripes finisher" and playerCastSpell == False and playerSpells.spellLevel >= 5 and wizard1.health > 20:
							playerCastSpell = True
							prompt("You cast the stars and stripes finisher.")
							mixer.music.fadeout(2000)
							time.sleep(2)
							mixer.music.load("assets/thelandofthefree.mp3")
							mixer.music.play()
							prompt("Your look down at your wand. its flashing red, white, and blue.")
							prompt("You can feel the pure patriotism in your veins, pulsing from the wand.")
							prompt("In the distance, you hear the mighty Bald Eagle, a symbol of American freedom.")
							prompt("You raise your wand into the air, calling upon the Eagle.")
							prompt(playerName + ": UNCLE SAM! DESTROY MY ENEMIES, AND MY OIL IS YOURS!")
							prompt("Suddenly, your opponent cries out in pain as he gets 13 slashes across his neck, one for each stripe on the American flag.")
							prompt(enemyMessage("W-WHAT?? WHAT SPELL IS THAT, I'VE NEVER SEEN IT!", wizard1.name,))
							prompt("From the sky, 50 stars start to descend from the heavens.")
							prompt(playerName + ": Taste the might of PURE, UNFILTERED FREEDOM.")
							prompt("The stars land on the enemy. They explode in a blinding flash of white, leaving just a crater.")
							battleTurn = 0
							wizard1.health = 0
							playerSpells.spellXP += 10
					elif playerOption.lower() == "extra":
						playerOption = menuUpdate("Do you want to view info or items?", "type 'back' to go back.", "Info", "			", "			", "Items" )
						if playerOption.lower() == "info":
							prompt("Enemy defence: " + str(wizard1.defence) + "\n Enemy accuracy: " + str(wizard1.accuracy) + "\n Enemy health: " + str(wizard1.health))
							prompt("Your defence: " + str(playerDefence) + "\n Your accuracy: " + str(weapon.accuracy) + "\n Your health: " + str(playerHealth))
			# else:
			if playerFireballCount > 0:
				wizard1.health -= 5
				playerFireballCount -= 1
				prompt("Your enemy takes fire damage! -5 hp!")
			if missTurn == 0:
				battleTurn = 2
			else:
				battleTurn = 1
				missTurn = 0
			if wizard1.health <= 0:
				prompt("you killed him! yippee!!!")
				battleTurn = 0
				menuLoop = menuLoopValue + 1
			else:
				while battleTurn == 2:
					playerCastSpell = False
					playerSpellEffect = ""
					weapon.accuracy = playerTempAccuracy
					playerDefence = playerTempDefence
					prompt("the wizard's turn.")
					battleTurn = 1

fight(testenemy, 2, "THE WIZARD " + colorama.Fore.RED + testenemy.name + colorama.Fore.WHITE + " APPROACHES", "assets/battle1.mp3")

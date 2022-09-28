from time import perf_counter
from msvcrt import kbhit, getch

# IDEAS
# Type the text out (DONE)
# Select between choices using arrows (prompt function) (DONE)
# 	Currently selected choice would have a white foreground (CHANGED)
# 	Make the selection green once it's chosen (CHANGED)
# Let user type name (DONE)
# Maybe some ascii animation? (FAIL)
# Sound effects? (FAIL)
# Turn color ON or OFF (FAIL)
# Add checkboxes (FAIL)
# Money/Currency (FAIL)
# Health bar (FAIL)
# Reference discovered fallacies (FAIL)
# Develop cultish role and use what you know to counter-argue points (FAIL)

class Text:
	ESC = "\x1b"
	CLEAR = 0
	BOLD = 1
	DIM = 2
	ITALIC = 3
	UNDERLINE = 4
	BLINK = 5
	INVERT = 7
	HIDDEN = 8
	RBOLD = 21
	RDIM = 22
	RITALIC = 23
	RUNDERLINE = 24
	RBLINK = 25
	RINVERSE = 27
	RHIDDEN = 28
	UNDERLINE = 4
	FBLACK = 30
	FRED = 31
	FGREEN = 32
	FYELLOW = 33
	FBLUE = 34
	FMAGENTA = 35
	FCYAN = 36
	FWHITE = 37
	BBLACK = 40
	BRED = 41
	BGREEN = 42
	BYELLOW = 43
	BBLUE = 44
	BMAGENTA = 45
	BCYAN = 46
	BWHITE = 47

class Fallacy:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		return self.name

def sgr(*decs):
	return f"{Text.ESC}[" + ";".join(map(str, decs)) + "m"

def clear():
	return sgr(Text.CLEAR)

def ttype(text, time=None, handle_SGR=True):
	'''
		text type, or ttype, types out the text rather than printing it instantly
		text = the string which is to be typed
		time = the time it takes to type in seconds
	'''
	if time is None:
		time = len(text) * .03
	typed = 0
	timer = perf_counter()
	s_per_char = time / len(text)
	while typed != len(text) and not kbhit():
		delta = perf_counter() - timer
		if delta >= s_per_char:
			total_chars = int(delta // s_per_char)
			text_to_type = text[typed:(typed + total_chars)]
			# Detect SGR in virtual terminal sequence
			if Text.ESC in text_to_type and handle_SGR:
				index1 = text.find(Text.ESC, typed)
				index2 = text.find('m', index1)
				terminal_seq = text[index1:(1 + index2)]
				normal_text = text_to_type[:text_to_type.find(Text.ESC)]
				text_to_type = normal_text + terminal_seq
				print(text_to_type, end="")
				typed += len(text_to_type)
				total_chars -= len(normal_text)
				text_to_type = text[typed:(typed + total_chars)]

			print(text_to_type, flush=True, end="")
			typed += len(text_to_type)
			timer = perf_counter()
	if kbhit() and typed != len(text):
		getch()
		print(text[typed:], flush=True, end="")

def mul_choice(*choices, tut=False, time=.2, color=(Text.BBLACK, Text.FCYAN), hide=False):
	def render_buttons(cs):
		print("\r", end="")
		for i in range(len(choices)):
			c = choices[i]
			style = color + ((Text.INVERT,) if i == cs else ())
			ttype(sgr(*(style)) + c + clear(), time)
			print(" " * 4, end="")
		if tut:
			print(sgr(Text.BLINK, Text.FRED) + "<ARROWS KEYS TO CHOOSE; ENTER TO SELECT>" + clear(), end="", flush=True)
	def select(cs):
		print("\r", end="")
		for i in range(len(choices)):
			c = choices[i]
			if i == cs:
				ttype(sgr(*color) + c + clear(), time)
			else:
				ttype(sgr(*color, Text.HIDDEN if hide else Text.DIM) + c + clear(), time)
			print(" " * 4, end="")		
	selected = False
	current_selection = 0
	render_buttons(current_selection)
	while not selected:
		if kbhit():
			btn = getch()
			if btn == b'\xe0': # Arrow key pressed
				match getch():
					case b'M': # Right arrow
						current_selection += 1
					case b'K': # Left arrow
						current_selection -= 1
				current_selection = max(0, min(current_selection, len(choices) - 1))
				render_buttons(current_selection)
			elif btn == b'\r':
				selected = True
				select(current_selection)
				print()
				return current_selection

def textfield():
	print(f"{Text.ESC}[{Text.UNDERLINE};{Text.FCYAN}m", end="")
	i = input()
	print(f"{Text.ESC}[0m")
	return i

title = f"""\
{sgr(Text.FCYAN)} /$$   /$$             /$$                                           {sgr(Text.FRED)} /$$$$$$$  /$$                                        
{sgr(Text.FCYAN)}| $$  | $$            | $$                                           {sgr(Text.FRED)}| $$__  $$| $$                                        
{sgr(Text.FCYAN)}| $$  | $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$$         {sgr(Text.FRED)}| $$  \\ $$| $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ 
{sgr(Text.FCYAN)}| $$$$$$$$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$ /$$_____/         {sgr(Text.FRED)}| $$$$$$$/| $$ /$$__  $$ |____  $$ /$$_____/ /$$__  $$
{sgr(Text.FCYAN)}| $$__  $$  /$$$$$$$  | $$    | $$$$$$$$| $$  \\__/|  $$$$$$         {sgr(Text.FRED)} | $$____/ | $$| $$$$$$$$  /$$$$$$$|  $$$$$$ | $$$$$$$$
{sgr(Text.FCYAN)}| $$  | $$ /$$__  $$  | $$ /$$| $$_____/| $$       \\____  $$        {sgr(Text.FRED)} | $$      | $$| $$_____/ /$$__  $$ \\____  $$| $$_____/
{sgr(Text.FCYAN)}| $$  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$       /$$$$$$$//$$      {sgr(Text.FRED)}| $$      | $$|  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$
{sgr(Text.FCYAN)}|__/  |__/ \\_______/   \\___/   \\_______/|__/      |_______/| $/   {sgr(Text.FRED)}   |__/      |__/ \\_______/ \\_______/|_______/  \\_______/
                                                           |_/{clear()}
"""

def print_day(n):
	"""http://patorjk.com/software/taag/ font: doh"""
	day = """\
            dddddddd                                        
            d::::::d                                        
            d::::::d                                        
            d::::::d                                        
            d:::::d                                         
    ddddddddd:::::d   aaaaaaaaaaaaayyyyyyy           yyyyyyy
  dd::::::::::::::d   a::::::::::::ay:::::y         y:::::y 
 d::::::::::::::::d   aaaaaaaaa:::::ay:::::y       y:::::y  
d:::::::ddddd:::::d            a::::a y:::::y     y:::::y   
d::::::d    d:::::d     aaaaaaa:::::a  y:::::y   y:::::y    
d:::::d     d:::::d   aa::::::::::::a   y:::::y y:::::y     
d:::::d     d:::::d  a::::aaaa::::::a    y:::::y:::::y      
d:::::d     d:::::d a::::a    a:::::a     y:::::::::y       
d::::::ddddd::::::dda::::a    a:::::a      y:::::::y        
 d:::::::::::::::::da:::::aaaa::::::a       y:::::y         
  d:::::::::ddd::::d a::::::::::aa:::a     y:::::y          
   ddddddddd   ddddd  aaaaaaaaaa  aaaa    y:::::y           
                                         y:::::y            
                                        y:::::y             
                                       y:::::y              
                                      y:::::y               
                                     yyyyyyy                """.split("\n")

	day1 = """\
  1111111   
 1::::::1   
1:::::::1   
111:::::1   
   1::::1   
   1::::1   
   1::::1   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
   1::::l   
111::::::111
1::::::::::1
1::::::::::1
111111111111""".split("\n")

	match n:
		case 1:
			for i in range(len(day)):
				d = i - 5
				if d < 0 or d >= len(day1):
					print(sgr(Text.FCYAN) + day[i] + clear())
				else:
					print(sgr(Text.FCYAN) + day[i] + " " * 5 + sgr(Text.FRED) + day1[d] + clear())					

def impor(s):
	return sgr(Text.UNDERLINE) + s + sgr(Text.RUNDERLINE)

def boss(s):
	return sgr(Text.ITALIC, Text.FGREEN) + s + clear()

def day0():
	ttype(title, 2)

	ttype(f"""\
You're about to start your first day. You pull up a sticky note. It says 'pw: {impor("kettle")}'
In front of you is building 512 on Harper St. The door looks like any other. You knock three times""")

	ttype("...", 3)
	ttype("The door creaks, opening slightly but without giving away whose behind.\n")

	ttype(boss("Password?") + "\n")

	if mul_choice("Kettle", "Bit", "Quiet", tut=True) != 0:
		ttype("The door closes on you. You walk away with shame and no money.")
		ttype(sgr(Text.BOLD) + "\nGAME OVER" + clear())
		exit()
	ttype(boss("You made the right choice. You'll encounter many haters... debate them and earn money.\n"))


def new_fallacies(f):
	"""Introduce new fallacies for the day"""
	ttype(boss("Learn these fallacies and use them wisely...\n"))
	for i in f:
		ttype(f"{sgr(Text.FCYAN)}{i.name}: {sgr(Text.DIM, Text.FWHITE)}{i.description}{clear()}\n")

def day1():
	def p1(s):
		return sgr(Text.ITALIC, Text.FBLUE) + "Bob: " + s + clear()
	def change_ego(p):
		if p > 0:
			ttype(f"His ego went up by {abs(p)} points\n")
		else:
			ttype(f"You knocked down his ego by {abs(p)} points\n")
		return p
	new_f = [Fallacy("Ad Hominem", "Literally, \"to the man.\" Attacking the person of a source rather than their qualifications or reliability or the actual argument they make."),
	Fallacy("Begging the Question", "Implicitly using the conclusion as a premise."),
	Fallacy("Complex Question", "Occurs when a single question contains multiple parts and an unestablished hidden assumption.")]
	for i in range(3):
		ttype("LOADING DAY 1...\r", 1)
		ttype(f"{sgr(Text.HIDDEN)}LOADING DAY 1...\r{clear()}", .3)
	print_day(1)
	print()
	# Introduce new fallacies everyday
	new_fallacies(new_f)
	ttype("Your first hater is here. He's initiating the debate...\n")
	p1_health = 50
	ttype(p1("Your cult freaking sucks\n") + "What is your response?\n")
	match mul_choice(*map(str, new_f)):
		case 0:
			ttype(p1("Well you f-f-f-freakin deserve it!\n"))
			p1_health += change_ego(-30)
		case 1:
			ttype(p1("Bro I'm not begging nothing!!\n"))
			p1_health += change_ego(20)
		case 2:
			ttype(p1(f"Bro, I didn't even {sgr(Text.ITALIC)} ask {sgr(Text.RITALIC)} you a question!\n"))
			p1_health += change_ego(30)
	ttype(p1(f"Why do you even support Harvey McSadwords when you don't even support sending space ships to space!!\n"))
	ttype(("You can see him sweat a bit. " if p1_health < 50 else "He says it with a clear smirk on his face. ") + "What is your response?\n")
	match mul_choice(*map(str, new_f)):
		case 0:
			ttype(p1("Add my butt! You're wasting my time!\n"))
			p1_health += change_ego(20)
		case 1:
			ttype(p1("I'm the one asking you sir! Sir? Sir? Sir? OH SORRY FOR BEGGING THE QUESTION\n"))
			p1_health += change_ego(30)
		case 2:
			ttype(p1("Agh! Why don't you just answer my question!!\n"))
			p1_health += change_ego(-30)
			ttype("He's beginning to shed some tears. ")
	ttype(p1("I have better things to do. Point is, it's clear your cults \"manifesto\" is wrong because it has a lot of errors\n"))
	match mul_choice(*map(str, new_f)):
		case 0:
			ttype(p1("OK\n"))
			p1_health += change_ego(20)
		case 1:
			ttype(p1("Yeah yeah professor\n"))
			p1_health += change_ego(-30)
		case 2:
			ttype(p1("Not worth my time...\n"))
			p1_health += change_ego(30)

	ttype("He leaves your corner, and another came after him. And another. And another. Before you knew it, it was already night time and your shift was over. Your boss is here to give your report...")
	if p1_health <= 0:
		ttype(boss("Congratulations. You destroyed them with facts and logic. Here's your paycheck, with bonus!\n"))
	elif p1_health < 70:
		ttype(boss("You did alright. Here's your paycheck...\n"))
	else:
		ttype(boss("It would have been better without you. Just go home. No money for you.\n"))
	ttype("And with that, you end your day. Hope you had fun playing!")

day0()
day1()

# print(clear(), end="")
# Will you remember the code?
# YES | NO
# 1) Code is given but scrambled later
# 2) Code is repeated and only one of them is scrambled
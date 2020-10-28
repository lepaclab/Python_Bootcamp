sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

#Write code that loops ovet the list and adds all the strings together to form ine lrge combined string (don't add any spaces between them)
#The combined string should be in all UPPERCASE as well
#Save the result in a variable called result

index = 0

#solution 1
while index < len(sounds):
#for sound in sounds:
	sound = sounds[index]+sounds[index+1]+sounds[index+2]+sounds[index+3]+sounds[index+4]+sounds[index+5]+sounds[index+6]
	result = sound.upper()
	print(result)
	#print(sounds[index]+sounds[index+1]+sounds[index+2]+sounds[index+3]+sounds[index+4]+sounds[index+5]+sounds[index+6])
	break

#Solution 2

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s.upper()

#solution 3

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s
# result = result.upper()
	
	

def checkPangram(s): 
	List = [] 

	for i in range(26): 
		List.append(False) 
		
	for c in s.lower(): 
		if not c == " ": 

			List[ord(c) -ord('a')]= True
			
	for ch in List: 
		if ch == False: 
			return False
	return True

sentence = input()
if (checkPangram(sentence)): 
	print("is a pangram")
else: 
	print( "is not a pangram")

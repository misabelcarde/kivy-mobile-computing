def getButtonPosition(button):
	idSplit = button.id.split("_")
	return [int(idSplit[0]), int(idSplit[1])]

def getLimitingButtons(button):
	res = {}

	idSplit = button.id.split("_")
	row = int(idSplit[0])
	col = int(idSplit[1])

	up = str (row-1)+"_"+str(col)
	up2 = str (row-2)+"_"+str(col)
	down = str (row+1)+"_"+str(col)
	down2 = str (row+2)+"_"+str(col)
	right = str (row)+"_"+str(col+1)
	right2 = str (row)+"_"+str(col+2)
	left = str (row)+"_"+str(col-1)
	left2 = str (row)+"_"+str(col-2)
	res['up'] = up
	res['up2'] = up2
	res['down'] = down
	res['down2'] = down2
	res['right'] = right
	res['right2'] = right2
	res['left'] = left
	res['left2'] = left2

	upLeft = str (row-1)+"_"+str(col-1)
	upRight = str (row-1)+"_"+str(col+1)
	downLeft = str (row+1)+"_"+str(col-1)
	downRight = str (row+1)+"_"+str(col+1)
	res['upLeft'] = upLeft
	res['upRight'] = upRight
	res['downLeft'] = downLeft
	res['downRight'] = downRight

	return res

def getBoatsIds():
	'''boatsXYIds: X boats of Y cells'''
	res = {}

	boats41Ids = ["4_1_0", "4_1_1", "4_1_2", "4_1_3"]
	boats32Ids = [["3_2_0_0", "3_2_0_1"], ["3_2_1_0", "3_2_1_1"], ["3_2_2_0","3_2_2_1"]]
	boats23Ids = [["2_3_0_0","2_3_0_1","2_3_0_2"],["2_3_1_0","2_3_1_1","2_3_1_2"]]
	boats14Ids = ["1_4_0", "1_4_1", "1_4_2", "1_4_3"]

	res['41Ids'] =  boats41Ids
	res['32Ids'] =  boats32Ids
	res['23Ids'] =  boats23Ids
	res['14Ids'] =  boats14Ids

	return res

def exixtsLimits(button, dicc, limits):
	return (limits['up'] in dicc) and (limits['down'] in dicc) and (limits['left'] in dicc) and (limits['right'] in dicc)

def exixtsLimitsNoUp(button, dicc, limits):
	return (limits['up'] not in dicc) and (limits['down'] in dicc) and (limits['left'] in dicc) and (limits['right'] in dicc)

def exixtsLimitsNoDown(button, dicc, limits):
	return (limits['up'] in dicc) and (limits['down'] not in dicc) and (limits['left'] in dicc) and (limits['right'] in dicc)

def exixtsLimitsNoRight(button, dicc, limits):
	return (limits['up'] in dicc) and (limits['down'] in dicc) and (limits['left'] in dicc) and (limits['right'] not in dicc)

def exixtsLimitsNoLeft(button, dicc, limits):
	return (limits['up'] in dicc) and (limits['down'] in dicc) and (limits['left'] not in dicc) and (limits['right'] in dicc)

def exixtsLimitsNoUpLeft(button, dicc, limits):
	return (limits['up'] not in dicc) and (limits['down'] in dicc) and (limits['left'] not in dicc) and (limits['right'] in dicc)

def exixtsLimitsNoUpRight(button, dicc, limits):
	return (limits['up'] not in dicc) and (limits['down'] in dicc) and (limits['left'] in dicc) and (limits['right'] not in dicc)

def exixtsLimitsNoDownLeft(button, dicc, limits):
	return (limits['up'] in dicc) and (limits['down'] not in dicc) and (limits['left'] not in dicc) and (limits['right'] in dicc)

def exixtsLimitsNoDownRight(button, dicc, limits):
	return (limits['up'] in dicc) and (limits['down'] not in dicc) and (limits['left'] in dicc) and (limits['right'] not in dicc)




def colourUp(dicc, limits):
	return dicc[limits['up']].background_color == [1,0.65,0,1]

def colourDown(dicc, limits):
	return dicc[limits['down']].background_color == [1,0.65,0,1]

def colourLeft(dicc, limits):
	return dicc[limits['left']].background_color == [1,0.65,0,1]

def colourRight(dicc, limits):
	return dicc[limits['right']].background_color == [1,0.65,0,1]

def colourUp2(dicc, limits):
	return (limits['up2'] in dicc) and (dicc[limits['up2']].background_color == [1,0.65,0,1])

def colourDown2(dicc, limits):
	return (limits['down2'] in dicc) and (dicc[limits['down2']].background_color == [1,0.65,0,1])

def colourLeft2(dicc, limits):
	return (limits['left2'] in dicc) and (dicc[limits['left2']].background_color == [1,0.65,0,1])

def colourRight2(dicc, limits):
	return (limits['right2'] in dicc) and (dicc[limits['right2']].background_color == [1,0.65,0,1])






































# def colourLimits(dicc, limits):
# 	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])

# def colourLimitsNoUp(dicc, limits):
# 	return (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])

# def colourLimitsNoDown(dicc, limits):
# 	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])	

# def colourLimitsNoLeft(dicc, limits):
# 	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])

# def colourLimitsNoRight(dicc, limits):
# 	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1])

# def colourLimitsNoUpLeft(dicc, limits):
# 	return (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])

# def colourLimitsNoUpRight(dicc, limits):
# 	return (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1])

# def colourLimitsNoDownLeft(dicc, limits):
# 	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])

# def colourLimitsNoDownRight(dicc, limits):
# 	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1])






def noColourLimitsLessUp(dicc, limits):
	return (dicc[limits['up']].background_color == [1,0.65,0,1]) and (dicc[limits['down']].background_color != [1,0.65,0,1]) and (dicc[limits['left']].background_color != [1,0.65,0,1]) and (dicc[limits['right']].background_color != [1,0.65,0,1])

def noColourLimitsLessDown(dicc, limits):
	return	(dicc[limits['up']].background_color != [1,0.65,0,1]) and (dicc[limits['down']].background_color == [1,0.65,0,1]) and (dicc[limits['left']].background_color != [1,0.65,0,1]) and (dicc[limits['right']].background_color != [1,0.65,0,1])

def noColourLimitsLessLeft(dicc, limits):
	return (dicc[limits['up']].background_color != [1,0.65,0,1]) and (dicc[limits['down']].background_color != [1,0.65,0,1]) and (dicc[limits['left']].background_color == [1,0.65,0,1]) and (dicc[limits['right']].background_color != [1,0.65,0,1])

def noColourLimitsLessRight(dicc, limits):
	return (dicc[limits['up']].background_color != [1,0.65,0,1]) and (dicc[limits['down']].background_color != [1,0.65,0,1]) and (dicc[limits['left']].background_color != [1,0.65,0,1]) and (dicc[limits['right']].background_color == [1,0.65,0,1])	

def colourLimitUp2(dicc, limits):
	return (dicc[limits['up2']].background_color == [1,0.65,0,1])




def generateRandomGame():
	pass
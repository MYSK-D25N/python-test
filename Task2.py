parralels = {'8':["",0],'9':["",0],'10':["",0],'11':["",0]}
subjects = {"Алгебра":["",'',0],"Геометрия":["",'',0]}

with open('math2.txt',"r") as f:
	for i in f:
		s = i.split(" ")
		fullname = s[0] + " " + s[1] 
		grade = s[2]
		points1 = int(s[3])
		points2 = int(s[4])
		points = points1 + points2

		if points > parralels[grade][1]:
			parralels[grade] = [fullname, points]
		elif points == parralels[grade][1]:
			parralels[grade][0] = parralels[grade][0] + ", " + fullname

		if points1 > subjects["Алгебра"][2]:
			subjects["Алгебра"] = [fullname, grade, points1]
		elif points1 == subjects["Алгебра"][2]:
			subjects["Алгебра"] = [subjects["Алгебра"][0]+", "+fullname, subjects["Алгебра"][1]+", "+grade, points1]

		if points2 > subjects["Геометрия"][2]:
			subjects["Геометрия"] = [fullname, grade, points2]
		elif points2 == subjects["Геометрия"][2]:
			subjects["Геометрия"] = [subjects["Геометрия"][0]+", "+fullname, subjects["Геометрия"][1]+", "+grade, points2]


print(parralels)
print(subjects)


import os
def Empty(pth,rmv=False):
	t=os.walk(pth,False)
	while True:
		try:
			l=next(t)
			for x in l[2]:
				os.remove(l[0]+'\\'+x)
			for y in l[1]:
				os.rmdir(l[0]+'\\'+y)
		except:
			break
	if rmv:
		try: os.rmdir(pth)
		except: pass
if __name__=='__main__':
	Empty("C:\\Users\\AISSCE2019\\Desktop\\Arghyadip\\Library Management\\Library",True)
	os.system("python Setup.py py2exe")
	os.rename("C:\\Users\\AISSCE2019\\Desktop\\Arghyadip\\Library Management\\dist","C:\\Users\\AISSCE2019\\Desktop\\Arghyadip\\Library Management\\Library")
	Empty("C:\\Users\\AISSCE2019\\Desktop\\Arghyadip\\Library Management\\build",True)
	os.system("ISCC Setup.iss")

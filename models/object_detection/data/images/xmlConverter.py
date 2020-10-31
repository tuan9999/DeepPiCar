
from os import listdir
from os.path import isfile, join
files_in_dir = [ f for f in listdir('/Users/tuanperera/Documents/autonomous_robot/DeepPiCar/models/object_detection/data/images/test') if isfile(join('/Users/tuanperera/Documents/autonomous_robot/DeepPiCar/models/object_detection/data/images/test',f)) ]

for file in files_in_dir:
	with open(file, 'r+t') as f:
		#print(f.read())
		lst = []
		xmin = ""
		xmax = ""

		for line in f:
			if "<xmin>" in line:
				xmin = line
			elif "<ymin>" in line:
				lst.append(xmin)
				lst.append(line)
			elif "<xmax>" in line:
				xmax = line
			elif "<ymax>" in line:
				lst.append(xmax)
				lst.append(line)
			else:
				lst.append(line)

		f.close()
		f = open(file,'w')
		for line in lst:
			f.write(line)
		f.close()
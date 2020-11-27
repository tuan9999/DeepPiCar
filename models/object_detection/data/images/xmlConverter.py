
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
			if "<xmax>" in line:
				xmax = line
			elif "<ymin>" in line:
				lst.append(line)
				lst.append(xmax)
			elif "<occluded>" in line:
				print(line)
			else:
				lst.append(line)

		f.close()
		f = open(file,'w')
		for line in lst:
			f.write(line)
		f.close()
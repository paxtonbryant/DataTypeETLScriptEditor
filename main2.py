import os, re, sys

files = ['hiea_de.dsx', 'hiea_lab.dsx', 'hiea_depression_demographic.dsx']

for f in files:
	os.makedirs('../../Downloads/Modified', exist_ok=True)
	outfilename = "Modified" +"/" + f + ".modified"
	outfile = open(outfilename, 'w', encoding='latin-1', newline='\r\n')
	sys.stdout = outfile

	with open(f, 'r', encoding='latin-1') as file:
		lines = file.readlines()
		Flag = False
		for index, line in enumerate(lines):
			line = line.rstrip()

	# Here, we are looking for Name fields for the columns EVENT_ID, INSRT_EVNT_ID, and UPDT_EVNT_ID. If we do,
	# then we get ready to edit the field length.
	# If we hit the end of the DSSUBRECORD after we have found the Name record, it's time
	# to reset and ignore
			if re.search("Name \"EVENT_ID\"", line):
				Flag = True
			if re.search('Name \"INSRT_EVNT_ID\"', line):
				Flag = True
			if re.search('Name \"UPDT_EVNT_ID\"', line):
				Flag = True
			if re.search("END DSSUBRECORD", line):
				Flag = False


	# So now, we are looking the fields for the columns EVENT_ID, INSRT_EVNT_ID, and UPDT_EVNT_ID.
	# The flag variable should be set to true when searching withing these fields
	# When the flag is set to true and we find the line Precision "50", we edit to be Precision "250"
			if Flag:
				gen = re.search('[^a-zA-Z0-9]Precision \"\d*\"', line)
				gen2 = re.search('[^a-zA-Z0-9]DisplaySize \"\d*\"', line)
				if gen:
					enc = re.sub('[^a-zA-Z0-9]Precision \"\d*\"', 'Precision \"250\"', line)
					print(enc)
				elif gen2:
					enc = re.sub('[^a-zA-Z0-9]DisplaySize \"\d*\"', 'DisplaySize \"250\"', line)
					print(enc)
				else:
					print(line)

	# If we are not editing the precision we just pass through the line
			else:
				print(line)

	file.close()
	outfile.close()
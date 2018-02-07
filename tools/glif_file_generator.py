
# function to get file body
# formatted as a string, perhaps should use a proper xml lib going forward
def GetBody(x,xStr,y,yStr) :
	z = y-x
	yOffset = 7*x

	# the base attr of the compent element is formated by:
	# if x-y is 0 'line.flat'
	# else 'line.up.z' or 'line.down.z' for z positive or negative
	baseContent = ""
	if z == 0 :
		baseContent = "line.flat"
	elif z > 0 :
		baseContent = "line.up.{}".format(str(z).zfill(3))
	else:
		#flip z to positive for the string formatting
		z = z*-1
		baseContent = "line.down.{}".format(str(z).zfill(3))

	# component differs for yOffset values
	if yOffset == 0 :
		return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><glyph name=\"line.{}.{}\" format=\"1\"><advance width=\"350\"/><outline><component base=\"{}\"/></outline></glyph>".format(xStr,yStr,baseContent)

	return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><glyph name=\"line.{}.{}\" format=\"1\"><advance width=\"350\"/><outline><component base=\"{}\" yOffset=\"{}\"/></outline></glyph>".format(xStr,yStr,baseContent,yOffset)

for x in range(0,101) : #change me to (0,101)
	for y in range(0,101) : #change me to (0,101)
		# create the filename
		xStr = str(x).zfill(3)
		yStr = str(y).zfill(3)
		fileName = 'line.{}.{}.glif'.format(xStr, yStr)

		# create the file
		f = open(fileName, "w+")
		f.write(GetBody(x,xStr,y,yStr))
		f.close()

		print 'file {} created'.format(fileName)

import os

for path, subdirs, files in os.walk("uploads"):
	a = open("successful.html", "w")
	a.write("<html><body><center>")
	a.write("<h1> List of Submitted Files</h1>")
	for filename in files:
		f = os.path.join(path, filename)
		a.write("<br>")
		a.write(str(filename))
a.write("</center></body></html>")
a.close()   

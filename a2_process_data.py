#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

tableheads = "\n\t\t\t\t\t"
for i in range(len(contents[0])):
	tableheads = tableheads + "<th>" +contents[0][i] + "</th>" + "\n\t\t\t\t\t"
	##tableheads.append( "<th>" + contents[0][i] + "</th>" + "\n")
tableheads = tableheads[:tableheads.rfind('\t')]

tabledata = "\n\t\t\t\t"
flag1 = True
for row in contents:
	if(flag1):
		flag1 = False
		continue
	tabledata = tabledata + "<tr>"
	for cell in row:
		tabledata = tabledata + "\n\t\t\t\t\t" + "<td>" + cell + "</td>"
	tabledata = tabledata + "\n\t\t\t\t" + "</tr>" + "\n\t\t\t\t"

def htmlpage():
    htmltext = """
<!DOCTYPE html>

<html lang="en">
<head>
	<title>Player Statistics</title>
	<meta charset="UTF-8" />
	<link rel="stylesheet" type="text/css" href="webfiles/stylesheet.css" />
	<link href = "webfiles/icon.png" rel="icon" type="image/png">
	<script src="webfiles/sorttable.js"></script>
</head>
<body>
	<div class="banner">
		<h1>Player Statistics</h1>
	</div>

	<section class="content">
		<h2>Statistics Of Professional Dota2 Players</h2>
		<p>Let's analyse the statistics of Dota2 player's official matches. The data got collected from <a href="https://www.datdota.com/" target="_blank">datdota</a>. To make the data recent and relevant following criterias are used.
		<ul>
			<li>Patch 7.00 and after</li>
			<li>Players with minimum 35 matches</li>
			<li>Professional or premium matches(aka matches that actually matters)</li>
		</ul>
		</p>
	</section>
	<section class="c2">
		<h2>The Data: </h2>
		<div class="grid">
			<table>
				<tr>"""+tableheads+"""</tr>"""+tabledata+"""	
		</table>
	</div>		
</body>
</html>
"""
    return htmltext

fileptr = open("a2_output.html","w")
print(htmlpage(), file=fileptr)
fileptr.close()
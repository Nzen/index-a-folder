'''
<!DOCTYPE html5>
<html language='en'>
<head>
	<meta charset="UTF-8"></meta>
	<title> [this folder name] </title>
	<link rel="stylesheet" href="basic.css">
</head>
<body>
	<p>
		<h2> [subfolder name] </h2>
		<ul>
			<li> [file name] </li>
		</ul>
	</p>
</body>
</html>
'''

import os

def folder_name( here ) :
	segment = here.split( '\\' )
	if len( segment[0] ) == len( here ) :
		segment = here.split( '/' ) # a small concession to _nix file slash
	return segment[ -1 ] # last one is this folder

def fill_with_subfolders( output, here ) :
	f_depth = 2
	curr_file = "basic I/O, world"
	begin_folder = "\n\t<p>"
	mid_folder = "\n\t\t <ul>"
	end_folder = "\t\t </ul>\n\t</p>\n"
	
	for directory_tuple in os.walk( here, False ) : # top dir, start from bottom?
		current_f = directory_tuple[0]
		if current_f == here :
			return
		output.write( begin_folder )
		output.write( "\n\t\t<h"+str(f_depth)+">" + folder_name(current_f) + "</h"+str(f_depth)+">" )
		output.write( mid_folder )
		output.write( "\n\t\t\t<li>" + curr_file + "</li>\n" )
		output.write( end_folder )
		

def main() :
	begin_htm = "<!DOCTYPE html5>\n<html language='en'>\n<head>\n\t<meta charset=\"UTF-8\"></meta>\n\t<title>"
	mid_htm = "</title>\n\t<link rel=\"stylesheet\" href=\"basic.css\">\n</head>\n"
	mid_htm +=		"<body>\n  <div class=\"twenty_p\">\n"
	mid_htm +=		"<p>&emsp;</p>\n\n" * 10
	mid_htm +=		"</div><div class=\"content\">"
	end_htm = "\n  </div>\n</body>\n</html>"

	'''
	make a file
	put in begin, get foldername, put in mid
	walk the structure, output the subfolders in their own paragraph
	put in end
	close the file
	'''
	here = os.getcwd()
	output = open( "index.htm", 'w' )
	output.write( begin_htm )
	curr = folder_name( here )
	output.write( curr ) # current folder is the title ; later get just the end
	output.write( mid_htm )
	output.write( "\n<h1>" + curr + "</h1>" )
	fill_with_subfolders( output, here )
	output.write( end_htm )
	output.close()

main()
'''
	the_files = "\\*"
	for directory_tuple in os.walk( here, False ) : # top dir, start from bottom?
		current = directory_tuple[0]
		# well, one problem is the spaces aren't being eaten like I expect :\
		if current == here :
			return
		for_bash = command + '\"' + current + the_files + '\"'
'''
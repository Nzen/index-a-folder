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

def just_last( here ) :
	segment = here.split( '\\' )
	if len( segment[0] ) == len( here ) :
		segment = here.split( '/' ) # a small concession to _nix file slash
	return segment[ -1 ] # last one is the goal

def just_name( file_w_ext ) :
	segment = file_w_ext.split( '.' )
	return segment[ 0 ]

def fill_with_files( output, files, here ) :
	for curr_file in files :
		output.write( "\n\t\t\t<li> <a href=\""+here+"\\"+curr_file+"\">"+just_name(curr_file)+"</a> </li>\n" )
		# make these links, yay!

def fill_with_subfolders( output, here ) :
	f_depth = 2
	begin_folder = "\n\t<p>"
	mid_folder = "\n\t\t <ul>"
	end_folder = "\t\t </ul>\n\t</p>\n"
	
	for directory_tuple in os.walk( here, False ) : # top dir, start from bottom?
		current_f = directory_tuple[0]
		if current_f == here :
			return
		output.write( begin_folder )
		output.write( "\n\t\t<h"+str(f_depth)+">" + just_last(current_f) + "</h"+str(f_depth)+">" )
		output.write( mid_folder )
		fill_with_files( output, directory_tuple[2], just_last(current_f) ) # FIX assumption, only one folder deep
		output.write( end_folder )
		

def main() :
	begin_htm = "<!DOCTYPE html5>\n<html language='en'>\n<head>\n\t<meta charset=\"UTF-8\"></meta>\n\t<title>"
	mid_htm = "</title>\n\t<link rel=\"stylesheet\" href=\"basic.css\">\n</head>\n"
	mid_htm +=		"<body>\n  <div class=\"twenty_p\">\n"
	mid_htm +=		"<p>&emsp;</p>\n\n" * 10
	mid_htm +=		"</div><div class=\"content\">"
	end_htm = "\n  </div>\n</body>\n</html>"

	here = os.getcwd()
	output = open( "index.htm", 'w' )
	output.write( begin_htm )
	curr = just_last( here )
	output.write( curr ) # current folder is the title ; later get just the end
	output.write( mid_htm )
	output.write( "\n<h1>" + curr + "</h1>" )
	#
	fill_with_subfolders( output, here )
	output.write( end_htm )
	output.close()

main()

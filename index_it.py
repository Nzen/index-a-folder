'''
Author: Nicholas Prado - Nzen
License: MIT
Purpose: Outputs an html index of the folders it is run within.
'''

import os

def just_last( here ) :
	""" Splits final folder name from c:/one/two/last """
	segment = here.split( '\\' )
	if len( segment[0] ) == len( here ) :
		segment = here.split( '/' ) # a small concession to _nix file slash
	return segment[ -1 ] # last one is the goal

def just_name( file_w_ext ) :
	""" Splits file name from its extension, assuming single period """
	segment = file_w_ext.split( '.' )
	return segment[ 0 ]

def fill_with_files( output, files, here, cut_ind ) :
	""" writes <a> with relative path and file name """
	for curr_file in files :
		rel_path = here[ cut_ind+1: ]
		output.write( "\n\t\t\t<li> <a href=\""+rel_path+"\\"+curr_file+"\">"+just_name(curr_file)+"</a> </li>\n" )

def fill_with_subfolders( output, here ) :
	""" walks the tree, writing the subfolder names in <h_> and files in an <ul> """
	begin_folder = "\n\t<p>"
	mid_folder = "\n\t\t <ul>"
	end_folder = "\t\t </ul>\n\t</p>\n"
	for directory_tuple in os.walk( here, True ) : # top dir
		if len(directory_tuple[2]) <= 0 : # ignore empty folders
			continue
		current_f = directory_tuple[0]
		#if current_f.find("ui source")>=0 : # a folder you don't need to traverse
		#	continue
		output.write( begin_folder )
		rel_path = directory_tuple[0][ len(here)+1: ]
		h_tag = rel_path.count( "\\" ) + 1
		output.write( "\n\t\t<h"+str(h_tag)+">" + rel_path + "</h"+str(h_tag)+">" )
		output.write( mid_folder )
		fill_with_files( output, directory_tuple[2], directory_tuple[0], len(here) )
		output.write( end_folder )
		

def main() :
	""" writes the surrounding html template for the page """
	begin_htm = "<!DOCTYPE html>\n<html language='en'>\n<head>\n\t<meta charset=\"UTF-8\"></meta>\n\t<title>"
	mid_htm = "</title>\n\t<link rel=\"stylesheet\" href=\"basic.css\">\n</head>\n"
	mid_htm +=		"<body>\n  <div class=\"twenty_p\">\n"
	mid_htm +=		"<p>&emsp;</p>\n</div><div class=\"content\">"
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

'''
	OUTPUT : index.htm

<!DOCTYPE html5>
<html language='en'>
<head>
	<meta charset="UTF-8"></meta>
	<title> [this folder name] </title>
	<link rel="stylesheet" href="basic.css">
</head>
<body>
	<p>
		<h_> [subfolder name] </h_>  # '_' is the folder depth
		<ul>
			<li> [file name] </li>
		</ul>
	</p>
</body>
</html>
'''

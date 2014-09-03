'''
<!DOCTYPE html>
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

def fill_with_subfolders( output, here ) :
	output.write( "\t<p>basic I/O, world</p>" )

def main() :
	begin_htm = "<!DOCTYPE html>\n<html language='en'>\n<head>\n\t<meta charset=\"UTF-8\"></meta>\n\t<title>"
	mid_htm = "</title>\n\t<link rel=\"stylesheet\" href=\"basic.css\">\n</head>\n<body>\n"
	end_htm = "</body>\n</html>"

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
	output.write( here ) # current folder is the title ; later get just the end
	output.write( mid_htm )
	fill_with_subfolders( output, here )
	output.write( end_htm )
	output.close()

	'''
	for directory_tuple in os.walk( here, False ) : # top dir, start from bottom?
		if current == here :
			return'''

main()
'''
	newFileName = originalFileName[ : -3 ] + "asm" # replaces .txt or similar
	output = open( newFileName, 'w' )
	output.truncate( ) # erase what's in there for safety
	for nn in self.smlData :
		output.write( str( nn ) + '\n' ) # consider outputting as a grid, as in showMem()?
	output.close( )
	return newFileName

	command = "sdelete.exe "# or "echo " for testing
	folder_flag = "-r "
	here = os.getcwd()
	the_files = "\\*"
	current = ""
	for_bash = ""
	for directory_tuple in os.walk( here, False ) : # top dir, start from bottom?
		current = directory_tuple[0]
		# well, one problem is the spaces aren't being eaten like I expect :\
		if current == here :
			return
		for_bash = command + '\"' + current + the_files + '\"'
		os.system( for_bash )
		for_bash = command + '\"' + current + '\"'
		os.system( for_bash )
'''
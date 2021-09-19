def createColor(code):
	# Make the function for the colour
	def color(txt):
		# Format the escape character template with the ANSI code
		ansi = '\x1b[{}m{}\x1b[0m'
		return ansi.format(code, txt)
	return color

red = createColor(31)
green = createColor(32)
cyan = createColor(36)

bold = createColor(1)
underline = createColor(4)

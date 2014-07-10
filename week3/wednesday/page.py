def div(content):
	return "<div>%s</div>" % content

def page():
	header = "Demo"
	footer = "(c)2014"
	content = """
<strong>this</strong>
is
my
<em>content</em>
"""

	return header + content + div(footer)



print page()

"""A class for holding data of HTML tags. """
class Element:
	tag=""
	attr={}
	text=""
	children=[]
	css={}
	indent='    '
	def __init__(self,tag="",attr={},children=[],text=""):
		self.tag=tag
		self.attr=attr
		self.children=children

		if (tag or children) and text:
		 	raise Exception("Setting text and tag name in the constructor at the same time is not allow")
		self.text=text

	#adds a child to the current tag
	def add_child(self,ele):
		self.children=self.children+[ele]

	#add text to the current tag - create a text element , and add it to the children list of the current object
	def set_text(self, text):
	 	e = Element(text=text)
	 	self.children=self.children+[e]
		pass
	#set the attributes of the current tag
	def set_attribute(self, key,val):
		self.attr[key]=val
	#set the id of the current tag
	def set_id(self,id):
		self.attr["id"]=id
	#print out the tree as string - output the tree to html
	def to_string(self,level=0):
		if not self.tag:
			return Element.indent*level+self.text+"\n"
		else:
			lst=[Element.indent*level]

			lst.append("<"+self.tag)

			for k,v in self.attr.items():
				lst.append(" "+k+'="'+v+'" ')

			lst.append(">\n")

			for chd in self.children:
				lst.append(chd.to_string(level+1))

			lst.append(Element.indent*level)
			lst.append("</"+self.tag+">\n")
		return "".join(lst)
	


#testing code
if __name__=="__main__":
	c = Element("div")
	c2 = Element("p")

	c2.set_text("Hay!!")
	c.add_child(c2)
	#print(c2.children)

	tree=Element("html",attr={"href":"http://google.com",},children=[c])

	print(tree.to_string())



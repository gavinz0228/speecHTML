class Element:
	tag=""
	attr={}
	text=""
	children=[]
	css={}
	indent='\t'
	def __init__(self,tag="",attr={},children=[],text=""):
		self.tag=tag
		self.attr=attr
		self.children=children

		# if (tag or children) and text:
		# 	raise Exception("sdfsdf")
		self.text=text

	def addChild(self,ele):

		self.children=self.children+[ele]
		pass

	def setText(self, text):
	 	e = Element(text=text)
	 	self.children=self.children+[e]
		pass

	def setAttribute(self, key,val):
		self.attr[key]=val

	def setId(self,id):
		self.attr["id"]=id
	
	def toString(self,level=0):
		if not self.tag:
			return self.indent*level+self.text+"\n"
		else:
			lst=[self.indent*level]

			lst.append("<"+self.tag)

			for k,v in self.attr.items():
				lst.append(" "+k+'="'+v+'" ')

			lst.append(">\n")
			# print(self.children[0].children[0].children[0].children[0].children[0].children[0].children[0].tag)
			#print(len(self.children))
			for chd in self.children:
				lst.append(chd.toString(level+1))

			lst.append(self.indent*level)
			lst.append("</"+self.tag+">\n")
		return "".join(lst)
	



c = Element("div")
c2 = Element("p")

c2.setText("Hay!!")
c.addChild(c2)
#print(c2.children)

tree=Element("html",attr={"href":"http://google.com",},children=[c])

print(tree.toString())



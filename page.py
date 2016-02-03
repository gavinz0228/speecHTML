from element import *
class Page:
	#member variable
	page=None
	title=None
	head=None
	body=None
	#static variables
	default_title="untitile"
	def __init__(self):
		self.title=Element("title")
		self.title.set_text(Page.default_title)
		self.head=Element(tag="head",children=[self.title])
		self.body=Element(tag="body")
		self.page=Element(tag="html", children=[self.head,self.body])

	def export(self):
		return self.page.to_string()

	def add_div(self,id,parent=None):
		pass
	def delete_div(self,id):
		pass
	def set_attr(self,id,akey,aval):
		pass
	
	#implement something to get element by id - use dictionary

if "__main__"==__name__:
	print(Page().export())

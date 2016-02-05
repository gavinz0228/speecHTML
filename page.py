from element import *
class Page:
	#member variable
	root=None
	title=None
	head=None
	body=None
	#static variables
	default_title="untitile"
	def __init__(self,title=default_title):

		self.root = Element(tag="html")


		self.head = Element(tag="head",parent=self.root)

		self.title = Element("title",parent=self.head)
		self.title.add_text(title)

		self.body = Element(tag="body",parent=self.root)

		self.head.add_child(self.title)
		self.root.add_child(self.head)
		self.root.add_child(self.body)


	def export(self):
		return self.root.to_string()



	def add_div(self,id,parent=None):
		pass
	def delete_div(self,id):
		pass
	def set_attr(self,id,akey,aval):
		pass


#class["class_name"]=[ele1,ele2]
#id["id_name"]=ele1

	#implement something to get element by id - use dictionary

if "__main__"==__name__:
	print(Page().export())

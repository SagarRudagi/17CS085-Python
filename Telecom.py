class CallDetail:
	def __init__(self,lst):
		self.dailer = lst[0]
		self.recipient = lst[1]
		self.duration = lst[2]
		self.type = lst[3]

class Util:
	def __init__(self):
		self.object_list = None

	def parse_customer(self,string_list):
		temp_lst = []
		for i in string_list:
			i = i.split(",")
			temp_lst.append(CallDetail(i))
		object_list = temp_lst
		print(object_list)


call = "111,222,10,STD"
call2 = "333,444,20,ISD"
string_list = [call,call2]
Util().parse_customer(string_list)






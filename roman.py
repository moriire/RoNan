import re
forbidden=()
ro=["I", "V", "X", "L", "C", "M"]
specials=["IV", "IX", "XL","XC"]
man=(1,5,10,50,100,1000, 4, 9,40,90)

class Roman:
	def __init__(self, numeral):
		self.numeral=numeral
	
	def __dict__(self):
		roman=zip(ro+specials, man)
		return dict(roman)

	def __combo(self):
		self.A=[]
		self.B=list(self.numeral)
		for special in specials:
			ss=re.search(special, self.numeral)
			if ss:
				self.A.append(special)
				for i in special:
					self.B.remove(i)
		return self.A+self.B
	
	def __list__(self):
		return [self.__dict__()[i] for i in self.__combo()]
		
	def __int__(self):
		return sum(self.__list__())	
		
	def value(self):
		return self.__int__()
		
		
x=Roman("CXIV")
y=x.value()
print(y)
		
if __name__=="__main__":
	x=Roman("CXIV")
	print(type(x))
		
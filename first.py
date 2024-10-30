
class Person:
 def __init__(self, name, surname):
  self.name =name
  self.surname =surname
print("------------------------------")


print("------------------------------")

class EUCitizen(Person):
	recordNum=0
	
	def __init__(self,name,surname,nationality):
		 super().__init__( name,surname)
		 self.name=name
		 self.surname=surname
		 self.nationality=nationality
		 EUCitizen.recordNum+=1
	     		 	  
     
		 
print("--------------------------------------------")

print("The value of our class variable before creating the first EUCitizen object is  %d"%(EUCitizen.recordNum))

c1= EUCitizen("katt","Papa","spanish")
print("The value of our class variable after creating the first EUCitizen object is  %d"%(EUCitizen.recordNum))

c2= EUCitizen("katt","Papa","spanish")
print("The value of our class variable after creating the second  EUCitizen object is  %d"%(EUCitizen.recordNum))




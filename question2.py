class Person:
	pass

class Student(Person):
	def __init__(self, obj_name, obj_id):
		self.obj_name = obj_name
		self.obj_id = obj_id
	def properties(self):
		print(self.obj_name)
		print(self.obj_id)


print("Question 2\n")
student = Student("this is a name", "this is an id")
student.properties()
print("\n")


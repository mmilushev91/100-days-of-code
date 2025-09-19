#class declaration
#class is a blueprint for creating objects
#class name is always in PascalCase
class User:
  #constructor method is a special method that is called when an object is created
  def __init__(self, user_id, username):
    #attributes are variables that belong to a class
    #self is a reference to the current instance of the class
    #properties names should be the same as the parameter names, but it's not a     requirement
    self.id = user_id
    self.username = username
    #default value for followers to all instances of the class
    self.followers = 0
    self.following = 0

  #method is a function that belongs to a class
  #self is a reference to the current instance of the class
  def follow(self, user):
    user.followers += 1
    self.following += 1


#object is an instance of a class
#instantiation of an object user_1 from the class User
user_1 = User("001", "angela")

#manually adding attributes to the object
user_1.id = "001"
user_1.username = "angela"

print(user_1.id)
print(user_1.username)

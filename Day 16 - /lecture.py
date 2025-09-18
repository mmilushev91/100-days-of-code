"""The procedural approach in programming is a paradigm that structures code into a series of
step-by-step instructions or procedures. It emphasizes a top-down design, where tasks are broken into smaller, 
reusable functions or routines, making it easier to manage and understand. This approach is foundational for

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects,
which are instances of classes. These objects encapsulate data (attributes) and behavior (methods),
enabling modular, reusable, and maintainable code.

Key Concepts of OOP

Classes and Objects: A class is a blueprint for creating objects, defining their attributes and methods.
For example, a Car class might define properties like color and speed and methods like drive() or brake(). 
An object is an instance of a class. For example, myCar = Car() creates an object myCar with specific attributes
and behaviors.

Encapsulation: Encapsulation involves bundling data and methods within an object and restricting direct access 
to some components. This ensures data hiding and protects the integrity of the object.

Inheritance: Inheritance allows a class (child) to derive properties and methods from another class (parent). 
For instance, a SportsCar class can inherit from a Car class and add unique features like turboBoost().

Polymorphism: Polymorphism enables objects to take on multiple forms. For example, a draw() method
might behave differently for Circle and Rectangle objects, even though both inherit from a common Shape class.

Abstraction: Abstraction hides complex implementation details and exposes only essential features. 
For example, a Car class might provide a start() method without revealing the internal workings of the engine.
"""

from turtle import Turtle 

timmy = Turtle()
print(timmy)

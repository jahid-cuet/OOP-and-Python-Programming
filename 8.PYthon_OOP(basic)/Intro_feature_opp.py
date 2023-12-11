"""What does mean by OOp?
Object-oriented programming (OOP) is a programming paradigm based on the concept of objects,
which can contain data and code: data in the form of fields (often known as attributes or properties), 
and code in the form of procedures (often known as methods)."""

The feature or pillar of OOP->
""" 
#(1)Encapsulation ->
 prevents external code from being concerned with the internal workings of an object. 
This facilitates code refactoring, for example allowing the author of the class to change how objects of that 
class represent their data internally without changing any external code (as long as "public" method calls work the same way). 
It also encourages programmers to put all the code that is concerned with a certain set of data in the same class,
 which organizes it for easy comprehension by other programmers. Encapsulation is a technique that encourages decoupling.

#(2)Composition, inheritance, and delegation
Objects can contain other objects in their instance variables; this is known as object composition. For example, an object in the Employee class might contain (either directly or through a pointer) an object in the Address class, in addition to its own instance variables like "first_name" and "position". Object composition is used to represent "has-a" relationships: every employee has an address, so every Employee object has access to a place to store an Address object (either directly embedded within itself, or at a separate location addressed via a pointer).

Languages that support classes almost always support inheritance. This allows classes to be arranged in a hierarchy that represents "is-a-type-of" relationships. For example, class Employee might inherit from class Person. All the data and methods available to the parent class also appear in the child class with the same names. For example, class Person might define variables "first_name" and "last_name" with method "make_full_name()". These will also be available in class Employee, which might add the variables "position" and "salary". This technique allows easy re-use of the same procedures and data definitions, in addition to potentially mirroring real-world relationships in an intuitive way. Rather than utilizing database tables and programming subroutines, the developer utilizes objects the user may be more familiar with: objects from their application domain.[27]

Subclasses can override the methods defined by superclasses. Multiple inheritance is allowed in some languages, though this can make resolving overrides complicated. Some languages have special support for mixins, though in any language with multiple inheritance, a mixin is simply a class that does not represent an is-a-type-of relationship. Mixins are typically used to add the same methods to multiple classes. For example, class UnicodeConversionMixin might provide a method unicode_to_ascii() when included in class FileReader and class WebPageScraper, which do not share a common parent.

Abstract classes cannot be instantiated into objects; they exist only for the purpose of inheritance into other "concrete" classes that can be instantiated. In Java, the final keyword can be used to prevent a class from being subclassed.[28]

The doctrine of composition over inheritance advocates implementing has-a relationships using composition instead of inheritance. For example, instead of inheriting from class Person, class Employee could give each Employee object an internal Person object, which it then has the opportunity to hide from external code even if class Person has many public attributes or methods. Some languages, like Go do not support inheritance at all.

The "open/closed principle" advocates that classes and functions "should be open for extension, but closed for modification".

Delegation is another language feature that can be used as an alternative to inheritance.

#(3)Polymorphism->

Subtyping – a form of polymorphism – is when calling code can be independent of which class in the supported hierarchy it is operating on – 
the parent class or one of its descendants. Meanwhile, the same operation name among objects in an inheritance hierarchy may behave differently.

For example, objects of type Circle and Square are derived from a common class called Shape.
 The Draw function for each type of Shape implements what is necessary to draw itself while calling code 
 can remain indifferent to the particular type of Shape being drawn.
This is another type of abstraction that simplifies code external to the
 class hierarchy and enables strong separation of concerns.
 
 #(4)Abstraction->
 Abstraction is the process of hiding the internal details of an application from the outer world. 
 Abstraction is used to describe things in simple terms. 
 It’s used to create a boundary between the application and the client programs.
 
 
 """

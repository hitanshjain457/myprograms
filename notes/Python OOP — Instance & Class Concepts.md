# Python OOP — Instance & Class Concepts

> Beginner → Intermediate Notes  
> **Topics:** Instance Variable, Instance Method, Class Variable, Class Method, Static Method

---

## 1. Instance Variable

### Definition

Jo variable **har object ka apna alag data store** kare, usse **Instance Variable** bolte hain.

Usually Instance Variable ko `self` ke through banate hain.

### Easy Rule

**Object-specific data = Instance Variable**

### Examples

| Class | Instance Variables |
|---|---|
| `Student` | `name`, `age`, `marks` |
| `Car` | `color`, `model`, `speed` |
| `Employee` | `name`, `salary`, `department` |

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Yahan:

```python
self.name
self.age
```

Instance Variables hain.

Agar:

```python
s1 = Student("Rahul", 20)
s2 = Student("Amit", 22)
```

to:

```text
s1.name → Rahul
s2.name → Amit
```

Dono objects ka `name` alag hai.

---

# 2. Instance Method

### Definition

Jo method **object ke data ke saath kaam** kare, use **Instance Method** bolte hain.

Instance Method ka first parameter normally:

```python
self
```

hota hai.

### `self` kya represent karta hai?

`self` **current object** ko represent karta hai.

### Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Rahul", 80)
s1.show()
```

Yahan:

```python
show()
```

→ Instance Method hai.

Aur:

```python
self.name
self.marks
```

→ Instance Variables hain.

### Easy Rule

**Instance Method → Object ke data par kaam**

---

# 3. Class Variable

Instance Variable har object ka **alag** hota hai.

Lekin agar koi value **sab objects ke liye common** hai, to **Class Variable** use kar sakte hain.

### Example

```python
class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Yahan:

```python
school = "ABC School"
```

→ Class Variable hai.

Aur:

```python
self.name
self.age
```

→ Instance Variables hain.

---

## Instance Variable vs Class Variable

| Instance Variable | Class Variable |
|---|---|
| Object-specific | Class-level/common |
| Usually `self.x` | Usually `ClassName.x` |
| Har object ki separate value | Common value |
| `name`, `age` | `school` |

### Example

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


s1 = Student("Rahul")
s2 = Student("Amit")

print(s1.name)
print(s2.name)

print(Student.school)
```

Output:

```text
Rahul
Amit
ABC School
```

---

## Important Note

Class Variable ko **object se bhi access** kar sakte hain.

```python
class Student:
    school = "ABC School"


s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)
print(Student.school)
```

Output:

```text
ABC School
ABC School
ABC School
```

### Best Practice

Class Variable ko access karne ke liye generally:

```python
Student.school
```

use karna clearer hota hai.

---

# 4. Class Method

### Definition

Class Method wo method hai jo **class ke data ke saath kaam** karta hai.

Isme `self` nahi hota.

Iska first parameter hota hai:

```python
cls
```

Class Method banane ke liye:

```python
@classmethod
```

decorator lagate hain.

---

## Example

```python
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


Student.change_school("XYZ School")

print(Student.school)
```

Output:

```text
XYZ School
```

Yahan:

```python
cls.school
```

class variable ko access/change kar raha hai.

---

# 5. `self` vs `cls`

Ye bahut important hai:

| Parameter | Represents |
|---|---|
| `self` | Current Object |
| `cls` | Current Class |

### Yaad rakhne ka simple trick

```text
self → object
cls  → class
```

---

# 6. Class Method — Complete Example

```python
class Employee:
    company = "ABC Pvt Ltd"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Rahul")
e2 = Employee("Amit")

print(e1.company)
print(e2.company)

Employee.change_company("XYZ Pvt Ltd")

print(e1.company)
print(e2.company)
```

Output:

```text
ABC Pvt Ltd
ABC Pvt Ltd
XYZ Pvt Ltd
XYZ Pvt Ltd
```

### Kya hua?

Initially:

```text
company = ABC Pvt Ltd
```

Class Method call kiya:

```python
Employee.change_company("XYZ Pvt Ltd")
```

To class variable change ho gaya:

```text
company = XYZ Pvt Ltd
```

Isliye dono objects ko updated value mil gayi.

---

# 7. Static Method

### Definition

Static Method aisa method hota hai jo **object ke data ya class ke data par directly depend nahi karta**.

Ye basically class ke andar rakhi hui **independent utility/logic** hoti hai.

Static Method banane ke liye:

```python
@staticmethod
```

decorator use karte hain.

Isme normally:

```text
self → nahi
cls  → nahi
```

hota.

---

## Example

```python
class Student:

    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100


print(Student.is_valid_marks(80))
print(Student.is_valid_marks(120))
```

Output:

```text
True
False
```

Yahan method ko:

- `self` ki zarurat nahi
- `cls` ki zarurat nahi
- kisi object ke data ki zarurat nahi

Bas `marks` input leta hai aur result return karta hai.

---

# 8. Instance Method vs Class Method vs Static Method

| Type | First Parameter | Kis par kaam karta hai? | Decorator |
|---|---|---|---|
| Instance Method | `self` | Object data | None |
| Class Method | `cls` | Class data | `@classmethod` |
| Static Method | Nothing required | Independent logic | `@staticmethod` |

### Super Easy Rule

```text
self → Object
cls  → Class
nothing → Independent logic
```

---

# 9. Complete Example — All Concepts Together

```python
class Student:

    # Class Variable
    school = "ABC School"

    # Constructor
    def __init__(self, name, marks):

        # Instance Variables
        self.name = name
        self.marks = marks

    # Instance Method
    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Class Method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static Method
    @staticmethod
    def is_valid_marks(marks):
        return 0 <= marks <= 100


# Object
s1 = Student("Rahul", 80)

# Instance Method
s1.show()

# Class Method
Student.change_school("XYZ School")

print(Student.school)

# Static Method
print(Student.is_valid_marks(80))
```

---

## Code mein kya kya hai?

### Instance Variables

```python
self.name
self.marks
```

→ Object-specific data

---

### Instance Method

```python
show()
```

→ Object ke data par kaam karta hai.

---

### Class Variable

```python
school
```

→ Sab students ke liye common data.

---

### Class Method

```python
change_school()
```

→ Class variable ko change karta hai.

---

### Static Method

```python
is_valid_marks()
```

→ Independent validation/utility logic.

---

# 10. One Example to Understand Everything

Imagine karo ek **school** hai.

```text
Student
   |
   |-- name       → har student ka alag
   |-- marks      → har student ke alag
   |
   |-- school     → sabka common
```

So:

```text
name, marks
    ↓
Instance Variables

school
    ↓
Class Variable
```

Methods:

```text
Student ka data show karna
        ↓
Instance Method

School ka naam change karna
        ↓
Class Method

Marks valid hain ya nahi check karna
        ↓
Static Method
```

---

# 11. Real-Life Analogy

Suppose:

```python
class Employee:
```

### Instance Variable

Har employee ka:

```text
name
salary
age
department
```

alag ho sakta hai.

→ **Instance Variable**

### Class Variable

Company ka naam:

```text
ABC Pvt Ltd
```

sab employees ke liye same hai.

→ **Class Variable**

### Instance Method

Employee ki salary ya name display karna:

```python
employee.show_details()
```

→ **Instance Method**

### Class Method

Company ka naam change karna:

```python
Employee.change_company(...)
```

→ **Class Method**

### Static Method

Salary valid hai ya nahi check karna:

```python
Employee.is_valid_salary(...)
```

→ **Static Method**

---

# 12. Sabse Easy Way to Remember

## Variables

```text
INSTANCE
   ↓
Object ki cheez

CLASS
   ↓
Sab objects ki common cheez
```

## Methods

```text
INSTANCE METHOD
   ↓
Object ke data par kaam

CLASS METHOD
   ↓
Class ke data par kaam

STATIC METHOD
   ↓
Independent utility / logic
```

## Parameters

```text
self
 ↓
Current Object

cls
 ↓
Current Class

nothing
 ↓
Static / Independent Logic
```

---

# 13. Interview-Style Questions

### Q1. Instance Variable kya hota hai?

**Answer:**  
A variable that stores data specific to an individual object is called an Instance Variable. It is usually created using `self`.

---

### Q2. Class Variable kya hota hai?

**Answer:**  
A variable shared by all objects of a class is called a Class Variable.

Example:

```python
class Student:
    school = "ABC School"
```

---

### Q3. `self` kya hai?

**Answer:**  
`self` current object ko represent karta hai.

---

### Q4. `cls` kya hai?

**Answer:**  
`cls` current class ko represent karta hai aur Class Method mein use hota hai.

---

### Q5. Class Method kaise banate hain?

```python
@classmethod
def method_name(cls):
    pass
```

---

### Q6. Static Method kaise banate hain?

```python
@staticmethod
def method_name():
    pass
```

---

# 14. Quick Revision Table

| Concept | Meaning | Example |
|---|---|---|
| Instance Variable | Object ka apna data | `self.name` |
| Instance Method | Object ke data par kaam | `show()` |
| Class Variable | Sab objects ka common data | `school` |
| Class Method | Class ke data par kaam | `change_school()` |
| Static Method | Independent utility logic | `is_valid_marks()` |
| `self` | Current object | `self.name` |
| `cls` | Current class | `cls.school` |

---

# 15. Final Memory Trick 🧠

Bas ye 5 lines yaad rakho:

```text
Instance Variable → Object ka data

Instance Method → Object ke data par kaam

Class Variable → Sab objects ka common data

Class Method → Class ke data par kaam

Static Method → Independent logic
```

Aur:

```text
self → Object
cls  → Class
nothing → Static
```

> **Golden Rule:**  
> Agar question mein poocha jaye **"kis ka data?"** → Object ya Class identify karo.  
> Agar poocha jaye **"kis par kaam?"** → Instance Method, Class Method ya Static Method identify karo.

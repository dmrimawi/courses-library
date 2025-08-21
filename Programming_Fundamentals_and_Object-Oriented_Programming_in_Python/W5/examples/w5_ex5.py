class A:
    def method2(self):
        print("Method from A")

class B(A):
    def method1(self):
        print("Method from B")

class C:
    def method(self):
        print("Method from C")

class D(B, C):
    def method(self):
        super().method() 
        print("Method from D")

# Usage
d = D()
d.method()

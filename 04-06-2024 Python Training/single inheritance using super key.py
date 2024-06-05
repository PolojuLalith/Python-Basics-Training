class parent:
    def func1(self):
        print("this is func1")
class child(parent):
    def func2(self):
        super().func1()
        print("this is func2")
ob=child()
ob.func2()
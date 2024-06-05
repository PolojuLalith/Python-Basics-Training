class Test:
    def __init__(self):
        self.x=0
class derived_test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y=1
def main():
    b=derived_test()
    print(b.x,b.y)
main()

# single_ == protected
#  double__ == private
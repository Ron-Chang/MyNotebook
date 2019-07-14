from datetime import date

class Foo:

    today = date.today()

    # 屬性默認為類屬性（可以給直接被類本身調用）
    y = today.year
    m = today.month
    d = today.day

    my_name = "Ronhsien Chang"

    def __init__(self, name, register_y=y, register_m=m, register_d=d):

        self.name = name;
        self.newBirthY = register_y;
        self.newBirthM = register_m;
        self.newBirthD = register_d;

    def __repr__(self):
        print("repr")
        return self.name

    def __str__(self):
        print("str")
        return self.name

    # 實例化方法（必須實例化類之後才能被調用）
    def myBirth(self): # self : 表示實例化類後的地址id
        print(f"{self.name}`s birthday is {self.newBirthY}/{self.newBirthM}/{self.newBirthD}")
        # print(self)

    # 類方法（不需要實例化類就可以被類本身調用）
    @classmethod
    def ronBirth(cls): # cls : 表示沒用被實例化的類本身
        print(f"Ron`s Birthday is {cls.y}/{cls.m}/{cls.d:02d}")
        # print(cls)
        # cls().myBirth("Jaque")

    # 不傳遞傳遞默認self參數的方法（該方法也是可以直接被類調用的，但是這樣做不標準）
    def printMyName():
        print(f"My name is {Foo.my_name}.") # 屬性是可以直接用類本身調用的

a = Foo("1000")  #r"" means raw string
print(a)
# inztance = Foo("Danny")
# inztance.myBirth()
# Foo.ronBirth()
# Foo.printMyName()

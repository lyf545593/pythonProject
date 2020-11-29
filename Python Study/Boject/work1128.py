class Animal:
    # 属性：名称，颜色，年龄，性别
    name: str = "None"
    color: str = '白色'
    age: int = 1
    gender: str = "雄性"

    # 初始化属性
    def __init__(self, name, color, age, gender):
        self.name = name  # 实例化属性
        self.color = color
        self.age = age
        self.gender = gender

    # 方法：会叫，会跑
    def shout(self):
        print("会叫")

    def run(self):
        print("会跑")


class Cat(Animal):  # 继承动物类
    # 特有属性：毛发=短毛
    hair: str = "短毛"

    # 继承父类属性
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)  # 父类属性重新赋值
        self.hair = hair

    # 特有方法：会捉老鼠
    def CatchTheMouse(self):
        # 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
        print(f"{self.name}is{self.color} and 年龄是{self.age}岁，性别是{self.gender}{self.hair},技能是会捉老鼠")

    # 重写父类方法
    def shout(self):
        print("喵喵叫")


class Dog(Animal):
    # 添加一个新的属性，毛发=长毛
    hair: str = "长毛"

    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    # 添加一个新的方法， 会看家，
    def home(self):
        print("会看家")


# 创建猫猫的实例
c = Cat("龙猫", "棕色", 2, "雄性", "短毛")
print(c.name, c.color, c.age, c.gender, c.hair)
# 调用捉老鼠的方法
c.CatchTheMouse()

# 创建狗狗的实例
d = Dog("吉娃娃", "白色", 1, "雌性", "长毛")
print(d.name, d.color, d.age, d.gender, d.hair)

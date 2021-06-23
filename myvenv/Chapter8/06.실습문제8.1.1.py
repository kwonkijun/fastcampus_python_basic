# 클래스 생성
class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")

    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] 착용했습니다. {self.effect}")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}] 사용했습니다. {self.effect}")

# 인스턴스 생성
sword = WearableItem("이가닌자의검", 30000, 3.5, True, "체력 5000증가, 마력 5000증가")
sword.wear()
sword.sale()
sword.discard()

potion = UsableItem("신비한투명물약", 150000, 0.1, False, "투명효과 300초 지속")
potion.discard()
potion.sale()
potion.use()
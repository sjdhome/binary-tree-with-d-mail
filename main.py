import os, time, random

d_mail_chance_increase = 0.01


class BinaryTree:
    value = 0
    d_mail_chance = 0
    level = 0
    parent = None
    child = None

    def __init__(self, value, chance, level, parent) -> None:
        self.value = value
        self.d_mail_chance = chance
        self.level = level
        self.parent = parent

    def send_d_mail(self, level):
        if self.level != level:
            return self.parent.send_d_mail(level)
        else:
            if self.value == 0:
                self.value = 1
            else:
                self.value = 0
            self.child = None
            self.d_mail_chance = 0


def printBinaryTree(root: BinaryTree):
    os.system("cls")
    margin = 0
    current = root
    while current != None:
        for _ in range(margin):
            print(" ", end="")
        print(current.value)
        for _ in range(margin):
            print(" ", end="")
        current = current.child
        if current != None:
            if current.value == 0:
                print("|")
            else:
                margin += 2
                print("  \\")


def getValue():
    r = random.random()
    if r >= 0.5:
        return 1
    else:
        return 0


def compute(root: BinaryTree):
    current = root
    while current.child != None:
        current = current.child
    d_mail_chance = random.random() * current.d_mail_chance
    d_mail_level = int(random.random() * current.level)
    if d_mail_chance >= 0.5:
        print(f"D-mail触发，发往第{d_mail_level}层")
        time.sleep(3)
        current.send_d_mail(d_mail_level)
    else:
        current.child = BinaryTree(
            getValue(),
            current.d_mail_chance + d_mail_chance_increase,
            current.level + 1,
            current,
        )


if __name__ == "__main__":
    root = BinaryTree(0, 0, 0, None)
    while True:
        printBinaryTree(root)
        time.sleep(0.5)
        compute(root)

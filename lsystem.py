from turtle import *

class L_system:
    def __init__(self, axiom, rules, angle, size, level):
        self.turtle = Turtle()
        self.axiom = axiom
        self.rules = self.apply_rules(rules)
        self.angle = angle
        self.size = size
        self.level = level
        self.memorized_postion = self.turtle.position()
        

    def drawLsystem(self):
        for cmd in self.axiom:
            if cmd == 'a':
                self.turtle.pd()
                self.turtle.fd(self.size)
            elif cmd == 'b':
                self.turtle.pu()
                self.turtle.fd(self.size)
            elif cmd == '+':
                self.turtle.right(self.angle)
            elif cmd == '-':
                self.turtle.left(self.angle)
            elif cmd == '*':
                self.turtle.right(180)

            # return to the last memorized position and memorize the current position.
            elif cmd == '[':
                self.memorized_postion = self.turtle.position()  
            elif cmd == ']':
                self.turtle.setposition(self.memorized_postion)
# rules to be applied successively to each symbol of the axiom at each iteration.
    def apply_rules(self, rules):
        apply_rules = dict()
        for r in rules:
            l = r.split('=')
            apply_rules.update({l[0]:l[1]})

        return apply_rules

    def Createnew(self):
        while self.level > 0:
            newAxiom = ''
            for n in self.axiom:
                if n in self.rules.keys():
                    newAxiom += self.rules.get(n)
                else:
                    newAxiom += n
            self.axiom = newAxiom
            self.level -= 1




if __name__ == "__main__":
    f = open('lsysdico.txt', 'r')
    axiom = f.readline()
    rules = []
    rules_no = int(f.readline())
    for i in range(rules_no):
        rules.append(f.readline())
    angle = int(f.readline())
    size = int(f.readline())
    level = int(f.readline())
    f.close()

    lsystem = L_system(axiom=axiom, rules=rules, angle=angle, size=size, level=level)
    lsystem.Createnew()
    lsystem.drawLsystem()
    exitonclick()
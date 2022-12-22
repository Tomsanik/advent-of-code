class Monkey:
    def __init__(self, items, oper, test_div, test_res) -> None:
        self.items = items
        self.test_div = test_div
        self.test_res = test_res
        self.oper = oper    # [true/false, number] if true, then +, else *
        self.oper_count = 0

    def test(self, item):
        if item % self.test_div == 0:
            return self.test_res[0]
        else:
            return self.test_res[1]
    
    def throw_out(self):
        self.items = []

    def operation(self, item):
        if self.oper[0]:
            item += self.oper[1]
        else:
            if self.oper[1] == 0:
                item *= item
            else:
                item *= self.oper[1]
        self.oper_count += 1
        return item

    def catch(self, item):
        self.items.append(item)

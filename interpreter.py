
class Tape(object):

    def __init__(self, values = '', default = 0):
        self.default = default
        self.tape = [v for v in values]
        self.pointer = 0

    def shift_right(self):
        self.pointer += 1
        if self.pointer >= len(self.tape):
            self.tape.append(self.default)

    def shift_left(self):
        self.pointer -= 1
        if self.pointer == -1:
            self.tape.insert(0, self.default)
            self.pointer = 0

    def put(self, value):
        self.tape[self.pointer] = value

    def get(self):
        return self.tape[self.pointer]


class Interpreter(object):

    def __init__(self, program=''):
        self.instructions = Tape([c for c in program], 'halt')
        self.data = Tape([0], 0)

    def run(self):
        #for i in range(n):
        while True:
            # get operation
            op = self.instructions.get()
            # execute
            if op == 'halt':
                return
            elif op == '>':
                self.data.shift_right()
            elif op == '<':
                self.data.shift_left()
            elif op == '+':
                self.data.put(self.data.get() + 1)
            elif op == '-':
                self.data.put(max(0, self.data.get() - 1))
            elif op == '.':
                print('%s' % self.data.get())
            elif op == ',':
                self.data.put(int(raw_input('input> ')))
            elif op == '[':
                if self.data.get() == 0:
                    self.instructions.shift_right()
                    depth = 0
                    while not (self.instructions.get() == ']' and depth == 0):
                        inner_op = self.instructions.get()
                        if inner_op == '[':
                            depth += 1
                        elif inner_op == ']':
                            depth -= 1
                        self.instructions.shift_right()
            elif op == ']':
                if self.data.get() != 0:
                    self.instructions.shift_left()
                    depth = 0
                    while not (self.instructions.get() == '[' and depth == 0):
                        inner_op = self.instructions.get()
                        if inner_op == ']':
                            depth += 1
                        elif inner_op == '[':
                            depth -= 1
                        self.instructions.shift_left()
            else:
                raise Exception('unknown op: %s' % op)
            # move to next instruction
            self.instructions.shift_right()


prog_count_down = ',[.-].'
prog_count_up = ',[->.+<]>.'
prog_copy_second = ',>,[->+>+<<]>>[-<<+>>]<<'
prog_if_else = ',>+<[>[->+<]<-]>>.'
prog_if_else2 = ',[[-]>+<]>.'

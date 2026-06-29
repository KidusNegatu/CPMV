#RULES:
#1. VARIABLE_VALUE opcode should come before VARIABLE_NAME opcode.
#2. For every control flow there should be JUMP_IF_TRUE and JUMP_IF_FALSE opcode.
#3. The bytecode must be stored as a list of tuples, where each tuple represents opcode.
class VirtualMachine:
  def __init__(self, byteCode):
    self.byteCode = byteCode
    self.stack = []
    self.memory = {}
    self.LP = 0

  def runVM(self):
    if not isinstance(self.byteCode, list):
        raise TypeError("Bytecode must be a list")

    elif len(self.byteCode) < 2:
        raise RuntimeError("Not enough values on bytecode")
    
    elif not all(isinstance(x, tuple) for x in self.byteCode):
        raise TypeError("Bytecode must contain tuples")
    else:
        pass
    while self.LP < len(self.byteCode):
      if len(self.byteCode[self.LP]) != 2:
        raise RuntimeError("opcode format is not correct")
      instruction, value = self.byteCode[self.LP]

      if instruction == "LOAD_NUMBER":
        self.stack.append(value)

      elif instruction == "LOAD_STRING":
        self.stack.append(value)

      elif instruction == "VARIABLE_VALUE":
        self.stack.append(value)

      elif instruction == "VARIABLE_NAME":
        self.memory[value] = self.stack.pop()

      elif instruction == "ADDITION":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y + x
        self.stack.append(result)

      elif instruction == "SUBTRACTION":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y - x
        self.stack.append(result)

      elif instruction == "MULTIPLICATION":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y * x
        self.stack.append(result)

      elif instruction == "DIVISION":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        if x == 0:
          raise ZeroDivisionError("Can't divide by zero")
        else:
          result = y / x
        self.stack.append(result)

      elif instruction == "POWER":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y ** x
        self.stack.append(result)

      elif instruction == "SQUARE":
        x = self.stack.pop()
        result = x ** 2
        self.stack.append(result)
          
      elif instruction == "FLOOR_DIVISION":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        if x == 0:
          raise ZeroDivisionError("Can't divide by zero")
        else:
          result = y // x
        self.stack.append(result)

      elif instruction == "REMAINING":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        if x == 0:
          raise ZeroDivisionError("Can't divide by zero")
        else:
          result = y % x
        self.stack.append(result)

      elif instruction == "GREATER_THAN":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y > x
        self.stack.append(result)

      elif instruction == "LESS_THAN":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y < x

        self.stack.append(result)

      elif instruction == "EQUAL_TO":
        if len(self.stack) < 2:
          raise RuntimeError("Not enough values on stack")
        x = self.stack.pop()
        y = self.stack.pop()
        result = y == x
        self.stack.append(result)

      elif instruction == "JUMP_IF_FALSE":
        condition = self.stack.pop()
        if condition == False:
          self.LP = value
          continue

      elif instruction == "JUMP_IF_TRUE":
        condition = self.stack.pop()
        if condition == True:
            self.LP = value
            continue

      elif instruction == "PRINT":
        result = self.stack.pop()
        print(result)

      elif instruction == "LOAD_VARIABLE":
        if value not in self.memory:
          raise NameError("The Variable is not found!!")
        variableValue = self.memory[value]
        self.stack.append(variableValue)

      else:
        print("The instruction is not valid according to Kidus's Python Virtual Machine.")
      self.LP += 1

program = [
    ("LOAD_STRING", "Hello"),
    ("PRINT", None)
]
vm = VirtualMachine(program)
vm.runVM()

# Example of opcodes
# ===================

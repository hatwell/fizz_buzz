class Kwic:
    def __init__(self, input_string='', limit=1):
        self.input = input_string.split(' ')
        self.limit = limit

    def get_input(self):
        return self.input

    def get_output(self):
        output = []
        for index,word in enumerate(self.input):
            output.append(self.input[index:(index + self.limit)])

        output = [element for element in output if len(element) == self.limit]

        output = sorted(output, key=lambda x:x[1][0])
        
        output = list(map(lambda x: " ".join(x), output))

        return output
class Test_Case:
    def __init__(self, *arguments):
        self.arguments = []
        for argument in arguments:
            self.arguments.append(argument)

    def get_arguments(self):
        return_string = ""
        for argument in self.arguments:
            if type(argument) is str:
                return_string += '\"' + argument + '\"' + ','
            else:
                return_string += str(argument) + ','
        return return_string[0:len(return_string) - 1]


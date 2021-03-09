from sys import argv


class Manager:
    def __init__(self):
        self.actions = {}
        self.stock = {}
        self.balance = 0
        self.history = []
        self.input_error = False


    def assign(self, action, count):
        def decorate(callback):
            self.actions[action] = (callback, count)
        return decorate

    def execute(self, action, *args, **kwargs):
        if action not in self.actions:
            #print("Error ", action)
            pass
        else:
            self.actions[action][0](self, *args, **kwargs)

    def param_count(self, action):
        return self.actions.get(action, (0, 0))[1]
"""         if action not in self.actions:
            return 0
        return self.actions[action][1]
 """        


class FileManager:
    def __init__(self):
        self.data = []
        self.file_path = 'in.txt'

    def open_file(self):
        with open(self.file_path) as fp:
            for line in fp:
                self.data.append(line.strip())

    def save_data(self):
        with open(self.file_path, 'w') as fp:
            for line in self.data:
                fp.write(line + "\n")

    def file_process(self, manager):
        index = 0
        while index < len(self.data):
            action = self.data[index]
            index += 1
            param_count = manager.param_count(action)
            params = self.data[index: index+param_count]
            manager.execute(action, *params)

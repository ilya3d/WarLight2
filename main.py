# __main__
import sys

class Reader():
    cur = ''
    parts = []
    world = {}
    settings = {}

    def get(self):
        self.cur = sys.stdin.readline().strip('\n')
        if not self.cur or self.cur == '':
            return False
        self.parts = self.cur.split(' ')
        return len(self.parts)

    def set(self, cmd):
        sys.stdout.write(cmd + '\n')

    def apply(self):
        if self.parts[0] == 'pick_starting_regions':
            self.set('give me randomly')
        elif len(self.parts) == 3 and self.parts[0] == 'go':
            s = ''
            if self.parts[1] == 'place_armies':
                for i in range(5):
                    s += 'myBot place_armies ' + str(i) + ' 1,'
            elif self.parts[1] == 'attack/transfer':
                for i in range(5):
                    s += 'myBot attack/transfer ' + str(i) + ' ' + str(i+1) + ' 1,'
            self.set(s)
        elif self.parts[0] == 'settings':
            self.settings[self.parts[1]] = self.parts[2]
        elif self.parts[0] == 'setup_map':
            self.world[self.parts[1]] = [self.parts[i+2] for i in range(len(self.parts) - 2)]



class MyBot():

    reader = None

    def __init__(self):
        self.reader = Reader()

    def run(self):
        while self.reader.get():
            self.reader.apply()


bot = MyBot()
bot.run()
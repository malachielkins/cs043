class Simpledb:
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return ('<' + self.__class__.__name__ +
        ' file=\'' + self.filename + '\'>')
        
    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()
    
    def select_one(self, key):
        f = open(self.filename, 'r')
        for line in f:
            (linekey, linevalue) = line.split('\t', 1)
            if linekey == key:
                return linevalue[:-1]
        f.close()
    
    def delete(self, key):
        f = open(self.filename, 'r')
        newfile = open('newfile.txt', 'w')
        for line in f:
            (linekey, linevalue) = line.split('\t', 1)
            if linekey != key:
                newfile.write(line)
        f.close()
        newfile.close()
        import os
        os.replace('newfile.txt', self.filename)
    
    def update(self, key, value):
        f = open(self.filename, 'r')
        newfile = open('newfile.txt', 'w')
        for line in f:
            (linekey, linevalue) = line.split('\t', 1)
            if linekey == key:
                newfile.write(key + '\t' + value + '\n')
            else:
                newfile.write(line)
        f.close()
        newfile.close()
        import os
        os.replace('newfile.txt', self.filename)

class Antrian:
    def __init__(self):
        self.antrian = []
    
    def enqueue(self, item):
        self.antrian.append(item)
    
    def dequeue(self):
        if len(self.antrian) > 0:
            return self.antrian.pop(0)
        else:
            return None
        
    def __len__(self):
        return len(self.antrian)
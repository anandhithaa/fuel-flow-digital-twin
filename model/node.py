class Node:
    def __init__(self, node_id, node_type, capacity, initial_stock):
        self.id = node_id
        self.type = node_type  # refinery, depot, station
        self.capacity = capacity
        self.stock = initial_stock

    def consume(self, amount):
        consumed = min(self.stock, amount)
        self.stock -= consumed
        return consumed

    def receive(self, amount):
        self.stock = min(self.capacity, self.stock + amount)

class Node:
    def _init_(self, node_id, capacity_mb):
        self.node_id = node_id
        self.capacity = capacity_mb
        self.used = 0

    def upload_file(self, size_mb):
        if self.used + size_mb > self.capacity:
            return "Error: Not enough space"
        self.used += size_mb
        return "Upload successful"

import requests

class NetworkController:
    def _init_(self):
        self.nodes = []

    def register_node(self, node_url):
        self.nodes.append(node_url)
        return {"status": "node registered", "node": node_url}

network = NetworkController()

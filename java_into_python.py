class City:
    def __init__(self, name, straight_line_dist_from_goal, straight_line_dist_from_source, node):
        self.f_n = straight_line_dist_from_goal  # straightLineDistfromGoal
        self.g_n = straight_line_dist_from_source  # straightLineDistfromSource
        self.total = self.f_n + self.g_n
        self.city_name = name
        self.n = node
class Node:
    def __init__(self, name, next_nodes=None):
        self.node_name = name
        self.next_nodes = next_nodes if next_nodes is not None else []
        self.Start = None

    def initialization(self):
        # Create nodes
        Arad = Node("Arad")
        Sibiu = Node("Sibiu")
        RimnicuVilcea = Node("RimnicuVilcea")
        Pitesti = Node("Pitesti")
        Zerind = Node("Zerind")
        Timisoara = Node("Timisoara")
        Craiova = Node("Craiova")
        Bucharest = Node("Bucharest")
        Oradea = Node("Oradea")
        Fagaras = Node("Fagaras")

        # Define connections
        Arad.next_nodes = [
            City("Sibiu", 253, 140, Sibiu),
            City("Zerind", 374, 75, Zerind),
            City("Timisoara", 329, 118, Timisoara)
        ]

        Sibiu.next_nodes = [
            City("Arad", 366, 280, Arad),
            City("Fagaras", 176, 239, Fagaras),
            City("RimnicuVilcea", 193, 220, RimnicuVilcea),
            City("Oradea", 380, 291, Oradea)
        ]

        RimnicuVilcea.next_nodes = [
            City("Pitesti", 100, 317, Pitesti),
            City("Craiova", 160, 366, Craiova),
            City("Sibiu", 253, 300, Sibiu)
        ]

        Pitesti.next_nodes = [
            City("RimnicuVilcea", 193, 414, RimnicuVilcea),
            City("Craiova", 160, 455, Craiova),
            City("Bucharest", 0, 418, Bucharest)
        ]

        self.Start = Arad
        print("Initialized")

    def search(self):
        dest = "ab"
        curr = self.Start
        print(curr.node_name)

        while dest != "Bucharest":
            # Find the city with minimum total cost
            min_total = curr.next_nodes[0].total
            pseudo_curr = curr.next_nodes[0].n

            for i in range(1, len(curr.next_nodes)):
                if curr.next_nodes[i].total < min_total:
                    min_total = curr.next_nodes[i].total
                    pseudo_curr = curr.next_nodes[i].n

            curr = pseudo_curr
            dest = curr.node_name
            print(dest)


class AStar:
    @staticmethod
    def main():
        n = Node("dummy")
        n.initialization()
        n.search()


if __name__ == "__main__":
    AStar.main()

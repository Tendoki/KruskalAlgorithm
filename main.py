import math
import random
import time
from random import randint

class Graph:
     def __init__(self, vertices):
          self.vertices = vertices
          self.edges = []
     def add_edge(self, u, v, weight):
          self.edges.append((u, v, weight))
     def sort_edges(self):
          self.edges = sorted(self.edges, key=lambda item: item[2])
     def get_edges(self):
          return self.edges
     def number_of_vertices(self):
           return self.vertices

     def generateGraph(self, number_of_additional_edges):
         free = []
         selected = []
         for i in range(self.vertices):
             free.append(i)

         first_node = free[random.randint(0, len(free) - 1)]
         free.remove(first_node)
         selected.append(first_node)
         while free:
             node_from_free = free[random.randint(0, len(free) - 1)]
             node_from_selected = selected[random.randint(0, len(selected) - 1)]
             free.remove(node_from_free)
             selected.append(node_from_free)
             self.add_edge(node_from_free, node_from_selected, randint(1, 10))

         for i in range(number_of_additional_edges):
             is_new_edge = False
             while not is_new_edge:
                 is_new_edge = True
                 first_node = random.randint(0, self.vertices - 1)
                 second_node = random.randint(0, self.vertices - 1)
                 for edge in self.edges:
                     if (edge[0] == first_node and edge[1] == second_node) or (
                             edge[0] == second_node and edge[1] == first_node):
                         is_new_edge = False
                         break
             self.add_edge(first_node, second_node, randint(1, 5))

class DisjointSet:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        for node in range(size):
            self.parent.append(node)
            self.rank.append(0)
    def find(self, v):
        if self.parent[v] == v:
            return v
        else:
            return self.find(self.parent[v])
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1

def kruskal(graph):
    forest = []
    graph.sort_edges()
    disjoint_set = DisjointSet(graph.number_of_vertices())
    for (u, v, weight) in graph.get_edges():
        if disjoint_set.find(u) != disjoint_set.find(v):
            forest.append((u, v, weight))
            disjoint_set.union(u, v)
    return forest


if __name__ == '__main__':
    n = 1000
    # number_of_additional_edges = randint(n - 1, (n - 2)*(n - 1)/2)
    number_of_additional_edges = n - 1
    factor = 1
    for i in range(5):
        graph = Graph(n * factor)
        graph.generateGraph(number_of_additional_edges * factor - (factor - 1))

        begin = time.perf_counter()
        forest = kruskal(graph)
        end = time.perf_counter()
        print(f"Вычисление заняло {end - begin:0.4f} секунд")
        print('Количество ребер: ', len(graph.edges))
        print('Количество вершин: ', graph.vertices)
        factor *= 2
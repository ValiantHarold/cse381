from collections import defaultdict

class Graph:
   def __init__(self):
      self.graph = defaultdict(list)

   def addEdge(self, u, v):
      self.graph[u].append(v)

   def _topologicalSort(self, v, visited, stack):
      visited[v] = True

      for i in self.graph[v]:
         if not visited[i]:
            self._topologicalSort(i, visited, stack)
            print(f'Stack: {stack}')

      stack.append(v)

   def topologicalSort(self):
      visited = {node: False for node in self.graph}
      stack = []
      nodes = sorted(self.graph.keys())

      for node in nodes:
         if not visited[node]:
            self._topologicalSort(node, visited, stack)
            print(f'Stack: {stack}')

      print()
      print('Sorted nodes:')
      print(f'Stack: {stack[::-1]}')

   def __str__(self):
      s = ''
      for node in self.graph:
         s += str(node) + ': ' + str(self.graph[node]) + '\n'
      return s

def main():
   graph = Graph()
   graph.addEdge('a', 'b')
   graph.addEdge('b', 'c')
   graph.addEdge('c', 'd')
   graph.addEdge('d', 'g')
   graph.addEdge('e', 'a')
   graph.addEdge('f', 'b')
   graph.addEdge('f', 'c')
   graph.addEdge('f', 'e')
   graph.addEdge('f', 'g')
   graph.addEdge('g', 'e')

   print(graph)

   graph.topologicalSort()
   

if __name__ == "__main__":
   main()
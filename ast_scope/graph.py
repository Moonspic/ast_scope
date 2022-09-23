
class DiGraph:
    def __init__(self):
        self.__adjacency_list = {}
        self.__NodeDict = {}

    def add_nodes_from(self, iterable, Asts=None):
        i = -1 
        if Asts==None: 
            for node in iterable:
                self.add_node(node)
        else: 
            for node in iterable:
                i+=1 
                self.add_node(node)
                self.__NodeDict[node]=Asts[i]
            

    def add_node(self, node, Ast=None):
        if node not in self.__adjacency_list:
            if Ast!=None:
                self.__NodeDict[node]=Ast
            self.__adjacency_list[node] = set()
           
    def add_edge(self, source, target):
        self.__adjacency_list[source].add(target)

    def nodes(self, returnAST=False):
        Result=[]
        if returnAST:
           Result = self.__NodeDict
        else:
            Result =list(self.__adjacency_list)
            
        return Result 

    def edges(self, returnAST = False):
        Edges = list((source, target) for source, targets in self.__adjacency_list.items() for target in targets)
        Asts = []
        Result=Edges
        if returnAST:
            for edge in Edges:
                source = self.__NodeDict[edge[0]]
                target = self.__NodeDict[edge[1]]
                Asts.append((source, target))
            Result =Edges, Asts
        return Result

    def neighbors(self, node):
        return list(self.__adjacency_list[node])

class Solution:

    def hasCircularNode(self, value, graph, visited, knownCircularNodes):
        visitedCopy = set(visited)
        if value in visitedCopy:
            return True
        
        visitedCopy.add(value)
        for neighborValue in graph[value]:
            if neighborValue in knownCircularNodes:
                return True
            if self.hasCircularNode(neighborValue, graph, visitedCopy, knownCircularNodes):
                return True

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 and numCourses > 0:
            return True
        
        # build blank prereq graph
        prereqGraph = {}
        for i in range(numCourses):
            prereqGraph[i] = []

        # build remaining prereq graph
        for i in range(len(prerequisites)):
            prerequisite = prerequisites[i]
            if (prerequisite[0] in prereqGraph):
                prereqGraph[prerequisite[0]].append(prerequisite[1])
            else:
                prereqGraph[prerequisite[0]] = [ prerequisite[1] ]

            if prerequisite[1] not in prereqGraph:
                prereqGraph[prerequisite[1]] = []

        # find all circular nodes
        circularNodes = set()
        for course in prereqGraph.keys():
            if self.hasCircularNode(course, prereqGraph, set(), circularNodes):
                circularNodes.add(course)

        print (prereqGraph)
        print (circularNodes)

        return (len(prereqGraph.keys()) - len(circularNodes) >= numCourses)
class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.points:
            self.points[point] = 0
        self.points[point] += 1
        
    def detectSquare(self, point1, point2, diff):
        t_l = (point1[0], point1[1] + diff)
        t_r = (point2[0], point2[1] + diff)
        value_l = self.points[t_l] if t_l in self.points else 0
        value_r = self.points[t_r] if t_r in self.points else 0
        top = self.points[point2] * value_l * value_r
        
        b_l = (point1[0], point1[1] - diff)
        b_r = (point2[0], point2[1] - diff)
        value_l = self.points[b_l] if b_l in self.points else 0
        value_r = self.points[b_r] if b_r in self.points else 0
        bottom = self.points[point2] * value_l * value_r
        
        return top + bottom
        
    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for x2, y2 in self.points:
            if y == y2 and x != x2:
                count += self.detectSquare(tuple(point), (x2, y2), x2 - x)
        return count
        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

#Floyd’s triangle


class floyd:
    def __init__(self,row):
        self.number = 1
        self.row=row

    def draw(self):
        print("Floyd's Triangle") 
        for i in range(1, self.row + 1):
            for j in range(1, i + 1):        
                print(self.number, end = ' ')
                self.number = self.number + 1
            print()

triangle = floyd(int(input("Enter the number of rows to be printed, N: ")))
triangle.draw()
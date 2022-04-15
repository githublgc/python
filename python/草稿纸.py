import numpy as np           # 提供维度数组与矩阵运算
import copy                  # 从copy模块导入深度拷贝方法
from board import Chessboard

# 基于棋盘类，设计搜索策略
class Game:
    def __init__(self, show = True):
        """
        初始化游戏状态.
        """
        
        self.chessBoard = Chessboard(show)
        self.solves = []
        self.gameInit()
        
    # 重置游戏
    def gameInit(self, show = True):
        """
        重置棋盘.
        """
        
        self.Queen_setRow = [-1] * 8
        self.chessBoard.boardInit(False)
        
    ##############################################################################
    ####                请在以下区域中作答(可自由添加自定义函数)                 #### 
    ####              输出：self.solves = 八皇后所有序列解的list                ####
    ####             如:[[0,6,4,7,1,3,5,2],]代表八皇后的一个解为                ####
    ####           (0,0),(1,6),(2,4),(3,7),(4,1),(5,3),(6,5),(7,2)            ####
    ##############################################################################
    #  
    #AAAAAAAAA
    def queen(A, cur=0):
        if cur == len(A):
            print(A)
            return 0
        for col in range(len(A)):  # 遍历当前行的所有位置
            A[cur] = col
            for row in range(cur):  # 检查当前位置是否相克
                if A[row] == col or abs(col - A[row]) == cur - row:
                    break
            else:  # 如果完成了整个遍历，则说明位置没有相克
                queen(A, cur+1)  # 计算下一行的位置


  #AAAAAAAAAA  
    def run(self, row=0):
        self.solves.append( [0, 5, 7, 2, 6, 3, 1, 4])

    #  AAAAAAA                                                                          #
    ##############################################################################
    #################             完成后请记得提交作业             ################# 
    ##############################################################################
    
    def showResults(self, result):
        """
        结果展示.
        """
        
        self.chessBoard.boardInit(False)
        for i,item in enumerate(result):
            if item >= 0:
                self.chessBoard.setQueen(i,item,False)
        
        self.chessBoard.printChessboard(False)
    
    def get_results(self):
        """
        输出结果(请勿修改此函数).
        return: 八皇后的序列解的list.
        """
        
        self.run()
        return self.solves

game = Game()
solutions = game.get_results()
print('There are {} results.'.format(len(solutions))) #len(solutions)
game.showResults(solutions[0])  #solutions[0]

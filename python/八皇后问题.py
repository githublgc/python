def run(self, cur=0):
        if cur ==  8:   #len(self):8处为len(self)
            print(self)
            return 0
        for col in range(8):  # 遍历当前行的所有位置
            self[cur] = col
            for row in range(cur):  # 检查当前位置是否相克
                if self[row] == col or abs(col - self[row]) == cur - row:
                    break
            else:  # 如果完成了整个遍历，则说明位置没有相克
                run(self, cur+1)  # 计算下一行的位置

run([None]*8)

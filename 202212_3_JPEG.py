import numpy as np
def strlist2numlist(strlist):
    strlist = strlist.split()
    for i in range(len(strlist)):
        strlist[i] = int(strlist[i])
    return strlist

def receive_Q():
    Q = []
    for i in range(8):
        str = input()
        numlist = strlist2numlist(str)
        Q.append(numlist)
    return Q

def alpha_function(u):
    if u == 0:
        return np.sqrt(0.5)
    else:
        return 1

def Mij_function(i,j,M):
    Mij_ = 0
    for u in range(8):
        for v in range(8):
            Mij_ += 1/4 * alpha_function(u) * alpha_function(v) * M[u,v] * np.cos(np.pi/8 * (i + 1/2) * u) * np.cos(np.pi / 8 * (j + 0.5) * v)
    return Mij_
def main():
    Q = receive_Q()
    num_to_scan = int(input()) # 扫描的数据数
    T = int(input()) # 输出选择变量，当取 0 时，输出填充（步骤 3）后的图像矩阵；当取 1 时，输出量化（步骤 4）后的图像矩阵；当取 2 时，输出最终的解码结果。
    scan_data = strlist2numlist(input())

    # print(Q)
    # print(num_to_scan)
    # print(T)
    # print(scan_data)

    M = np.zeros([8,8])
    location = [0, 0] # 当前位置
    step = [0, 0] # 需要维护的方向向量
    for i in range(num_to_scan):
        M[location[0],location[1]] = scan_data[i]
        # 确定下一个location的方向向量
        if location[0] == 0 and ((step[0] == -1 and step[1] == 1) or (step[0] == 0 and step[1] == 0)): # 起步或走到最上边一行向右走
            step = [0, 1]
        elif location[0] == 0 and step == [0, 1]: # 第一行向右走完向左下走
            step = [1, -1]
        elif location[1] == 0 and location[0] != 0 and step == [1, -1]: # 走到最左边一列向下走
            step = [1, 0]
        elif location[1] == 0 and location[0] != 0 and step == [1, 0]: # 向下走完向右上走
            step = [-1, 1]
        elif location[0] == 7 and step == [1, -1]: # 走到最下边一行向右走
            step = [0, 1]
        elif location[0] == 7 and step == [0, 1]: # 向右走完向右上走
            step = [-1, 1]
        elif location[1] == 7 and step == [-1, 1]: # 走到最右边一列后向下走
            step = [1, 0]
        elif location[1] == 7 and step == [1, 0]: # 向下走完向左下走
            step = [1, -1]
        else:
            step = step
        # 更新当前坐标位置
        location[0] = location[0] + step[0]
        location[1] = location[1] + step[1]
    if T == 0:
        for i in range(8):
            for j in range(8):
                if j != 7:
                    print(int(M[i,j]), end=" ")
                else:
                    print(int(M[i,j]))
    elif T == 1:
        M_ = np.array(Q) * M
        for i in range(8):
            for j in range(8):
                if j != 7:
                    print(int(M_[i,j]), end=" ")
                else:
                    print(int(M_[i,j]))
    else:
        M_ = np.array(Q) * M
        M_new = np.zeros([8,8])
        for i in range(8):
            for j in range(8):
                M_new[i,j] = Mij_function(i,j,M_) + 128
                M_new[i,j] = round(M_new[i,j],0)
                if M_new[i,j] > 255:
                    M_new[i,j] =255
                if M_new[i,j] < 0:
                    M_new[i,j] = 0
        for i in range(8):
            for j in range(8):
                if j != 7:
                    print(int(M_new[i,j]), end=" ")
                else:
                    print(int(M_new[i,j]))



if __name__ == "__main__":
    main()

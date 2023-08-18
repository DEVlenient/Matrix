import numpy as np

# 獲取矩陣大小
def get_matrix_size(矩陣編號):
    行數 = int(input(f"請輸入第 {矩陣編號} 個矩陣的行數："))
    列數 = int(input(f"請輸入第 {矩陣編號} 個矩陣的列數："))
    return (行數, 列數)

# 獲取矩陣元素
def get_matrix_elements(矩陣大小, 矩陣編號):
    行數, 列數 = 矩陣大小
    矩陣元素 = []
    print(f"================================")
    print(f"請輸入第 {矩陣編號} 個矩陣的元素：")
    for i in range(行數):
        行 = []
        for j in range(列數):
            元素 = float(input(f"請輸入第 {i+1} 行，第 {j+1} 列的元素："))
            行.append(元素)
        矩陣元素.append(行)
    return 矩陣元素

# 執行矩陣加法
def 矩陣加法(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        raise ValueError("矩陣形狀不相同")
    result = np.add(matrix1, matrix2)
    return result

# 執行矩陣減法
def 矩陣減法(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        raise ValueError("矩陣形狀不相同")
    result = np.subtract(matrix1, matrix2)
    return result

# 執行矩陣乘法
def 矩陣乘法(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError("矩陣形狀不相容")
    result = np.matmul(matrix1, matrix2)
    return result

# 執行矩陣除法
def 矩陣除法(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        raise ValueError("矩陣形狀不相同")
    result = np.divide(matrix1, matrix2)
    return result

# 主函式
def main():
    # 獲取矩陣大小
    size1 = get_matrix_size(1)
    size2 = get_matrix_size(2)

    # 獲取矩陣元素
    matrix1 = get_matrix_elements(size1, 1)
    matrix2 = get_matrix_elements(size2, 2)

    # 將輸入的列表轉換為NumPy陣列
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # 執行矩陣加法
    print(f"================================")
    try:
        矩陣加法結果 = 矩陣加法(matrix1, matrix2)
        print("矩阵加法结果：")
        print(np.round(矩陣加法結果, decimals=2))
    except ValueError as e:
        print(f"矩陣加法出错：{str(e)}")

    # 執行矩陣減法
    try:
        矩陣減法結果 = 矩陣減法(matrix1, matrix2)
        print("矩陣減法結果：")
        print(np.round(矩陣減法結果, decimals=2))
    except ValueError as e:
        print(f"矩陣減法出错：{str(e)}")

    # 執行矩陣乘法
    try:
        矩陣乘法結果 = 矩陣乘法(matrix1, matrix2)
        print("矩陣乘法結果：")
        print(np.round(矩陣乘法結果, decimals=2))
    except ValueError as e:
        print(f"矩陣乘法出错：{str(e)}")

    # 執行矩陣除法
    try:
        矩陣除法結果 = 矩陣除法(matrix1, matrix2)
        print("矩陣除法結果：")
        print(np.round(矩陣除法結果, decimals=2))
    except ValueError as e:
        print(f"矩陣除法出错：{str(e)}")

# 執行主函式
main()
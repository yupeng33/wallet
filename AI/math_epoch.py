import numpy as np

# 1. 构造模拟数据
np.random.seed(42)
x = np.linspace(0, 5, 20)  # 20个样本
y = 2 * x + 1 + np.random.normal(0, 0.3, size=x.shape)  # 加一点噪声

# 初始化参数
w = 0.0
b = 0.0
lr = 0.02  # 学习率
epochs = 500  # 训练30轮
n = len(x)  # batch_size = n，Full Batch

print(f"理论最优：w≈2, b≈1\n")
print("epoch\t w\t\t b\t\t loss\t\tdw\t\tdb")
print("-" * 50)

for epoch in range(epochs):
    # 预测
    y_pred = w * x + b
    # 均方损失 MSE
    loss = np.mean((y_pred - y) ** 2)

    # 梯度（full batch，全部样本一起算梯度）
    dw = (2 / n) * np.sum((y_pred - y) * x)
    db = (2 / n) * np.sum(y_pred - y)

    # 更新w b
    w = w - lr * dw
    b = b - lr * db

    # 打印
    print(f"{epoch + 1}\t {w:.4f}\t {b:.4f}\t {loss:.4f}\t {dw:.4f}\t {db:.4f}")

import torch
from matplotlib import pyplot as plt
from IPython import display
import numpy as np
import random


#生成数据集
num_inputs = 2
num_examples = 1000
true_w = [3,-3.4]
true_b = 4.2
features = torch.randn(num_examples,num_inputs,dtype=torch.float32)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0,0.01,size=labels.size()),dtype=torch.float32)

#print(features[0],labels[0])
#plt.scatter(features[:,1].numpy(),labels.numpy(),1)

#读取数据
def Load_data(features,labels,batch_size):
    nums = len(features)
    indices = list(range(nums))
    random.shuffle(indices)
    for i in range(0,nums,batch_size):
        j = torch.LongTensor(indices[i:min(i+batch_size,nums)])
        yield features.index_select(0,j),labels.index_select(0,j)
'''
batch_size = 10
for X,y in Load_data(features,labels,batch_size):
    print(X,y)
    break
'''

#初始化模型参数
w = torch.tensor(np.random.normal(0,0.01,(num_inputs,1)),dtype=torch.float32,requires_grad=True)
b = torch.zeros(1,dtype=torch.float32,requires_grad=True)

#定义模型
def linreg(X,w,b):
    return torch.mm(X,w) + b

#损失函数
def loss1(y_hat,y):
    return (y_hat-y.view(y_hat.size()))**2/2

#优化算法
def sgd(params,lr,batch_size):
    for param in params:
        param.data -= lr*param.grad/batch_size
  

#训练模型
lr = 0.03
num_epo = 3
net = linreg
loss = loss1
batch_size = 10
for epoch in range(num_epo):
    for X,y in Load_data(features,labels,batch_size):
        y_hat = net(X,w,b)
        l = loss(y_hat,y).sum()
        l.backward()
        sgd([w,b],lr,batch_size)
        w.grad.data.zero_()
        b.grad.data.zero_()
    tran = loss(net(features,w,b),labels)
    print('epoch %d,loss %f' % (epoch+1,tran.mean().item()))

print(true_b,b)
print(true_w,w)
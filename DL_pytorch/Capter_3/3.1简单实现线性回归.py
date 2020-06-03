import torch
from torch import nn
import numpy as np
torch.manual_seed(1)
#print(torch.__version__)
#torch.set_default_tensor_type('torch.FloatTensor')

#生成数据集
num_inputs = 2
num_examples = 1000
true_w = [3,-3.4]
true_b = 4.2
features = torch.randn(num_examples,num_inputs,dtype=torch.float32)
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += torch.tensor(np.random.normal(0,0.01,size=labels.size()),dtype=torch.float32)

#读取数据
import torch.utils.data as Data
batch_size = 10
dataset = Data.TensorDataset(features,labels) #X与y连接起来
data_iter = Data.DataLoader(dataset,batch_size,shuffle=True)

'''
for X,y in data_iter:
    print(X,y)
    break
'''

#定义模型
'''
class linearNet(nn.Module):
    def __init__(self,n_feature):
        super(linearNet,self).__init__()
        self.linear = nn.Linear(n_feature,1)
    
    def forward(self, x):
        y = self.linear(x)
        return y

net = linearNet(num_inputs)
'''

net = nn.Sequential()
net.add_module('linear',nn.Linear(num_inputs,1))
#print(net)
'''
for param in net.parameters():
    print(param)
'''

loss = nn.MSELoss() #损失函数

#优化算法
import torch.optim as optim
optimizer = optim.SGD(net.parameters(),lr=0.03)
#print(optimizer)

num_epochs = 3
for epoch in range(num_epochs):
    for X,y in data_iter:
        output = net(X)
        l = loss(output,y.view(-1,1))
        optimizer.zero_grad() #梯度清0
        l.backward()
        optimizer.step()
    print('epoch %d, loss %f'%(epoch+1,l.item()))

dense = net[0]
print(true_w,dense.weight)
print(true_b,dense.bias)
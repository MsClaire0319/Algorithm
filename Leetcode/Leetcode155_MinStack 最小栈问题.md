# Leetcode155_MinStack 最小栈问题 

## 题目：

设计一个支持push, pop, top操作，并能在常数时间内检索到最小元素的栈

- push(x)——将元素x推入栈中；
- pop()——删除栈顶元素；
- top()——获取栈顶元素；
- getMin()——检索栈中最小元素。

## 示例：

```python
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.pusk(-3);
minStack.getMin();	#返回-3
minStack.pop();
minStack.top();		#返回0
minStack.getMin();	#返回-2
```

## 解题思路：

### 思路一：两个栈实现

栈的基本操作PUSH, POP, TOP使用普通栈stack，getMin使用最小值栈min_stack记录当前最小值。

如果新元素PUSH进入stack：

1. 如果当前min_stack为空栈，将新元素PUSH进入min_stack;
2. 如果当前min_stack为非空，比较min_stack的栈顶元素和新元素的大小，将小的PUSH进入min_stack；

此时，任意时刻的栈stack和min_stack的栈顶元素都是栈stack元素的最小元素；

当需要POP元素时，两个栈同时POP;

## 代码：

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self,x: int) -> None:
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] <= x:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
            
    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]
```


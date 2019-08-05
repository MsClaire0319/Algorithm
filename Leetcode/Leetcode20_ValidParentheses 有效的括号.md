# Leetcode20_ValidParentheses 有效的括号

## 题目内容：

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

## 解题方案：

### 思路一：

将左括号放入字典的键中，将右括号放到字典的值中，因为"in"只对键有效，所以只要检测到左括号就放入栈中，利用后进先出的特性完成括号的匹配和判断。

### 代码：

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'{':'}','[':']','(':')'}
        for i in s:
            if i in dict:
                stack.append(i)
            elif len(stack)==0 or dict[stack.pop()] != i:
                return False
        return len(stack)==0
```


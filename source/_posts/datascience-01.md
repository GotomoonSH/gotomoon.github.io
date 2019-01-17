---
title: 机器学习
date: 2019-01-17 23:10:00
tags: [python,ml]
categories: 机器学习
---

# 机器学习
精通数据科学——从线性回归到深度学习

## 何为机器学习？
机器学习可以被看做一种全新的编程方式。在进行机器学习的时候，人类不需要总结具体的规则或者公式，只需制定学习的步骤，输入大量的数据到计算
机，后者可以根据数据和学习步骤自己总结经验，自动学习。

```flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

```flow
mermaid
graph LR
    id1(Start)-->id2(Stop)
    style id1 fill:#f9f,stroke:#333,stroke-width:4px,fill-opacity:0.5
    style id2 fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 10,5
```

```flow
start=>start: 开始
loginInfo=>inputoutput: 登录数据
verifyLogin=>subroutine: 登录验证
isSuccess=>condition: 验证成功？
respondSuccess=>operation: 响应成功
responseFailure=>operation: 响应失败
end=>end: 结束

start->loginInfo->verifyLogin->isSuccess
isSuccess(yes)->respondSuccess->end
isSuccess(no)->responseFailure->end
```
作者：_Sonia_Xu_ 
来源：CSDN 
原文：https://blog.csdn.net/u010908723/article/details/79188575 
版权声明：本文为博主原创文章，转载请附上博文链接！
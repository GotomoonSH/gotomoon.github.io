---
title: Hexo文章排序
date: 2019-01-17 6:10:01
tags: [hexo]
categories:
---

#  Hexo文章自定义排序

* 在文章属性中加入了top属性，top值越高，其排序越在前。不设置top值的话则按照时间顺序排序。

打开Hexo文件夹下 'node_modules/hexo-generator-index/lib/generator.js' 文件，修改其代码如下：

``` javascript
'use strict';

var pagination = require('hexo-pagination');

module.exports = function(locals) {
  var config = this.config;
  var posts = locals.posts.sort(config.index_generator.order_by);
  var paginationDir = config.pagination_dir || 'page';
  var path = config.index_generator.path || '';

  return pagination(path, posts, {
    perPage: config.index_generator.per_page,
    layout: ['index', 'archive'],
    format: paginationDir + '/%d/',
    data: {
      __index: true
    }
  });

  posts.data = posts.data.sort(function(a, b) {
  if(a.top && b.top) { // 两篇文章top都有定义
      if(a.top == b.top) return b.date - a.date; // 若top值一样则按照文章日期降序排
      else return b.top - a.top; // 否则按照top值降序排
  }
  else if(a.top && !b.top) { // 以下是只有一篇文章top有定义，那么将有top的排在前面（这里用异或操作居然不行233）
      return -1;
  }
  else if(!a.top && b.top) {
      return 1;
  }
  else return b.date - a.date;}); // 都没定义按照文章日期降序排
};
```

在新建文章的时候添加top属性即可。
文章有多个属性，可在 'scaffolds\post.md' 文件中修改模板。

# GPA_management_lite
平均学分绩点管理系统和计算器（4.8制）

> atarashichiaki@hotmail.com
>
> chiaki@seu.edu.cn

### 总览

一个简陋的个人成绩管理和计算平均学分绩点（GPA）的工具

功能有：

1. 创建/删除`成绩单`
2. 在`成绩单`内创建/删除`课程和成绩`
3. 计算`GPA`



### 安装和使用

##### Windows

`download_release`下选择合适的版本进行下载

将下载好的`GPA_management_lite_a******.exe`文件放入一个空文件夹，即可运行

##### 我想要自己打包程序

仅依赖于官方库，建议`Python3`以上版本

##### 我想要源代码运行

仅依赖于官方库，建议`Python3`以上版本



### 程序文件结构

程序创建`seu_grade_data`目录

`descriptor.json`文件中存有所有`成绩单`的基础信息和映射信息

以数字开头的文件`**************.json`是每个`成绩单`内的`课程和成绩`数据
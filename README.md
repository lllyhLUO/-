#pytest自动化测试软件环境搭建
创建一个文件夹：autoTest,使用命令行进入root运行：git clone https://github.com/youngyangyang04/Test-Automation-Framework.git
可能会因为网络不好下载很慢
全局安装uv
curl -LsSf https://astral.sh/uv/install.sh | sh
反馈：
To add $HOME/.local/bin to your PATH, either restart your shell or run:

source $HOME/.local/bin/env (sh, bash, zsh)
source $HOME/.local/bin/env.fish (fish)
在bash脚本模式下选择第一个运行，fish脚本模式则选择第二个运行，"()"里面的内容不需要输入。这个指令是把uv放入path里面，这样无论在哪里都可以调取了。
启动mock服务
执行cd mock_server/api_server
这里需要下载g++用于运行c语言项目：执行apt install -y build-essential。
uv run base/flask_service.py
运行成功之后这个假后端项目就可以跑起来了。
运行测试
执行uv sync
然后下载pytest时，需要先下载一个头文件ffi.h(属于libffi-dev开发依赖),执行apt install -y libffi-dev进行安装。运行uv add pytest下载，用pytest --version验证是否下载成功。
最后执行pytest就可以进行运行测试了。

pytest细节：
pytest执行时可以设置a.参数；b.mark（标记）;c.fixture;d.hook（困难）。
requests：a.[向接口发送请求]和pytest结合=接口自动化；b.[控制浏览器]和pytest结合=web自动化;c.[控制手机App]和pytest结合=App自动化。

 1，表单参数
 主要在web项目：
 1）参数只能是字符串
 2）请求头中包含form
 requests技巧：如果data参数是一个字典，则自动将其识别为表单，并自动添加请求头。这里应该就可以运用上YAML了。
2，JSON参数
主要用在各类项目中：
1）参数类型很多：字符串、数字、布尔值、空值、数组
2）请求头重包含json
 requests技巧：如果传递json参数，则自动将其识别为json参数类型，并自动添加请求头。
3.文件上传


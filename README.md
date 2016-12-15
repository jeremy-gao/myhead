# MyHead
myhead是一个简易的ElasticSearch web可视化管理工具,可以用来观察集群状态，索引管理等.

# 页面预览
--------------
![image](https://github.com/jeremy-gao/myhead/blob/master/assets/i/index.png)
![image](https://github.com/jeremy-gao/myhead/blob/master/assets/i/list.png)

# 功能介绍
---------------
 - 支持集群状态健康健康
 - 分片数监控
 - 索引最大前20(数量可调整)
 - 查看索引mapping，stats，
 - 删除，和批量删除索引


# 计划支持功能
---------------
 - 集群状态非Green告警
 - 多方面绘图统计等.

# 安装部署
---------------
 - 安装apache和mod_wsgi模块
 - 配置vhost如下:
```
 <VirtualHost *:80>
    ServerName your server name
    WSGIScriptAlias / /home/myhead/app.wsgi
    ErrorLog logs/dummy-host.example.com-error_log
    CustomLog logs/dummy-host.example.com-access_log common
<Directory "/home/myhead/">
        Order deny,allow
        Allow from all
</Directory>
</VirtualHost>
```

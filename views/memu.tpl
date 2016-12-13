<header class="am-topbar admin-header">
  <div class="am-topbar-brand">
  <img src="assets/i/logo.png" alt="">
  </div>

  <div class="am-collapse am-topbar-collapse" id="topbar-collapse">
    <ul class="am-nav am-nav-pills am-topbar-nav admin-header-list">

   <li class="am-dropdown tognzhi" data-am-dropdown>
  <button class="am-btn am-btn-primary am-dropdown-toggle am-btn-xs am-radius am-icon-bell-o" data-am-dropdown-toggle> 
  集群:{{ state["cluster_name"] }}
  <span class="am-badge am-badge-danger am-round">{{ state["number_of_nodes"] }}</span>
  </button>
  <ul class="am-dropdown-content">
    <li class="am-dropdown-header">集群节点列表</li>
    %for list in listnode:
      %if len(list) !=0 and list[0] != "i":
        %if list.split()[1] == '*':
          <li>
          <a href="#">{{ list.split()[0] }}<span class="am-badge am-badge-danger am-round">{{ list.split()[1] }}</span></a>
          </li>
        %else:
          <li><a href="#">{{ list.split()[0] }}</a></li>
        %end
      %end
    %end
  </ul>
</li>

 <li class="kuanjie">
  <a href="/">集群信息</a>
  <a href="list.html">索引管理</a>
   <a href="#">系统设置</a>
 </li>
 <li class="soso">
  
<p>   
  <select data-am-selected="{btnWidth: 70, btnSize: 'sm', btnStyle: 'default'}">
          <option value="b">全部</option>
          <option value="o">Test</option>
          <option value="o">Test</option>
        </select>
</p>

<p class="ycfg"><input type="text" class="am-form-field am-input-sm" placeholder="圆角表单域" /></p>
<p>
<button class="am-btn am-btn-xs am-btn-default am-xiao"><i class="am-icon-search"></i></button>
</p>
 </li>


      <li class="am-hide-sm-only" style="float: right;"><a href="javascript:;" id="admin-fullscreen"><span class="am-icon-arrows-alt"></span> <span class="admin-fullText">开启全屏</span></a></li>
    </ul>
  </div>
</header>

<div class="am-cf admin-main"> 

<div class="nav-navicon admin-main admin-sidebar">
    
    
    <div class="sideMenu am-icon-dashboard" style="color:#aeb2b7; margin: 10px 0 0 0;"> 欢迎系统管理员：Jeremy Gao</div>
    <div class="sideMenu">
      <h3 class="am-icon-flag"><em></em> <a href="#">ElasticSearch</a></h3>
      <ul>
        <li><a href="/">集群概览</a></li>
      </ul>
      <h3 class="am-icon-cart-plus"><em></em> <a href="list.html">索引管理</a></h3>
      <ul>
        <li><a href="list.html">索引列表</a></li>
      </ul>
      <h3 class="am-icon-gears"><em></em> <a href="#">系统设置</a></h3>
      <ul>
        <li>邮件/短信管理</li>
      </ul>
    </div>
    <!-- sideMenu End --> 
    
    <script type="text/javascript">
      jQuery(".sideMenu").slide({
        titCell:"h3", //鼠标触发对象
        targetCell:"ul", //与titCell一一对应，第n个titCell控制第n个targetCell的显示隐藏
        effect:"slideDown", //targetCell下拉效果
        delayTime:300 , //效果时间
        triggerTime:150, //鼠标延迟触发时间（默认150）
        defaultPlay:true,//默认是否执行效果（默认true）
        returnDefault:true //鼠标从.sideMen移走后返回默认状态（默认false）
        });
    </script> 
</div>
</div>
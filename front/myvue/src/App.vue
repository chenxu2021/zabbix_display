<template>
  <div>
    <el-container style="height: 500px; border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu :default-openeds="['1', '3']" router>
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>资源监控</template>
          <!-- <el-menu-item-group> -->
            <!-- <template slot="title">分组一</template> -->
            <el-menu-item index="/host">资产信息</el-menu-item>
            <el-menu-item index="/hostinfo">主机</el-menu-item>
            <el-menu-item index="/cpuinfo">CPU</el-menu-item>
            <!-- <el-menu-item index="/">Hello</el-menu-item> -->
          <!-- </el-menu-item-group> -->
          <!-- <el-menu-item-group title="分组2"> -->
            <el-menu-item index="/meminfo">内存</el-menu-item>
            <el-menu-item index="/diskinfo">磁盘</el-menu-item>
          <!-- </el-menu-item-group> -->
          <!-- <el-submenu index="1-4"> -->
            <!-- <template slot="title">选项4</template> -->
            <!-- <el-menu-item index="1-4-1">选项4-1</el-menu-item> -->
          <!-- </el-submenu> -->
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-dropdown>
          <i class="el-icon-setting" style="margin-right: 15px"></i>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>查看</el-dropdown-item>
            <el-dropdown-item>新增</el-dropdown-item>
            <el-dropdown-item>删除</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        <span>Admin</span>
      </el-header>

      <el-main>
        
        
          <router-view></router-view>
          <!-- <el-table :data="tableData"> -->
          <!-- <el-table-column prop="date" label="日期" width="140">
          </el-table-column>
          <el-table-column prop="name" label="姓名" width="120">
          </el-table-column>
          <el-table-column prop="address" label="地址"> </el-table-column>
          </el-table-column>
          <el-table-column prop="status" label="状态"> </el-table-column> -->

        <!-- </el-table> -->
      </el-main>
    </el-container>
  </el-container>
  </div>
  
</template>


<style>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>

<script>
export default {
  // data() {
  //   const item = {
  //     date: "2021-05-16",
  //     name: "mysql-01",
  //     address: "192.168.1.100",
  //     status: "在线",
  //   };
  //   return {
  //     tableData: Array(20).fill(item),
  //   };
  // },
};
</script>
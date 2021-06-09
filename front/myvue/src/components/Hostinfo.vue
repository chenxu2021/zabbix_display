/* eslint-disable vue/no-parsing-error */
<!--  -->
<template>
  <div id="app">
    <el-table :data="tableData">
    <!-- <el-table> -->
      <!-- <el-table-column prop="date" label="日期" width="140"></el-table-column> -->
      <el-table-column prop="name" label="主机名" width="120"></el-table-column>
      <!-- <el-table-column prop="address" label="IP地址"> </el-table-column> -->
      <el-table-column prop="address" label="IP地址"> </el-table-column>
      <el-table-column prop="status" label="状态" >
        <template slot-scope="scope">
          <span v-if='scope.row.value != 1'> {{scope.row.status}} </this></span>
          <span v-else style="color: red">{{scope.row.status}}</span>
        </template> 
       </el-table-column>
      
    </el-table>
  </div>
</template>

<script>
//这里可以导入其他文件（比如：组件，工具js，第三方插件js，json文件，图片文件等等）
//例如：import 《组件名称》 from '《组件路径》';

export default {
  //import引入的组件需要注入到对象中才能使用
  components: {},
  data() {
    return {
          tableData: [],
        }
  },
  //监听属性 类似于data概念
  computed: {},
  //监控data中的数据变化
  watch: {},

  //方法集合
  methods: {
    getMenu() {
      this.$http.get("http://192.168.1.3:5000/hostinfo").then(
        (response) => {
          // get body data
          // this.someData = response.body;
          // this.name = response.data;
          // this.status = response.data;
          console.log(response.data.data)
          console.log(response.bodyText)
          // console.log(Array(response.bodyText))
          this.tableData = response.data.data
          // this.tableData =  response.bodyText
        },
        (response) => {
          // error callback
        }
      );
    },
  },
  //生命周期 - 创建完成（可以访问当前this实例）
  created() {
    this.getMenu();
  },
  //生命周期 - 挂载完成（可以访问DOM元素）
  mounted() {},
  beforeCreate() {}, //生命周期 - 创建之前
  beforeMount() {}, //生命周期 - 挂载之前
  beforeUpdate() {}, //生命周期 - 更新之前
  updated() {}, //生命周期 - 更新之后
  beforeDestroy() {}, //生命周期 - 销毁之前
  destroyed() {}, //生命周期 - 销毁完成
  activated() {
    this.getHost();
  }, //如果页面有keep-alive缓存功能，这个函数会触发
};
</script>
<style scoped>
/* //@import url(); 引入公共css类 */
</style>
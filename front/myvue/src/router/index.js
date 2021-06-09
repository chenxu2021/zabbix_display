import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Hostinfo from '@/components/Hostinfo'
import Cpuinfo from '@/components/Cpuinfo'
import Meminfo from '@/components/Meminfo'
import Diskinfo from '@/components/Diskinfo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/hostinfo',
      name: 'Hostinfo',
      component: Hostinfo
    },
    {
      path: '/cpuinfo',
      name: 'Cpuinfo',
      component: Cpuinfo
    },
    {
      path: '/meminfo',
      name: 'Meminfo',
      component: Meminfo
    },
    {
      path: '/diskinfo',
      name: 'Diskinfo',
      component: Diskinfo
    },

  ]
})

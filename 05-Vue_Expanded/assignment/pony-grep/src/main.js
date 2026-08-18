import Vue from 'vue'
import App from './App.vue'

// Making Bootstrap available in Vue project.
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import './app.scss'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
// Credit: https://bootstrap-vue.org/docs/#using-module-bundlers

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

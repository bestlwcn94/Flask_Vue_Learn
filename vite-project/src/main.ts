import { createApp } from 'vue'
import App from './App.vue'
import router from "./router/index"
import ElementPlus from 'element-plus'
import naive from 'naive-ui'
import "./style.css"
import 'element-plus/dist/index.css'
createApp(App).use(ElementPlus).use(naive).use(router).mount('#app')

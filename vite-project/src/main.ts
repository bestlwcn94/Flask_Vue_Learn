import { createApp } from 'vue'
import App from './App.vue'
import router from "./router/index"
import ElementPlus from 'element-plus'
import "./style.css"
import 'element-plus/dist/index.css'
createApp(App).use(ElementPlus).use(router).mount('#app')

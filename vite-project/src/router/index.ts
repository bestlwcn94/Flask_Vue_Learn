// write router
import { createWebHashHistory,createRouter } from "vue-router";
import HelloWorld from "../components/HelloWorld.vue";
import Login from "../components/Login.vue";

const  router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/main',
            component: HelloWorld,
        },
        {
            path: '/',
            component: Login,
        }
    ]

});
export default router;


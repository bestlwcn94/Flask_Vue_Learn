// write router
import { createWebHashHistory,createRouter } from "vue-router";
import HelloWorld from "../components/HelloWorld.vue";
import Login from "../components/Login.vue";
import Layout from "../view/layout.vue";
const  router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/',
            component: Layout,
            name: 'Layout',
            children:[
                {
                    path: '/',
                    component:() => import("../view/MenuItem/Home.vue"),
                    name: 'Home',
                },
                {
                    path: '/Home1',
                    component: () =>import("../view/MenuItem/Home1.vue"),
                    name: 'Home1',
                },
                                {
                    path: '/Home2',
                    component: () =>import("../view/MenuItem/Home2.vue"),
                    name: 'Home2',
                },
                                {
                    path: '/Home3',
                    component: () =>import("../view/MenuItem/Home3.vue"),
                    name: 'Home3',
                    redirect: '/Home3-sub1',
                    children:[
                        {
                            path: '/Home3-sub1',
                            component: () =>import("../view/MenuItem/Home3-sub/Home3-sub1.vue"),
                            name: 'Home3-sub1',
                        },
                       {
                            path: '/Home3-sub2',
                            component: () =>import("../view/MenuItem/Home3-sub/Home3-sub2.vue"),
                            name: 'Home3-sub',
                        }
                    ]
                },
                                {
                    path: '/Home4',
                    component: () =>import("../view/MenuItem/Home4.vue"),
                    name: 'Home4',
                },
                                {
                    path: '/Home5',
                    component: () =>import("../view/MenuItem/Home5.vue"),
                    name: 'Home5',
                },
            ]
        },
        {
            path: '/login',
            component: Login,
            name: 'login',
        }
    ]

});
export default router;


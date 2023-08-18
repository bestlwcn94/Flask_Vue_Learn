<script setup lang="ts">
import axios from 'axios'
import {reactive} from "vue";
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const userinfo =reactive(
    {
      name:'',
      password:''
    }
)

const submit2 =() => {
  var params = new URLSearchParams();
  params.append('name',userinfo.name);
  params.append('password',userinfo.password);

  axios.post("http://127.0.0.1:5000/w",params).then(res => {

    if (res.data.msg =="登录成功"){
      console.log('222')
      console.log('登录成功')

      router.push({path:'/main'})
      // window.location.href = '/'

    }
    else
      {
        console.log('111')
        console.log('登录失败')

      }
  })
}
const submit1 =() => {
  var params = new URLSearchParams();
  params.append('name',userinfo.name);
  params.append('password',userinfo.password);

  axios.post("http://127.0.0.1:5000/z", {'name':userinfo.name, 'password':userinfo.password}).then(res => {
      console.log(res.data)
      if (res.data.msg =="登录成功"){
        console.log('222')
        console.log('登录成功')

        router.push({path:'/main'})
        // window.location.href = '/'
      }
      else{
        console.log('111')
        console.log('登录失败')
          }
  })
}
</script>

<template>
  <form >
  <div>
    <input title="text" placeholder="用户名" v-model="userinfo.name">
  </div>
  <div>
    <input title="text" placeholder="密码" v-model = "userinfo.password">
  </div>
  <div>
    <button class="sigio"  title="text"  type='submit' @click="submit2" >列表提交</button>
  </div>
  </form>
    <form >
  <div>
    <input title="text" placeholder="用户名" v-model="userinfo.name">
  </div>
  <div>
    <input title="text" placeholder="密码" v-model = "userinfo.password">
  </div>
  <div>
    <button class="sigio"  title="text"  type='submit' @click="submit1" >form提交</button>
  </div>
  </form>
</template>

<style>
.sigio{
  font-size: 20px;
  font-weight: bold;
  color: black;
}
</style>
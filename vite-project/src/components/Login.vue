
<template>

  <div class="login-container">

    <div class="login-form">

      <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef">

        <h3 class="title">用户登录</h3>

        <el-form-item prop="username">
          <el-input v-model="loginForm.username" placeholder="用户名" ></el-input>
        </el-form-item>

        <el-form-item prop="password">
          <el-input type="password" v-model="loginForm.password" placeholder="密码"></el-input>
        </el-form-item>

        <el-button class="login-btn" type="primary" @click="handleLogin">登录</el-button>
        <el-button class="change-pwd-btn" @click="checklogin">修改密码</el-button>
        <el-button class="register-btn" @click="zhuce">注册</el-button>

      </el-form>

    </div>

  </div>

</template>

<script setup>

import {reactive, ref} from 'vue'
import {ElMessage} from 'element-plus'
import { useRouter } from 'vue-router'
import axios from 'axios'
axios.defaults.baseURL = 'http://192.168.1.3:5003'

const router = useRouter()

const token = ref()

const loginForm = reactive({
  username: '',
  password: ''
})
const handleLogin =() => {

  axios.post("/login", {'username':loginForm.username, 'password':loginForm.password}).then(res => {
      console.log(res.data.Authorization)

      if (res.data.msg =="Login successful!"){
        console.log('222')
        console.log('登录成功')

        localStorage.setItem('token', res.data.Authorization)

      }
      else{
        console.log('111')
        console.log('登录失败')
      }

  })

}
const checklogin =()=> {
  console.log(111)
  let token = localStorage.getItem('token')
  console.log("checklogin:",token)

  if(!token) {
    console.log('No token saved')
    return
  }

  try {

     axios.get('/profile',{headers:{'Authorization': token}}).then(res => {
      console.log(res.data.profile)
       if (res.data.profile==loginForm.username) {
         console.log('验证成功')
         router.push('/ee')
       }
     })

  } catch (error) {
    console.log('请求失败', error)
  }

}


const zhuce=()=>{
      let token = localStorage.getItem('token')
      axios.get('/z', {params:{'username':loginForm.username, 'password':loginForm.password},headers:{'Authorization': token}}).then(res => {
      console.log(res.data)})
}

</script>

<style>

.login-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  align-items: center;
  justify-content: center;

  background: linear-gradient(to bottom right, #FC466B, #3F5EFB);
}

.login-form {
  width: 400px;
  padding: 60px;
  border-radius: 10px;
  font-size: 1.5em;
  background: linear-gradient(to top left, #FFAFBD, #B9D8FF);
  box-shadow: 0 5px 10px rgba(0,0,0,.2);
}

.login-form-item {
  height: 60px;
  margin-bottom: 20px;
}

.login-input {
  height: 40px;
  font-size: 18px;
}

.login-label {
  font-size: 20px;
}

.login-btn {
  background: linear-gradient(to right,#7928CA,#FF0080);
  color: #fff;
  font-weight: bold;
}

/* 注册按钮 */
.register-btn {
  background: #34c924;
  color: #fff;
  border: 1px solid #33b727;
}

.register-btn:hover {
  background: #33b727;
}

/* 修改密码按钮 */
.change-pwd-btn {
  font-size: 12px;
  color: #999;
  text-decoration: underline;
}

.change-pwd-btn:hover {
  color: #666;
}

.title {
  font-size: 28px;
}

</style>
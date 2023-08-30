
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
        <el-button class="change-pwd-btn">修改密码</el-button>
        <el-button class="register-btn">注册</el-button>

      </el-form>

    </div>

  </div>

</template>

<script setup>

import {reactive, ref} from 'vue'
import {ElMessage} from 'element-plus'
import { useRouter } from 'vue-router'

const router = useRouter()

const loginForm = reactive({
  username: '',
  password: ''
})

const loginFormRef = ref()

const loginRules = reactive({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
   { required: true, message: '请输入密码', trigger: 'blur' }
  ]
})

// 登录接口
const loginApi = (form) => {
  return axios.post('http://192.168.1.3:5003/login', form)
}

// 登录
const handleLogin = async () => {

  const valid = await loginFormRef.value.validate()
  if (!valid) return

  try {
    ElMessage.success('开始登陆')
    const {data} = await loginApi(loginForm)
    console.log({data})
    // 保存token
    localStorage.setItem('token', data.token)

    // 跳转到首页
    router.push('/home')

  } catch (err) {
    ElMessage.error(err.response)
  }

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
<!--<script setup lang="ts">-->
<!--import axios from 'axios'-->
<!--import {reactive} from "vue";-->
<!--import { useRouter, useRoute } from 'vue-router'-->

<!--const router = useRouter()-->
<!--const userinfo1 =reactive(-->
<!--    {-->
<!--      name:'',-->
<!--      password:''-->
<!--    }-->
<!--)-->
<!--const userinfo2 =reactive(-->
<!--    {-->
<!--      name:'',-->
<!--      password:''-->
<!--    }-->
<!--)-->
<!--const submit1 =() => {-->
<!--  var params = new URLSearchParams();-->
<!--  params.append('name',userinfo1.name);-->
<!--  params.append('password',userinfo1.password);-->

<!--  axios.post("http://127.0.0.1:5003/w",params).then(res => {-->

<!--    if (res.data.msg =="登录成功"){-->
<!--      console.log('222')-->
<!--      console.log('登录成功')-->

<!--      router.push({name:'HelloWorld'})-->
<!--      // window.location.href = '/'-->

<!--    }-->
<!--    else-->
<!--      {-->
<!--        console.log('111')-->
<!--        console.log('登录失败')-->

<!--      }-->
<!--  })-->
<!--}-->
<!--const submit2 =() => {-->

<!--  axios.post("http://192.168.1.3:5003/z", {'name':userinfo2.name, 'password':userinfo2.password}).then(res => {-->
<!--      console.log(res.data)-->
<!--      if (res.data.msg =="登录成功"){-->
<!--        console.log('222')-->
<!--        console.log('登录成功')-->

<!--        router.push({name: 'HelloWorld'})-->

<!--      }-->
<!--      else{-->
<!--        console.log('111')-->
<!--        console.log('登录失败')-->
<!--          }-->
<!--  })-->
<!--}-->
<!--</script>-->

<!--<template>-->
<!--  <div class ="login-container">-->
<!--    <el-form :model="userinfo1" @click.prevent="" class ="login-form" label-position="right" label-width=100px>-->
<!--      <el-form-item class="login-form-user1">-->
<!--          <span style="height: 40px; float: left;margin-right: 10px ;font-size:16px">用户名</span>-->
<!--          <el-input label="用户名" title="text" v-model="userinfo1.name"-->
<!--                    style="width: 80%;height: 40px; float: left"></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item  class="login-form-user1" >-->
<!--        <span style="height: 40px; float: left;margin-right: 25px ;font-size:16px">密码</span>-->
<!--        <el-input title="text" v-model="userinfo1.password" class="login-form-pass-input" type="password"-->
<!--        style="width: 80%;height: 40px; float: left"></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item class="login-form-user1">-->
<!--&lt;!&ndash;        <span style="height: 40px; float: left;margin-right: 25px ;font-size:16px">提交</span>&ndash;&gt;-->
<!--        <el-button @click="submit1" class ="sub button"  style="width: 20%;margin-left:57px" type="primary" >提交</el-button>-->
<!--        <img src="../assets/images/logo.svg" alt="Smiley face" style="height: 40px; float: left;margin-right: 25px"/>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--&lt;!&ndash;    <el-form  @click.prevent="" class ="login-form" label-position="top">&ndash;&gt;-->
<!--&lt;!&ndash;          <el-form-item  class="login-form-user1" label="用户名">&ndash;&gt;-->
<!--&lt;!&ndash;            <el-input title="text" placeholder="用户名" v-model="userinfo2.name" class ="user button1"></el-input>&ndash;&gt;-->
<!--&lt;!&ndash;          </el-form-item>&ndash;&gt;-->
<!--&lt;!&ndash;          <el-form-item label="密码">&ndash;&gt;-->
<!--&lt;!&ndash;            <el-input title="text" placeholder="密码" v-model = "userinfo2.password" class ="password button2"></el-input>&ndash;&gt;-->
<!--&lt;!&ndash;          </el-form-item >&ndash;&gt;-->
<!--&lt;!&ndash;          <el-form-item label="提交">&ndash;&gt;-->
<!--&lt;!&ndash;            <el-button   title="text"  type='success' @click="submit2"  class ="sub button2 ">form提交 </el-button>&ndash;&gt;-->
<!--&lt;!&ndash;          </el-form-item>&ndash;&gt;-->
<!--&lt;!&ndash;    </el-form>&ndash;&gt;-->
<!--  </div>-->
<!--</template>-->
<!--<style lang="scss" scoped>-->
<!--.login-container{-->
<!--  position : absolute;-->
<!--  width:100%;-->
<!--  height: 100%;-->
<!--  background-image: url("../assets/images/米莱迪.jpg");-->
<!--  .login-form {-->
<!--    width: 600px;-->
<!--    height: 200px;-->
<!--    margin:  500px auto ;-->
<!--    //background-color: red;-->

<!--  }-->
<!--}-->


<!--</style>-->








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
import axios from 'axios'

const router = useRouter()

const token = ref()

const loginForm = reactive({
  username: '',
  password: ''
})
const handleLogin =() => {

  axios.post("http://192.168.1.3:5003/login", {'username':loginForm.username, 'password':loginForm.password}).then(res => {
      console.log(res.data.access_token)
      localStorage.setItem('token', res.access_token)
      if (res.data.msg =="登录成功"){
        console.log('222')
        console.log('登录成功')

        router.push({name: 'HelloWorld'})

      }
      else{
        console.log('111')
        console.log('登录失败')
          }
  })
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
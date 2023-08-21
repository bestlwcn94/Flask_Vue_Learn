<script setup lang="ts">
import axios from 'axios'
import {reactive} from "vue";
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const userinfo1 =reactive(
    {
      name:'',
      password:''
    }
)
const userinfo2 =reactive(
    {
      name:'',
      password:''
    }
)
const submit1 =() => {
  var params = new URLSearchParams();
  params.append('name',userinfo1.name);
  params.append('password',userinfo1.password);

  axios.post("http://127.0.0.1:5003/w",params).then(res => {

    if (res.data.msg =="登录成功"){
      console.log('222')
      console.log('登录成功')

      router.push({name:'HelloWorld'})
      // window.location.href = '/'

    }
    else
      {
        console.log('111')
        console.log('登录失败')

      }
  })
}
const submit2 =() => {

  axios.post("http://192.168.1.3:5003/z", {'name':userinfo2.name, 'password':userinfo2.password}).then(res => {
      console.log(res.data)
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

<template>
  <div class ="login-container">
    <el-form :model="userinfo1" @click.prevent="" class ="login-form" label-position="right" label-width=100px>
      <el-form-item class="login-form-user1">
          <span style="height: 40px; float: left;margin-right: 10px ;font-size:16px">用户名</span>
          <el-input label="用户名" title="text" v-model="userinfo1.name"
                    style="width: 80%;height: 40px; float: left"></el-input>
      </el-form-item>
      <el-form-item  class="login-form-user1" >
        <span style="height: 40px; float: left;margin-right: 25px ;font-size:16px">密码</span>
        <el-input title="text" v-model="userinfo1.password" class="login-form-pass-input" type="password"
        style="width: 80%;height: 40px; float: left"></el-input>
      </el-form-item>
      <el-form-item class="login-form-user1">
<!--        <span style="height: 40px; float: left;margin-right: 25px ;font-size:16px">提交</span>-->
        <el-button @click="submit1" class ="sub button"  style="width: 20%;margin-left:57px" type="primary" >提交</el-button>
        <img src="../assets/images/logo.svg" alt="Smiley face" style="height: 40px; float: left;margin-right: 25px"/>
      </el-form-item>
    </el-form>
<!--    <el-form  @click.prevent="" class ="login-form" label-position="top">-->
<!--          <el-form-item  class="login-form-user1" label="用户名">-->
<!--            <el-input title="text" placeholder="用户名" v-model="userinfo2.name" class ="user button1"></el-input>-->
<!--          </el-form-item>-->
<!--          <el-form-item label="密码">-->
<!--            <el-input title="text" placeholder="密码" v-model = "userinfo2.password" class ="password button2"></el-input>-->
<!--          </el-form-item >-->
<!--          <el-form-item label="提交">-->
<!--            <el-button   title="text"  type='success' @click="submit2"  class ="sub button2 ">form提交 </el-button>-->
<!--          </el-form-item>-->
<!--    </el-form>-->
  </div>
</template>
<style lang="scss" scoped>
.login-container{
  position : absolute;
  width:100%;
  height: 100%;
  background-image: url("../assets/images/米莱迪.jpg");
  .login-form {
    width: 600px;
    height: 200px;
    margin:  500px auto ;
    //background-color: red;

  }
}


</style>
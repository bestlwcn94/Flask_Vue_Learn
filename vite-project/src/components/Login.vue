<script setup lang="ts">
import axios from 'axios'
import {reactive} from "vue";
const userinfo =reactive(
    {
      name:'',
      password:''
    }
)
const submit111 = ()=>{
    console.log(userinfo)
}
</script>

<template>
  <form >
  <div>
    <input title="text" placeholder="用户名11" v-model="userinfo.name">
  </div>
  <div>
    <input title="text" placeholder="密码22" v-model = "userinfo.password">
  </div>
  <div>
    <button class="sigio"  title="text11111111"  type='submit' @click="submit111" >提交</button>
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
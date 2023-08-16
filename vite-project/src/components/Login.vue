<script setup lang="ts">
import axios from 'axios'
import {reactive} from "vue";
const userinfo =reactive(
    {
      name:'',
      password:''
    }
)
const submit = ()=>{
    console.log(userinfo)
}
</script>

<template>
  <div>
    <input title="text" placeholder="用户名" v-model="userinfo.name">
  </div>
  <div>
    <input title="text" placeholder="密码" v-model = "userinfo.password">
  </div>
  <div>
    <button title="text" @click="submit"></button>
  </div>>
</template>

<style scoped>

</style>
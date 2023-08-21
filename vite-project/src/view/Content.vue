<script setup lang="ts">
import Header from "./Header.vue";
</script>

<template>
  <div>
    <Header class = "header"></Header>
    <div class = "content">
       <router-view></router-view>
    </div>
  </div>
</template>

<style scoped lang="less">
.header
{
 height: 60px;
  background-color: blueviolet;
}

.content
{
  height: 100%;
  background-color: palevioletred;
}


</style>
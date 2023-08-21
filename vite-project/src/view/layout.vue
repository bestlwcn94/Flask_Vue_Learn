<script setup lang="ts">
import Content  from "./Content.vue";
import Mymenu from "./Mymenu.vue";
</script>

<template>
  <div class="Container">
    <Mymenu  class = "Mymenu"/>
    <Content class = "content" />
  </div>
</template>

<style lang ="less" scoped>
.Container {
  .Mymenu{
    width: 200px;
    min-height:500px;
    position: fixed;
    background-color: dodgerblue;
    top:0;
    bottom:0;
    /* border: 1px solid red; */
  }
  .content{
    margin-left: 200px;
  }
}
</style>
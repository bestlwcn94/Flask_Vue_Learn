<script setup lang="ts">
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
</script>

<template>
  <el-menu
    default-active="/Home"
    class="el-menu-vertical-demo"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    router >
<!--    <el-sub-menu index="/Home1">-->
<!--      <template #title>-->
<!--        <el-icon><location /></el-icon>-->
<!--        <span>导航一</span>-->
<!--      </template>-->
<!--      <el-menu-item-group>-->
<!--        <template #title>分组一</template>-->
<!--        <el-menu-item index="1-1">选项1</el-menu-item>-->
<!--        <el-menu-item index="1-2">选项2</el-menu-item>-->
<!--      </el-menu-item-group>-->
<!--      <el-menu-item-group title="分组2">-->
<!--        <el-menu-item index="1-3">选项3</el-menu-item>-->
<!--      </el-menu-item-group>-->
<!--      <el-sub-menu index="1-4">-->
<!--        <template #title>选项4</template>-->
<!--        <el-menu-item index="1-4-1">选项1</el-menu-item>-->
<!--      </el-sub-menu>-->
<!--    </el-sub-menu>-->
  <el-menu-item index="/Home1">
    <el-icon><location /></el-icon>
    <template #title>Home1</template>
  </el-menu-item>
    <el-menu-item index="/Home2">
      <el-icon><icon-menu/></el-icon>
      <template #title>Home2</template>
    </el-menu-item>
    <el-menu-item index="/Home3" >
      <el-icon><document /></el-icon>
      <template #title>Home3</template>
    </el-menu-item>
    <el-menu-item index="/Home4">
      <el-icon><setting /></el-icon>
      <template #title>Home4</template>
    </el-menu-item>
    <el-menu-item index="/Home5">
      <el-icon><setting /></el-icon>
      <template #title>Home5</template>
    </el-menu-item>
  </el-menu>



</template>

<style scoped>

</style>
<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'



import { useRouter, useRoute } from 'vue-router'





const count = ref(0)
const name1 = ref('')

const mkhj =() => {
  axios.get("http://127.0.0.1:5000")
      .then(res => {
            name1.value = res.data
            console.log (res.data)
            return res.value
          }
      )
}
const router = useRouter()
const mkhj1=() => {
   router.push({name: 'login'})
}
</script>

<template>
  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <button type="button" @click=mkhj>count is {{ name1}}</button>
    <button type="button" @click=mkhj1>count is {{ name1}}</button>
  </div>
</template>

<style scoped>

</style>

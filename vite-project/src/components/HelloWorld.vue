<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'



import { useRouter, useRoute } from 'vue-router'


const router = useRouter()


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
const mkhj1=() => {
   router.push("/")
}
</script>

<template>


  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <button type="button" @click=mkhj>count is {{ name1}}</button>
    <button type="button" @click=mkhj1>count is {{ name1}}</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<style scoped>

</style>

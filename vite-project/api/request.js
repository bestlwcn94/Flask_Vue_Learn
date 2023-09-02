// // request.js
//
// import axios from 'axios'
//
// async function validateToken() {
//
//   const token = localStorage.getItem('token')
//
//   try {
//
//     await axios.get('/profile', {headers:{'Authorization': token}})
//
//   } catch (error) {
//
//     console.error('Invalid token')
//
//   }
//
// }
//
// // 添加请求拦截器
// axios.interceptors.request.use(async config => {
//
//   await validateToken()
//
//   return config
//
// }, error => {
//
//   return Promise.reject(error)
//
// })
//
// export default axios
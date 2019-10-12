<template>
  <div id="app" class="container" >
    
    
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  data(){
    return{
    }
  },
  name: 'app',
  
}
</script>

<style>
  #app {
    
    text-align: center;
    direction: rtl;
    text-align: right;
  }
  select {
        margin-left: 800px;
        width: 150px;
  }
</style>

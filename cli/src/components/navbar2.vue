<template>
<div>
<nav class="navbar is-transparent">
  

  <div id="navbarExampleTransparentExample" class="navbar-menu">
    <div id="i-menu" class="navbar-start">
      <router-link :to="{name: 'home'}" class="navbar-item" >الرئيسية</router-link>
      
      <div class="navbar-item has-dropdown is-hoverable">
        <router-link :to="{name: 'items'}" class="navbar-link" >ادارة الأصناف</router-link>
               
        <div class="navbar-dropdown is-boxed">
          <router-link :to="{name: 'items'}" class="navbar-item" >اضافة صنف</router-link>
          <router-link :to="{name: 'items'}" class="navbar-item" >تعديل صنف</router-link>
        </div>
      </div>
        <router-link :to="{name: 'units'}" class="navbar-item" >ادارة الوحدات</router-link>
        <router-link :to="{name: 'items'}" class="navbar-item" >ادارة الأصناف</router-link>
        
      <div class="navbar-item has-dropdown is-hoverable">
        
      </div>
               
        
    </div>
  </div>


  
</nav>
</div>
</template>

<script>
export default {

}
</script>

<style>
  nav {
    direction: rtl;
  }
  #i-menu {
    direction: rtl;
    margin-right: 5px;
  }
</style>
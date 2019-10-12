<template>
<div>

  <ul class="nav nav-pills">
    <li class="nav-item">
      <router-link :to="{name: 'login'}" class="nav-link" active-class='active' exact >تسجيل دخول</router-link>
    </li>
    <li class="nav-item">
      <router-link :to="{name: 'logup'}" class="nav-link" active-class='active' href="#">انشاء حساب</router-link>
    </li>
    
  </ul>
</div>

</template>

<script>
export default {
    
}
</script>


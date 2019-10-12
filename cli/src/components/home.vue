<template>
    <div>
        
        <div class="navbar-brand">
            <a class="navbar-item" href="#">
            <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28">
            </a>
            <router-link v-if="isLogin"  :to="{name: 'home'}"><b-button @click="logout" pill variant="primary">تسجيل الخروج</b-button></router-link>
            <router-link v-else :to="{name: 'login'}"><b-button pill variant="info">تسجيل دخول</b-button></router-link>
            
            
        </div>
        
        <router-view></router-view>
        
    </div>
</template>

<script>
import {mapGetters} from 'vuex'
//import navBar from './navBar'

export default {
    components:{
        //navBar,
        
    },
    data(){
        return{
           
        }
    },
   
    computed:{
        ... mapGetters(['user',"isLogin"]),
        
        },
   
    methods:{
         logout(){
            this.$store.commit('set_user', {})
            this.$cookies.set('user',{});
            this.$store.commit('set_isLogin', false)
            this.$cookies.set('isLogin',false);
            
        },
       
    },
 
    



}
</script>

<style>
    div{
        margin: 15px;
    }
</style>

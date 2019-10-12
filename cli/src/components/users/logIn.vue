<template>
    <div>
        <div class="field">
            <p class="control has-icons-left">
                <input v-model="data.username" :class="addclass" class="input" type="text" placeholder="username">
                <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
                </span>
            </p>
            <p :class="addclass" v-if="addclass=='is-danger'" class="help">اسم المستخدم أو كلمة السر غير صالحة.</p>
        </div>
        <div class="field">
            <p class="control has-icons-left">
                <input v-model="data.password" class="input" type="password" placeholder="كلمة السر">
                <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
                </span>
            </p>
        </div>
        <div class="field">
            <p class="control">
                <button @click="sendData" class="button is-success">
                 تسجيل الدخول
                </button>
            </p>
        </div>
        <b-modal id="modal-center" centered ok-only title="خطأ في تسجيل الدخول">
            <p class="my-10">اسم المستخدم أو كلمة السر غير صالحة.</p>
        </b-modal>
    </div>
</template>

<script>

export default {
    data(){
        return{
            data:{
                username:'',
                password:''
            },
            addclass: ""
        }
    },
    methods:{
        sendData(){
            let data = this.data;
           return this.$https.post('users/login', data)
                    .then(response => {
                        /* eslint-disable no-console */
                        data.username =  ''
                        data.password = ''
                        this.addclass = ""
                        this.login(response.data)
                        
                        }, error => {
                        this.addclass = "is-danger"
                        console.error(error);
                        this.logout()
                        this.$bvModal.show('modal-center')

                        
                         });
        },
        login(value){
            this.$store.commit('set_user', value)
            this.$cookies.set('user',value)
            this.$store.commit('set_isLogin', true)
            this.$cookies.set('isLogin',true);
            this.$router.push({ name: 'user', params: { id: value.id }})

        },
        logout(){
            this.$store.commit('set_user', {})
            this.$cookies.set('user',{});
            this.$store.commit('set_isLogin', true)
            this.$cookies.set('isLogin',false);
        }
        
  

    },
    beforeRouteLeave(to,from,next){
            if(this.$cookies.get('isLogin') == false){
                next({ name: 'logup' })
            }
            else{
                next()
            }

        },
    watch:{
        
    }

}
</script>

<style>

</style>
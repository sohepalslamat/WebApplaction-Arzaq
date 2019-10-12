<template>
  <div>
        <div class="field">
            <label class="label">الاسم</label>
            <div class="control">
                <input v-model="user.first_name" class="input" type="text" placeholder="أدخل الاسم ">
            </div>
        </div>

        <div class="field">
            <label class="label">اسم المستخدم</label>
            <div class="control has-icons-left has-icons-right">
                <input v-model="user.username" :class="class_success" class="input" type="text" placeholder="username">
                <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
                </span>
                <span class="icon is-small is-right">
                <i class="fas fa-check"></i>
                </span>
                <p :class="class_success" v-if="class_success=='is-success'" class="help">اسم المستخدم هذا متاح.</p>
                <p v-else class="help is-danger">اسم المستخدم هذا غير متاح .</p>
            </div>
            
        </div>

        <div class="field">
            <label class="label">كلمة السر</label>
            <div class="control has-icons-left">
                <input  v-model="user.password" class="input" type="password" placeholder="كلمة السر">
                <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
                </span>
            </div>
        </div>

        <div class="field">
            <label class="label">Email</label>
            <div class="control has-icons-left has-icons-right">
                <input  v-model="user.email" class="input" type="email" placeholder="أدخل ايميل" >
                <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
                </span>
                <span class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
                </span>
            </div>
            
        </div>

        <div class="field">
            <label class="label">الصفة</label>
            <div class="control">
                <div class="select">
                <select>
                    <option>Select dropdown</option>
                    <option>With options</option>
                </select>
                </div>
            </div>
        </div>

        
        <div class="field">
            <div class="control">
                <label class="checkbox">
                <input  v-model="user.is_superuser" type="checkbox">
                مستخدم كامل الصلاحيات
                </label>
            </div>
        </div>

        
        <div class="field is-grouped">
            <div class="control">
                <button @click="sendData" class="button is-link">اضافة</button>
            </div>
            <div class="control">
                <button class="button is-text">الغاء</button>
            </div>
        </div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            user: {
                username: '',
                password: '',
                email: '',
                first_name: '',
                is_superuser: false
            },
            class_success: ""
        }
    },
    methods:{
        sendData(){
            let data = this.user;
           return this.$http.post('users/add', data,
           {headers: {'Authorization':'Token '+ this.$cookies.get('user').Authorization}
           })
                    .then(() => {
                        /* eslint-disable no-console */
                        data.username =  ''
                        data.password = ''
                        data.email = ''
                        data.first_name = ''
                        data.is_superuser = false
                        
                        }, error => {
                        
                        console.error(error);
                        
                         });
        }

    },
    watch:{
        user:{
            handler: function(value){
            return this.$http.post('users/checkusername', {username: value.username})
                    .then(response => {
                        /* eslint-disable no-console */
                        console.log(response)
                        if (response.data == false){
                            this.class_success = "is-success"
                        }
                        else{
                            this.class_success = "is-danger"
                        }
                        
                        }, error => {
                        
                        console.error(error);
                        
            });
        },deep:true
        }
    }

}
</script>

<style>

</style>
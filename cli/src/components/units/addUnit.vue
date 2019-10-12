<template>
    <div class="container ">
        <div class="notification">
            <h2 class="title" >اضافة وحدة </h2>
            <div class="field">
                <label class="label">اسم الوحدة</label>
                <div class="control">
                    <input v-model="unit.name" class="input" type="text" placeholder="اسم الوحدة">
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
    </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
    data(){
        return{
            unit:{
                name: ''
            }
            
        }
    },
    computed:{
        ... mapGetters(['user'])
        
    },
    methods:{
        sendData(){
            let data = this.unit;
           return this.$http.post('units/add', data)
                    .then(() => {
                        /* eslint-disable no-console */
                        data.name = '';
                        /* emit event */
                        this.$emit('added')
                        
                        }, error => {
                        
                        console.error(error);
                        
                         });
        }

    }

}
</script>

<style>
    h2 {
        text-align: center;
        
    }
</style>
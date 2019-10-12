<template>
    <div class="container">
        <div class="notification">
            <h2 class="title">تعديل وحدة </h2>
            <div class="field">
                <label class="label">اختر الوحدة التي تريد تعديلها</label>
                <b-form-select v-model="selected" :options="options_unit" class="mb-3">
                    <!-- This slot appears above the options from 'options' prop -->
                    <template v-slot:first>
                        <option :value={} disabled>-- اختر الوحدة --</option>
                    </template>
                </b-form-select>
            </div>
            

            <div class="field">
                <label class="label">اسم الوحدة</label>
                <div class="control">
                    <input v-model="selected.name" class="input" type="text" placeholder="اسم الوحدة">
                </div>
            </div>

            <div class="field is-grouped">
                <div class="control">
                    <button @click="editUnit(selected.id)" class="button is-link">تعديل</button>
                </div>
                <div class="control">
                    <button class="button is-text">الغاء</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data(){
        return{
            units: [],
            selected: {}
            
            
        }
    },
    computed:{
        
        options_unit: function(){
            var x = []
            for( var unit in this.units){
                x.push({ value: this.units[unit], text: this.units[unit].name })
            }
            return x
        }
        
    },
    props:{
        added_event: {}

    },
    created : function() {
        this.getUnits();
        
      },
    watch:{
        added_event: function(){
            this.getUnits();
            
        }
    },
     
    
    methods:{
        getUnits() {
            // GET /someUrl
           return this.$http.get('units').then(response => {
        
                /* eslint-disable no-console */
                this.units = response.data;
                }, error => {
                console.error(error); })    
            },
        editUnit(id){
            let data = this.selected;
            return this.$http.put('units/edit/'+id, data).then(response => {
            
                this.getUnits() 
                /* eslint-disable no-console */
                console.log(response);
                
                }, error => {
                console.error(error); })   
            }
        }

}
</script>

<style>
    h2 {
        text-align: center;
        
    }

</style>
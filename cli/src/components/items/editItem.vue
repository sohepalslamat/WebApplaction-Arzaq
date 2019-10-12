<template>
    <div class="container ">
        <div class="notification">
            <h2 class="title" >تعديل صنف </h2>
            <div class="field">
                <label class="label">اختر اسم الصنف الذي تريد تعديله:</label>
                <b-form-select v-model="item_selected" :options="options_item" class="mb-3">
                    <!-- This slot appears above the options from 'options' prop -->
                    <template v-slot:first>
                        <option :value='{unit: null}' disabled>-- اختر اسم الصنف --</option>
                    </template>
                </b-form-select>
                ------------------------------------------------------------
            </div>
            

            <div class="field">
                <label class="label">اسم الصنف</label>
                <div class="control">
                    <input v-model="item_selected.name" class="input" type="text" placeholder="ادخل اسم الصنف">
                </div>
            </div>

            <div class="field">
                <label class="label">الوحدة</label>
                <b-form-select v-model="item_selected.unit" :options="options_unit" class="mb-3">
                    <!-- This slot appears above the options from 'options' prop -->
                    <template v-slot:first>
                        <option :value='null' disabled>-- اختر الوحدة --</option>
                    </template>
                </b-form-select>
                
            </div>

            <div class="field">
                <label class="label">الكمية الدنيا في المستودع</label>
                <div class="control">
                    <input v-model="item_selected.minimum_quantity" class="input" type="number" placeholder="ادخل الكمية الدنيا في المستودع">
                </div>
            </div>

            <div class="field">
                <label class="label">نسبة الربح الدنيا</label>
                <div class="control">
                    <input v-model="item_selected.minimum_price" class="input" type="number" step="0.01" min="0.00" max="100.00" placeholder="ادخل نسبة الربح الدنيا">
                </div>
            </div>

            <div class="field">
                <label class="label">نسبة الربح </label>
                <div class="control">
                    <input v-model="item_selected.normal_price" class="input" type="number" step="0.01" min="0.00" max="100.00" placeholder="ادخل نسبة الربح">
                </div>
            </div>

            <div class="field">
                <label class="label">الوصف</label>
                <div class="control">
                    <textarea v-model="item_selected.specs" class="textarea" placeholder="الوصف"></textarea>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <label class="checkbox">
                    <input v-model="item_selected.status" type="checkbox">
                    صنف غير متداول
                    </label>
                </div>
            </div>

            <div class="field is-grouped">
                <div class="control">
                    <button @click="editItem(item_selected.id)" class="button is-link">تعديل</button>
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
            items: [],
            units: [],
            item_selected: {unit: null},
            
            
            
        }
    },
    computed:{
        
        options_unit: function(){
            var x = []
            for( var unit in this.units){
                x.push({ value: this.units[unit].id, text: this.units[unit].name })
            }
            return x
        },
        options_item: function(){
            var x = []
            for( var item in this.items){
                x.push({ value: this.items[item], text: this.items[item].name })
            }
            return x
        }
        
    },
    props:{
        added_event: {}

    },
    created : function() {
        this.getUnits();
        this.getItems();
        
      },
    
    watch:{
        added_event: function(){
            this.getUnits();
            this.getItems();
        }
    },
    
    
    methods:{
        getItems() {
            // GET /someUrl
            return this.$http.get('items').then(response => {
        
            /* eslint-disable no-console */
            this.items = response.data;
            }, error => {
            console.error(error); })    
            },
        
        getUnits() {
            // GET /someUrl
            return this.$http.get('units')
            .then(response => {
            /* eslint-disable no-console */
            this.units = response.data;
            }, error => {
            console.error(error); })    
            },
        editItem(id){
            let data = this.item_selected;
            return this.$http.put('items/edit/'+id, data)
            .then(() => {
            this.getItems() 
            this.item_selected = {unit: null}
            /* eslint-disable no-console */
           
            }, error => {
            console.error(error); })   
            }
        }

}
</script>

<style>
   
</style>
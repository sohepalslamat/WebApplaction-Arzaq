<template>
    <div class="container ">
        <div class="notification">
            <h2 class="title" >اضافة صنف </h2>
            <div class="field">
                <label class="label">اسم الصنف</label>
                <div class="control">
                    <input v-model="item.name" class="input" type="text" placeholder="ادخل اسم الصنف">
                </div>
            </div>

            <div class="field">
                <label class="label">الوحدة</label>
                <b-form-select v-model="item.unit" :options="options_unit" class="mb-3">
                    <!-- This slot appears above the options from 'options' prop -->
                    <template v-slot:first>
                        <option :value ='null' disabled>-- اختر الوحدة --</option>
                    </template>
                </b-form-select>
            </div>

            <div class="field">
                <label class="label">الكمية الدنيا في المستودع</label>
                <div class="control">
                    <input v-model="item.minimum_quantity" class="input" type="number" placeholder="ادخل الكمية الدنيا في المستودع">
                </div>
            </div>

            <div class="field">
                <label class="label">الكمية الحالية في المستودع</label>
                <div class="control">
                    <input v-model="item.quantity" class="input" type="number" placeholder="ادخل الكمية الحالية في المستودع">
                </div>
            </div>

            <div class="field">
                <label class="label">التكلفة الحالية للصنف</label>
                <div class="control">
                    <input v-model="item.cost" class="input" type="number" step="0.01" placeholder="ادخل التكلفة الحالية للصنف">
                </div>
            </div>

            <div class="field">
                <label class="label">نسبة الربح الدنيا</label>
                <div class="control">
                    <input v-model="item.minimum_price" class="input" type="number" step="0.01" min="0.00" max="100.00" placeholder="ادخل نسبة الربح الدنيا">
                </div>
            </div>

            <div class="field">
                <label class="label">نسبة الربح </label>
                <div class="control">
                    <input v-model="item.normal_price" class="input" type="number" step="0.01" min="0.00" max="100.00" placeholder="ادخل نسبة الربح">
                </div>
            </div>

            <div class="field">
                <label class="label">الوصف</label>
                <div class="control">
                    <textarea  v-model="item.specs" class="textarea" placeholder="الوصف"></textarea>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <label class="checkbox">
                    <input v-model="item.status" type="checkbox">
                    صنف غير متداول
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
        
    </div>
</template>

<script>

export default {
    data(){
        return{
            item:{
                name: '',
                specs:'',
                unit: null,
                minimum_quantity: 0,
                quantity: 0,
                cost: 0.00,
                minimum_price: 0.00,
                normal_price: 0.00,
                status: false
            },
            units:[],
            
            
        }
    },
    computed:{
        
        options_unit: function(){
            var x = []
            for( var unit in this.units){
                x.push({ value: this.units[unit].id, text: this.units[unit].name })
            }
            return x
        }
        
    },
    created : function() {
        this.getUnits();
        
      },
        
    methods:{
        getUnits() {
            // GET /someUrl
            this.$http.get('units')
                .then(response => {
                /* eslint-disable no-console */
                this.units = response.data;
                }, error => {
                console.error(error); })    
            },
        sendData(){
            let data = this.item;
           return this.$http.post('items/add', data)
                    .then(() => {
                        /* eslint-disable no-console */
                        
                        data.name = '';
                        data.specs = '';
                        data.cost = 0.00;
                        data.minimum_quantity = 0,
                        data.minimum_price = 0,
                        data.normal_price = 0,
                        data.unit = 1,
                        data.status = false
                        data.quantity = 0

                        /* emit event */
                        this.$emit('added')

                        /*message*/
                        
                        }, error => {
                        
                        console.error(error);
                        
                         });
        }

    }

}
</script>

<style>
 
</style>
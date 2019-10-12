<template>
    <div id="i-container">
    <div class="tabs is-centered is-boxed">
        <ul>
            <li :class="addUnit" @click="selected('addUnit')" >
            <a>
                <span class="icon is-small"><i class="fas fa-coins" aria-hidden="true"></i></span>
                <span>اضافة وحدة</span>
            </a>
            </li>
            <li :class="editUnit" @click="selected('editUnit')">
            <a>
                <span class="icon is-small"><i class="fas fa-balance-scale" aria-hidden="true"></i></span>
                <span>تعديل وحدة</span>
            </a>
            </li>
        </ul>
    </div>
    <keep-alive>
    <component v-if="addUnit" @added='added_val=!added_val' :is="comp" ></component>
    <component v-else-if="editUnit" :added_event='added_val' :is="comp" ></component>
    </keep-alive>
    </div>
</template>

<script>
import addUnit from './addUnit'
import editUnit from './editUnit'
export default {
    data(){
        return{
            comp: 'addUnit',
            is_active: true,
            editUnit: '',
            addUnit: 'is-active',
            added_val: true
        }
    },
    components: {
    addUnit,
    editUnit
       
  },
  methods:{
      selected(x){
          this.comp = x;
          if(x == 'addUnit'){
              this.addUnit = 'is-active';
              this.editUnit = '';
              
          }
          else if(x == 'editUnit'){
              this.editUnit = 'is-active';
              this.addUnit = '';
              
          }
      }
  }

}
</script>

<style>
    #i-container{
        margin-left: 10%;
        margin-right: 10%;
    }
</style>
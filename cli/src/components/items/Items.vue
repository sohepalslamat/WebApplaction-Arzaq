<template>
    <div id="i-container">
    <div class="tabs is-centered is-boxed">
        <ul>
            <li :class="addItem" @click="selected('addItem')" >
            <a>
                <span class="icon is-small"><i class="fas fa-image" aria-hidden="true"></i></span>
                <span>اضافة صنف</span>
            </a>
            </li>
            <li :class="editItem" @click="selected('editItem')">
            <a>
                <span class="icon is-small"><i class="fas fa-music" aria-hidden="true"></i></span>
                <span>تعديل صنف</span>
            </a>
            </li>
        </ul>
    </div>
    <keep-alive>
    <component v-if="addItem" @added='added_val=!added_val' :is="comp" ></component>
    <component v-else-if="editItem" :added_event='added_val' :is="comp" ></component>
    </keep-alive>
    </div>
</template>

<script>
import addItem from './addItem'
import editItem from './editItem'
export default {
    data(){
        return{
            comp: 'addItem',
            is_active: true,
            editItem: '',
            addItem: 'is-active',
            added_val: true
        }
    },
    components: {
    addItem,
    editItem
       
  },
  methods:{
      selected(x){
          this.comp = x;
          if(x == 'addItem'){
              this.addItem = 'is-active';
              this.editItem = '';
              
          }
          else if(x == 'editItem'){
              this.editItem = 'is-active';
              this.addItem = '';
              
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
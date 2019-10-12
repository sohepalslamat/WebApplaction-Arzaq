<template>
  <div >
    
  </div>
</template>

<script>
  export default {
    data() {
      return {
        boxOne: '',
        boxTwo: ''
      }
    },
    props:{
      showMsg : {type:[Boolean,], default: false},
      titleMsg : {type:[String,], default: 'تنبيه' },
      textMsg : {type:[String,], default: 'تم بنجاح' }

    },
    watch:{
        showMsg: function(val){
          if (val){
            this.showMsgBoxSuccess()
            }
          
            
        }
    },
    methods: {
      showMsgBoxSuccess() {
        this.$bvModal.msgBoxOk(this.textMsg, {
            title: this.titleMsg,
            size: 'bt',
            buttonSize: 'bt',
            okVariant: 'success',
            headerClass: 'p-2 border-bottom-0',
            footerClass: 'p-2 border-top-0',
            centered: true
            })
          .then(value => {
            /* eslint-disable no-console */
            this.boxOne = value
          })
          .catch(error => {
            // An error occurred
            console.error(error);
          })
      },
      showMsgBoxTwo() {
        this.boxTwo = ''
        this.$bvModal.msgBoxOk('Data was submitted successfully', {
          title: 'Confirmation',
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'success',
          headerClass: 'p-2 border-bottom-0',
          footerClass: 'p-2 border-top-0',
          centered: true
        })
          .then(value => {
            /* eslint-disable no-console */
            this.boxTwo = value
          })
          .catch(error => {
            // An error occurred
            console.error(error);
          })
      }
    }
  }
</script>
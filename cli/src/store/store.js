import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const store = new Vuex.Store({
    state:{
        user: {},
        isLogin: false

    },
    getters:{
        user(state){
            return state.user;
        },
        isLogin(state){
            return state.isLogin
        }
    },
    mutations:{
        set_user(state,user){
            return state.user = user;
        },
        set_isLogin(state, isLogin){
            return state.isLogin = isLogin
        }
    }
})

export default store
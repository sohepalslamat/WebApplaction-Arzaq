import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const store = new Vuex.Store({
    state:{
        user: window.$cookies.get("user"),
        isLogin: window.$cookies.get("isLogin")

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
            state.user = user
            window.$cookies.set('user',user)
        },
        set_isLogin(state, isLogin){
            state.isLogin = isLogin
            window.$cookies.set('isLogin',isLogin);
        }
    },
    actions:{
        set_user({commit}, user){
            commit('set_user', user)
        },
        set_isLogin({commit} ,isLogin){
            commit('set_isLogin', isLogin)
        }
    }
})

export default store
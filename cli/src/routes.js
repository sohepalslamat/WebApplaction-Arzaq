import Units from './components/units/Units'
import Items from './components/items/Items'
import home from './components/home'
import logIn from './components/users/logIn'
import logUp from './components/users/logUp'
import users from './components/users/users'


const routes = [
    
    {path:'/home', component: home, name: 'home',
        children:[
            
                {path:'login', component: logIn, name: 'login'},
                {path:'logup', component: logUp, name: 'logup'},
            
            
            {path:':id',component: users, name: 'user', props: true, beforeEnter: (to, from, next) => {
                /* eslint-disable no-console */
                if(window.$cookies.get('user').id != to.params.id){
                        next({name:'home'})
                    }
                else{
                    next()
                    }
                },
                children:[
            
                {path:'units', component: Units, name: 'units'},
                {path:'items', component: Items, name: 'items'},
            ]},
            {path:'*', redirect:'/'}
    ]}

]
export default routes
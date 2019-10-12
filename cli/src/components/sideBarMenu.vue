<template>
    <nav :class= "{'menu': true ,'menu-open': !show}">
        <span @click="show = !show" :class= "{'close-btn': true, 'open-btn': !show}">X</span>
        <ul id="father">
            <h1>MAIN MENU</h1>
            <li> Item 01</li>
            <li @mouseenter="showson = true" @mouseleave="showson = false"> Item 02
                <ul id="son" v-show="showson">
                    <li> Item 01</li>
                    <li> Item 02</li>
                    <li> Item 03</li>
                </ul>
            </li>
            <li> Item 03</li>
            <li> Item 04</li>
            <li> Item 05</li>                
        </ul>
    </nav>
  
</template>

<script>
export default {
    data(){
        return{
            show: true,
            showson: true
        }
    },
    methods: {
        
    }

}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Varela+Round');


* {
    margin: 0px;
    padding: 0px;
    font-family: 'Varela Round', sans-serif;
    -webkit-font-smoothing: antialiased; 
}

    h1{
    text-align: center;
    padding: 16px;
}
.menu{
    position: relative;
    float: left;
    left: -260px;
    width: 260px;
    height: 100vh;
    background-color: crimson;
    color: white;
    z-index: 999;
    transition: all 0.5s;
}

.menu-open{
    left: 0px;
    background-color: midnightblue;
}

.close-btn {
    display: block;
    height: 60px;
    font-size: 30px;
    float: right;
    padding: 0 10px;
    background-color: crimson;
    cursor: pointer;
    position: absolute;
    left: 260px;
    line-height: 60px;
    transition: all 0.5s;
}


.open-btn {
    background-color: midnightblue;
}

#father > li {
    list-style-type: none;
    text-align: center;
    line-height: 60px;
    cursor: pointer;
    border-bottom: 1px solid darkgrey;
}

li:hover {
    background-color: darkgray;
    color: black;
}
#son {
    list-style-type: none;
    width: 100% !important;
    
}

#son > li {
    background-color: darkgray;
    color: black;
}
#son > li:hover{
    background-color: crimson;
}

.content{
    position: relative;
    background-color: #eee;
    height: 60px;
    box-sizing: border-box;
}
/*
.image{
    position: relative;
    height: 360px;
    background-image: url(../imgs/burger.jpeg);
    background-size: cover;
    background-position: center;
}
*/
.content {
    width: 100vw;
    left: 0px;
}
</style>
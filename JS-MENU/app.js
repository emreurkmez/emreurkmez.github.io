changemenu=true

var containerMenu=()=>{
    var menuContent=document.querySelector(".menuContent")
    if(changemenu==true){
        menuContent.style.display="flex"
    }else{
        menuContent.style.display="none"
        
    }
    changemenu= !changemenu
}
changedrop = true;
var drop =()=>{
    var containerDrop = document.querySelector(".containerDrop")
    if(changedrop==true){
        containerDrop.style.display="flex"
    }else{
        containerDrop.style.display="none"
    }
    changedrop=!changedrop
}

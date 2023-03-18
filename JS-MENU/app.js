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
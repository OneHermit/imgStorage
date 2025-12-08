// 给window 增加自定义的功能
window.$ = function(cssSelector){
   let domObj = document.querySelector(cssSelector)
   domObj.css = function(key,value){
        domObj.style[key] = value
   }
   return domObj
}
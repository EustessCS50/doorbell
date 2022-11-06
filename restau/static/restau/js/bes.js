const toggleBtn = document.querySelector(".toggle-btn")
toggleBtn.addEventListener("click", function(){
    document.querySelector(".topnav-right").classList.toggle("close")
})
toggleBtn.addEventListener("click", function(){
    document.querySelector(".topnav").classList.toggle("lock")
})
const navSlide = () =>{
    const burger = document.querySelector(".burger"); 
    const nav = document.querySelector(".nav-links");
    const navLinks =document.querySelectorAll('.nav-links li');
burger.addEventListener('click', () => {
    //Toggle navbar
    nav.classList.toggle("nav-active");

    //animate links
    navLinks.forEach((link, index)=>{
        if (link.style.animation){
            link.style.animation = ''
        } else {
            link.style.animation = `navLinkFade 1s ease forwards ${index / 7 }s`;
        }
    });

    //Burger animations 
    burger.classList.toggle('toggle'); 

});
}

navSlide()

  

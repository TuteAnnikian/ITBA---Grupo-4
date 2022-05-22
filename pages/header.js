window.addEventListener('scroll', function () {
    var header = document.querySelector('header');
    var anchor = document.querySelector('a')
    var imageNone = document.querySelector('.logo');
    var scrollDos = document.querySelector('.logo-2');
    var toggle = document.querySelector('.hamburger');
    header.classList.toggle('abajo', window.scrollY > 20);
    anchor.classList.toggle('abajo', window.scrollY > 20);
    imageNone.classList.toggle('abajo', window.scrollY > 20);
    scrollDos.classList.toggle('abajo', window.scrollY > 20);
    toggle.classList.toggle('abajo', window.scrollY > 20)
    
  });

 
  const hamburgerMenu = document.querySelector('.hamburger');
  const menuIsActive = () => {
    hamburgerMenu.classList.toggle('active');
  };
  hamburgerMenu.addEventListener('click', menuIsActive);
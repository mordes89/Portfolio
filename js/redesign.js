(() => {
 const root=document.documentElement, buttons=[...document.querySelectorAll('.theme-btn')];
 function theme(value){if(!buttons.some(b=>b.dataset.theme===value))return;root.dataset.theme=value;buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.theme===value)));}
 try{theme(localStorage.getItem('mike-portfolio-theme'));}catch(_){}
 buttons.forEach(b=>b.addEventListener('click',()=>{theme(b.dataset.theme);try{localStorage.setItem('mike-portfolio-theme',b.dataset.theme);}catch(_){}}));
 const menu=document.querySelector('#navToggle'), nav=document.querySelector('#navLinks');
 function close(){nav.classList.remove('active');menu.setAttribute('aria-expanded','false');}
 menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';nav.classList.toggle('active',open);menu.setAttribute('aria-expanded',String(open));});
 nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('active')){close();menu.focus();}});
 if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.remove('pending');observer.unobserve(e.target);}}),{threshold:.06});document.querySelectorAll('.reveal').forEach(el=>{if(el.getBoundingClientRect().top>innerHeight){el.classList.add('pending');observer.observe(el);}});}
})();

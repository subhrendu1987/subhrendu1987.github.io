// Announcement Slider Section
var announcementSwiper = new Swiper('.announcement-slider', {
    slidesPerView: 1,
    spaceBetween: 40,
    navigation: {
        nextEl: '#announcement-swiper-button-next',
        prevEl: '#announcement-swiper-button-prev',
    },
        pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1024: { slidesPerView: 1 },
        480: { slidesPerView: 1 }
    },
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    loop: true,
});


// Faculty Slider Section
var facultySwiper = new Swiper('#faculty-slider', {
    slidesPerView: 1,
    spaceBetween: 40,
    navigation: {
        nextEl: '#faculty-swiper-button-next',
        prevEl: '#faculty-swiper-button-prev',
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1024: { slidesPerView: 3 },
        480: { slidesPerView: 1 }
    },
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    loop: true,
});

// Programs slider section
var programSwiper = new Swiper('.programs-slider', {
    slidesPerView: 1,
    spaceBetween: 40,
    navigation: {
        nextEl: '.program-next',
        prevEl: '.program-prev',
    },
        pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1024: { slidesPerView: 3 },
        768: { slidesPerView: 2 },
        480: { slidesPerView: 1 }
    },
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    infinite: true,
    loop: true,
})

// Event Slider Section
var eventSwiper = new Swiper('#event-slider', {
    slidesPerView: 1,
    spaceBetween: 40,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1024: { slidesPerView: 2 },
        480: { slidesPerView: 1 }
    },
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    infinite: true,
    loop: true,
});


// Research Slider Section
var researchSwiper = new Swiper('#research-slider', {
    slidesPerView: 1,
    spaceBetween: 30,
    navigation: {
        nextEl: '#sau-media-next',
        prevEl: '#sau-media-prev',
    },
        pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1024: { slidesPerView: 5 },
        480: { slidesPerView: 1 }
    },
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    infinite: true,
    loop: true,
});

// Sau Video slider section
var videoSwiper = new Swiper('#sau-video-slider', {
    slidesPerView: 1,
    spaceBetween: 40,
    navigation: {
        nextEl: '#sau-campus-next',
        prevEl: '#sau-campus-prev',
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        1024: { slidesPerView: 3 },
        480: { slidesPerView: 1 }
    },
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    infinite: true,
    loop: true,
});


// Testimonial Section

let currentTestimonialIndex = 0;
let testimonials = document.querySelectorAll(".testimonial-card");
let testimonialContent = document.getElementById("testimonial-content");
let autoSlideInterval;
let restartTimeout;

function showTestimonial(element) {
    let img = element.getAttribute('data-image');
    let title = element.getAttribute("data-title");
    let content = element.getAttribute("data-content");
    let name = element.getAttribute("data-name");
    let course = element.getAttribute("data-course");

    // Remove animation before changing content
    testimonialContent.classList.remove("testimonial-show");

    // Wait before changing the content
    setTimeout(() => {
        testimonialContent.innerHTML = `
            <div class="testimonial-info">
                <img src="${img}" alt="">
            </div>
            <div class="testimonial-details">
                <h3 class="text-3xl">${name}</h3>
                <h4 class="text-2xl text-golden-yellow">${course}</h4>
                <p class="text-2xl">${content}</p>
            </div>
        `;
        testimonialContent.classList.add("testimonial-show");
    }, 300);

    // Reset Auto-Slide Timer
    clearInterval(autoSlideInterval);
    clearTimeout(restartTimeout);
    restartTimeout = setTimeout(startAutoSlide, 10000); // Restart after 10s
}

// Function to automatically switch testimonials
function autoSlideTestimonials() {
    currentTestimonialIndex = (currentTestimonialIndex + 1) % testimonials.length;
    showTestimonial(testimonials[currentTestimonialIndex]);
}

// Start the auto-slide feature
function startAutoSlide() {
    autoSlideInterval = setInterval(autoSlideTestimonials, 5000); // Change every 5s
}

// Initialize auto-slide when page loads
startAutoSlide();


// Initialize Fancybox (for lightbox)
Fancybox.bind('[data-fancybox="gallery"]', {
    // Additional settings (optional)
    infinite: true,
    buttons: ['zoom', 'slideShow', 'fullScreen', 'close'],
});
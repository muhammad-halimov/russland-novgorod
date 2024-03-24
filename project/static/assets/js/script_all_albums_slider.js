
const sliders = document.querySelectorAll('.carousel');

sliders.forEach((slider) => {
  const prevButton = slider.querySelector('.carousel-control-prev');
  const nextButton = slider.querySelector('.carousel-control-next');

  const images = slider.querySelectorAll('.pic');

  let currentSlideIndex = 0;

  prevButton.addEventListener('click', () => {
    currentSlideIndex--;
    if (currentSlideIndex < 0) {
      currentSlideIndex = images.length - 1;
    }
    showSlide();
  });

  nextButton.addEventListener('click', () => {
    currentSlideIndex++;
    if (currentSlideIndex >= images.length) {
      currentSlideIndex = 0;
    }
    showSlide();
  });

  function showSlide() {
    images.forEach((image) => {
      image.style.display = 'none';
    });
    images[currentSlideIndex].style.display = 'block';
  }
});

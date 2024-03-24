// Получаем все слайды и кнопки переключения
let slides = document.querySelectorAll('.pic');
let prevButton = document.getElementById('back');
let nextButton = document.getElementById('next');

let currentSlideIndex = 0; // Текущий индекс слайда

// Функция для отображения текущего слайда и скрытия остальных
function showSlide(index) {
    for (let i = 0; i < slides.length; i++) {
        if (i === index) {
            slides[i].style.display = 'block';
        } else {
            slides[i].style.display = 'none';
        }
    }
}

// Функция для перехода к предыдущему слайду
function goBack() {
    currentSlideIndex--;
    if (currentSlideIndex < 0) {
        currentSlideIndex = slides.length - 1;
    }
    showSlide(currentSlideIndex);
}

// Функция для перехода к следующему слайду
function goNext() {
    currentSlideIndex++;
    if (currentSlideIndex >= slides.length) {
        currentSlideIndex = 0;
    }
    showSlide(currentSlideIndex);
}

// Устанавливаем обработчики событий для кнопок переключения
prevButton.addEventListener('click', goBack);
nextButton.addEventListener('click', goNext);

// Показываем первый слайд при загрузке страницы
showSlide(currentSlideIndex);

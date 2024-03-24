//динамическая подгрузка изображения на странице для загрузки фото
const input = document.getElementById("id_photo");
const imgContainer = document.getElementById("photo_review_block_img");

let rotation = 0; // сохранение текущего угла поворота

input.addEventListener("change", async(e) => {
    const selectedFile = e.target.files;

    if (selectedFile.length > 0) {
        const [imageFile] = selectedFile;
        const isImageType = imageFile.type.startsWith('image/') || imageFile.type === 'dng' || imageFile.type === 'raw';


        if (isImageType) {
            const fileReader = new FileReader();

            fileReader.onload = () => {
                const srcData = fileReader.result;
                const img = new Image();
                img.src = srcData.toString();

                imgContainer.innerHTML = '';
                imgContainer.append(img);

                let image = imgContainer.querySelector('img');
                let isDragging = false;
                let prevX, prevY;

                // определение мин масштаба
                let minScale = Math.max(imgContainer.offsetWidth / image.offsetWidth, imgContainer.offsetHeight / image.offsetHeight);

                image.style.transform = "scale(" + minScale + ")";
                image.style.minWidth = imgContainer.offsetWidth + "px";
                image.style.minHeight = imgContainer.offsetHeight + "px";

                // зум колесиком
                imgContainer.addEventListener("wheel", function(e) {
                    let scale;
                    let delta = e.deltaY;

                    if (delta > 0) {
                        scale = image.style.transform.replace("scale(", "").replace(")", "");
                        scale = scale ? parseFloat(scale) : 1;
                        scale -= 0.1;
                        image.style.transform = "scale(" + scale + ") rotate(" + rotation + "deg)"; // применяем поворот после изменения scale
                    } else {
                        scale = image.style.transform.replace("scale(", "").replace(")", "");
                        scale = scale ? parseFloat(scale) : 1;
                        scale += 0.1;
                        image.style.transform = "scale(" + scale + ") rotate(" + rotation + "deg)"; // применяем поворот после изменения scale
                    }

                    e.preventDefault();
                });

                // перетаскивание изображения
                image.addEventListener("mousedown", function(e) {
                    isDragging = true;
                    prevX = e.clientX;
                    prevY = e.clientY;

                    e.preventDefault();
                });

                document.addEventListener("mousemove", function(e) {
                    if (isDragging) {
                        let newX = prevX - e.clientX;
                        let newY = prevY - e.clientY;
                        prevX = e.clientX;
                        prevY = e.clientY;

                        image.style.left = (image.offsetLeft - newX) + "px";
                        image.style.top = (image.offsetTop - newY) + "px";
                    }
                });

                document.addEventListener("mouseup", function() {
                    isDragging = false;
                });
            };

            fileReader.readAsDataURL(imageFile);
        }
    }
});

// поворот
const rotationSelect = document.getElementById("rotation-range");
rotationSelect.addEventListener("change", function() {
    const selectedRotation = rotationSelect.value;
    rotation = selectedRotation; 
    applyRotation(selectedRotation);
});
function applyRotation(rotation) {
    let image = imgContainer.querySelector('img');
    image.style.transform = "scale(" + getScale() + ") rotate(" + rotation + "deg)"; 
}
function getScale() {
    let image = imgContainer.querySelector('img');
    let scale = image.style.transform.replace("scale(", "").replace(")", "");
    return scale ? parseFloat(scale) : 1;
}

// яркость и контрастность
const brightnessSelect = document.getElementById("brightness-range");
const contrastSelect = document.getElementById("contrast-range");

brightnessSelect.addEventListener("change", function() {
  const selectedBrightness = brightnessSelect.value;
  const selectedContrast = contrastSelect.value;
  applyBrightnessAndContrast(selectedBrightness, selectedContrast);
});

contrastSelect.addEventListener("change", function() {
  const selectedBrightness = brightnessSelect.value;
  const selectedContrast = contrastSelect.value;
  applyBrightnessAndContrast(selectedBrightness, selectedContrast);
});

function applyBrightnessAndContrast(brightness, contrast) {
  imgContainer.querySelector('img').style.filter = `brightness(${brightness}) contrast(${contrast})`;
}



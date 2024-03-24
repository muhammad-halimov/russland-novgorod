//динамическая подгрузка видео на странице для загрузки видео
const inputVideo = document.getElementById("id_video");
const videoContainer = document.getElementById("video_review_block");
inputVideo.addEventListener("change", function(e) {
    videoContainer.src= URL.createObjectURL(e.target.files[0]);
});
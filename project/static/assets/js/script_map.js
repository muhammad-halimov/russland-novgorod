let paths = document.querySelectorAll('.district');
let resultBlock = document.getElementById('map_click_result');
resultBlock.style.display = "block";

paths.forEach(function(path) {
    path.addEventListener('click', function() {
        let districtName = path.getAttribute('data-name');

        sendAsyncLocation(districtName).then(async (data) => {
            console.log(data); // JSON data parsed by data.json() call
            mapPageRender(data.region);
        });
    });
});

let mapPageRender = (region) => {
    window.location.href = "/map/" + region + "/";
}

let sendAsyncLocation = async (data = '') => {
    let url = "/map_ajax/";

    const response = await fetch(url,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify({'region': data}),
        });
    return response.json();
}
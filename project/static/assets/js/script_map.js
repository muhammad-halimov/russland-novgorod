let paths = document.querySelectorAll('.district');
let resultBlock =document.getElementById('map_click_result');

paths.forEach(function(path) {
  path.addEventListener('click', function() {
    let districtName = path.getAttribute('data-name');
    let districtElement = document.getElementById('districtName');
    resultBlock.style.display="block";
    districtElement.textContent = districtName;

    // alert(districtName)

    // sendAsyncLocation("http://127.0.0.1:8000/map/", districtName).then((data) => {
    //   console.log(data); // JSON data parsed by data.json() call
    // });

  });
});

// let sendAsyncLocation = async (url = "", data = '') =>
// {
//   // Example POST method implementation:
//   // Default options are marked with *
//   const response = await fetch(url,
//       {
//         method: "POST", // *GET, POST, PUT, DELETE, etc.
//         headers: {
//           "Content-Type": "application/json", // 'Content-Type': 'application/x-www-form-urlencoded'
//           "X-CSRFToken": csrftoken,
//         },
//         body: JSON.stringify({'region': data}), // body data type must match "Content-Type" header
//       });
//   return response.json(); // parses JSON response into native JavaScript objects
// }
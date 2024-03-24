var btnAdd = document.getElementById("add_collaborator");
btnAdd.addEventListener("click", addName);

function addName() {
  var inputName = document.getElementById("collabName");
  var nameValue = inputName.value;
  
  if (nameValue.trim() === "") {
    return; 
  }
  
  var collaboratorsList = document.getElementById("collabolators_list");
  var newLi = document.createElement("li");
  newLi.classList.add("collabolator");
  newLi.innerHTML = '@' + nameValue + ' <input type="submit" name="remove_collaborator" value="×" class="del_collaborator_btn">';
  
  collaboratorsList.appendChild(newLi);

  inputName.value = ""; 
}


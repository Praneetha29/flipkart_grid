// document.getElementById("save-button").addEventListener("click", function () {
//   var text = document.getElementById("text-input").value;
//
//   // Send the text to the backend using an HTTP request (AJAX)
//   var xhr = new XMLHttpRequest();
//   xhr.open("POST", "/save-text/", true);
//   xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
//   xhr.send(JSON.stringify({ text: text }));
// });
//
// const dropArea = document.querySelector(".drag-area"),
//   dragText = dropArea.querySelector("header"),
//   button = dropArea.querySelector("button"),
//   input = dropArea.querySelector("input");
// let files = [];
//
// button.onclick = () => {
//   input.click();
// };

input.addEventListener("change", function () {
  files = this.files;
  dropArea.classList.add("active");
  showFiles();
});

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload Files";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload Files";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  files = event.dataTransfer.files;
  showFiles();
});

function showFiles() {
  dropArea.innerHTML = "";

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    let fileType = file.type;
    let validExtensions = [
      "image/jpeg",
      "image/jpg",
      "image/png",
      "application/pdf",
      "text/plain",
      "application/vnd.ms-powerpoint",
      "application/vnd.openxmlformats-officedocument.presentationml.presentation",
      "application/vnd.ms-excel",
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "text/csv",
    ];

    if (validExtensions.includes(fileType)) {
      let fileReader = new FileReader();
      fileReader.onload = () => {
        let fileURL = fileReader.result;
        let fileContent;

        if (fileType.startsWith("image")) {
          fileContent = `<img src="${fileURL}" alt="image">`;
        } else if (fileType === "application/pdf") {
          fileContent = `<embed src="${fileURL}" type="application/pdf" width="100%" height="100%">`;
        } else {
          fileContent = `<p>Uploaded file: ${file.name}</p>`;
        }

        dropArea.innerHTML += fileContent;
      };
      fileReader.readAsDataURL(file);
    } else {
      alert(`File ${file.name} is not a valid file type!`);
    }
  }
}

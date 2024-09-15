// getting all required elements
const searchWrapper = document.querySelector(".form-inline");
const inputBox = searchWrapper.querySelector(".form-control");
const suggBox = document.createElement("ul");
suggBox.classList.add("autocom-box");
searchWrapper.appendChild(suggBox);

// Sample array for suggestions
const suggestions = [
    "RGUKT",
    "about rgukt"
];
const suggestions1 = [
    "python Introduction",
    "Flow control",
    "Functions",
    "File Handling",
    "class&objects",
    "Examples"
];
const suggestions2 = [
    "SQL Introduction",
    "SQL SELECT(I)",
    "SQL SELECT(II)",
    "SQL JOIN",
    "SQL Database",
    "SQL Insert and Delete"
];

// if user presses any key and releases
inputBox.addEventListener("input", (e) => {
    let userData = e.target.value; // user entered data
    let emptyArray = [];

    if (userData) {
        emptyArray = suggestions.filter((data) => {
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });

        // If suggestions1 is not empty, concatenate it with emptyArray
        if (suggestions1.length > 0) {
            emptyArray = emptyArray.concat(suggestions1.filter((data) => {
                return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
            }));
        }

        // If suggestions2 is not empty, concatenate it with emptyArray
        if (suggestions2.length > 0) {
            emptyArray = emptyArray.concat(suggestions2.filter((data) => {
                return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
            }));
        }

        emptyArray = emptyArray.map((data) => {
            return '<li class="suggestion">' + data + '</li>';
        });

        suggBox.innerHTML = emptyArray.join('');
        searchWrapper.classList.add("active"); // show autocomplete box
    } else {
        searchWrapper.classList.remove("active"); // hide autocomplete box
        suggBox.innerHTML = "";
    }
});

// Click event on suggestion
suggBox.addEventListener("click", (e) => {
    if (e.target.className === "suggestion") {
        inputBox.value = e.target.textContent;
        searchWrapper.classList.remove("active"); // hide autocomplete box
        suggBox.innerHTML = "";

        let webLink;

        if (suggestions.includes(inputBox.value)) {
            webLink = '/about_rgukt';
        } else if (suggestions1.includes(inputBox.value)) {
            webLink = '/python';
        } else if (suggestions2.includes(inputBox.value)) {
            webLink = '/sql_intro';
        }

        window.location.href = webLink;
    }
});

// Hide suggestions on outside click
document.addEventListener("click", (e) => {
    if (!searchWrapper.contains(e.target)) {
        searchWrapper.classList.remove("active");
        suggBox.innerHTML = "";
    }
});

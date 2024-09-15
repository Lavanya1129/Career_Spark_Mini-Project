var suggestions = [
    "RGUKT",
    "about rgukt"
];
var suggestions1 = [
    "python Introduction",
    "Flow control ",
    "Functions",
    "File Handling ",
    "class&objects ",
    "Examples"
];
var suggestions2 = [
    "SQL Introduction",
    "SQL SELECT(I)",
    "SQL SELECT(II)",
    "SQL JOIN",
    "SQL Database",
    "SQL Insert and Delete"
];

// getting all required elements
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
let linkTag = searchWrapper.querySelector("a");
let webLink;

// Sample array for suggestions
// const suggestions = ["Introduction", "Control Statements", "Object Class", "Inheritance", "Polymorphism", "Abstraction", "Encapsulation", "Examples"];

// if user press any key and release
inputBox.onkeyup = (e) => {
    let userData = e.target.value; // user entered data
    let emptyArray = [];

    if (userData) {
        icon.onclick = () => {
            if (webLink) {
                linkTag.setAttribute("href=#about rgukt", webLink);
                linkTag.click();
            }
        }

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
            return '<li>' + data + '</li>';
        });

        searchWrapper.classList.add("active"); // show autocomplete box
        showSuggestions(emptyArray);

        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            allList[i].setAttribute("onclick", "select(this)");
        }
    } else {
        searchWrapper.classList.remove("active"); // hide autocomplete box
    }
}

function select(element) {
    let selectUserData = element.textContent;
    inputBox.value = selectUserData; // passing the user-selected list item data in textfield
    if (suggestions.includes(selectUserData)) {
        webLink = '/about_rgukt';
    } else if (suggestions1.includes(selectUserData)) {
        webLink = 'python.html';
    } else if (suggestions2.includes(selectUserData)) {
        webLink = 'sql_intro.html';
    }
    icon.click();
    searchWrapper.classList.remove("active");
}

function showSuggestions(list) {
    let listData;
    if (!list.length) {
        userValue = inputBox.value;
        listData = '<li>' + userValue + '</li>';
    } else {
        listData = '<ul>' + list.join('') + '</ul>';
    }
    suggBox.innerHTML = listData;
}

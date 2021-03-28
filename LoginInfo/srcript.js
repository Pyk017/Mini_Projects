//variable to store number of entries done dynamically
let numberOfStudents = 0;

//function will validate all inputs in student enrollment form
function validate() {
    if (document.getElementById("nameId").value == "") {
        alert("Please provide your name!");
        document.getElementById("nameId").focus();
        return false;
    }
    if (document.getElementById("emailId").value == "") {
        alert("Please provide your Email!");
        document.getElementById("emailId").focus();
        return false;
    }
    else {
        var emailID = document.getElementById("emailId").value;
        atpos = emailID.indexOf("@");
        dotpos = emailID.lastIndexOf(".");

        if (atpos < 1 || (dotpos - atpos < 2)) {
            alert("Please enter correct email ID")
            document.getElementById('emailId').focus();
            return false;
        }
    }
    if (document.getElementById("websiteId").value == "") {
        alert("Please provide your website!");
        document.getElementById("websiteId").focus();
        return false;
    }
    else {
        let website = document.getElementById("websiteId").value;
        let expression = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi;
        let regex = new RegExp(expression);

        if(website.match(regex) == false){
            alert("Please enter correct website!");
            document.getElementById("websiteId").focus();
            return false;
        }

    }
    if (document.getElementById("linkId").value == "") {
        alert("Please provide your image link!");
        document.getElementById("linkId").focus();
        return false;
    }
    else {
        let imageLink = document.getElementById("linkId").value;
        let expression = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi;
        let regex = new RegExp(expression);

        if(imageLink.match(regex) == false){
            alert("Please enter correct image link!");
            document.getElementById("linkId").focus();
            return false;
        }
    }
    if ((document.getElementById("gridRadios1").checked == false) &&
        (document.getElementById("gridRadios2").checked == false)) {
        alert("Please choose your Gender: Male or Female");
        return false;
    }
    if ((document.getElementById("inlineCheckbox1").checked == false) &&
        (document.getElementById("inlineCheckbox2").checked == false) &&
        (document.getElementById("inlineCheckbox3").checked == false)) {
        alert("Please choose atleast one of the skills!");
        return false;
    }

    // console.log("this is the start");
    // if validation do not fail insertIntoTable
    enrollStudent();
}

var details = [];
function enrollStudent() {

    let name = document.getElementById("nameId").value;
    let email = document.getElementById("emailId").value;
    let website = document.getElementById("websiteId").value;
    let link = document.getElementById("linkId").value;
    let ele1 = document.getElementById('gridRadios1');
    let ele2 = document.getElementById('gridRadios2');
    ele = []
    ele.push(ele1);
    ele.push(ele2);
    let gender = "";
    // console.log(ele);
    for (let checkbox=0; checkbox<ele.length; checkbox++) {
        // console.log(checkbox);
        if (ele[checkbox].checked)
            gender = ele[checkbox].value;
    }
    let markedCheckbox = []
    markedCheckbox.push(document.getElementById("inlineCheckbox1"));
    markedCheckbox.push(document.getElementById("inlineCheckbox2"));
    markedCheckbox.push(document.getElementById("inlineCheckbox3"));
    // console.log(markedCheckbox);
    let skills = "";
    for (let checkbox=0; checkbox<markedCheckbox.length; checkbox++) {
        if (markedCheckbox[checkbox].checked)
            skills = skills + markedCheckbox[checkbox].value + ",";
    }
    console.log(skills, gender);
    details.push({
        "description": name + "\n" + gender + "\n" + email + "\n" +  website + "\n" + skills,
        "image": link
    });

    let data = Object.keys(details[0]);
    
    let table = document.querySelector("table");
    generateTableHead(table, details[0]);
    generateTable(table, details);

}


function generateTableHead(table, data){
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data){
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function generateTable(table, details) {
    for(let element of details){
        let row = table.insertRow();
        for(let key in element){
            let cell = row.insertCell();
            let text = document.createTextNode(element[key]);
            cell.appendChild(text);
        }
    }    
}

async function loadIntoTable(inputURL, table, country, qid) {
    const tableHead = table.querySelector("thead");
    const tableBody = table.querySelector("tbody");
    console.log("Before Fetch")

    var url = new URL(inputURL)

    var params = { "country": country, "qid": qid } // or:
    //ar params = [['country', '35.696233'], ['long', '139.570431']]

    url.search = new URLSearchParams(params).toString();

    const response = await fetch(url).then(response => { return response }).catch(e => console.log(e));

    console.log("The response");


    data = await response.json();
    console.log(data["headers"]);
    const { headers, rows, countries, theme, subtheme } = data
    console.log(headers)

    console.log("Came past Fetch")

    const themeDiv = document.getElementById("question")
    themeDiv.innerHTML = ""
    const themeElement = document.createElement("h2")
    themeElement.textContent = theme + ": " + subtheme
    themeDiv.appendChild(themeElement)


    // Clear table data
    tableHead.innerHTML = "<tr><th>Country</th></tr>";
    tableBody.innerHTML = "<tr></tr>";

    for (const headerText of headers) {
        const headerElement = document.createElement("th")

        headerElement.textContent = headerText;
        tableHead.querySelector("tr").appendChild(headerElement)
    }

    let i = 0;

    for (const row of rows) {
        const rowElement = document.createElement("tr")
        const country = document.createElement("td")
        country.textContent = countries[i];
        console.log(headers[i]);
        i++;
        rowElement.appendChild(country);

        for (const cellText of row) {
            const cellElement = document.createElement("td")
            if (cellText < 2) {
                cellElement.textContent = Math.round(cellText * 1000) / 10 + "%";
            }
            else {
                cellElement.textContent = cellText;
            }

            rowElement.appendChild(cellElement);
        }
        tableBody.appendChild(rowElement);
    }


}

const form_1 = document.getElementById('inputForm_1');

form_1.addEventListener('submit', (event) => {
    // handle the form data
    event.preventDefault();

    let country_1 = form_1.elements['country_1'].value
    let country_2 = form_1.elements['country_2'].value
    let country = [country_1, country_2]
    console.log(country)
    let qid = form_1.elements['qid'].value
    console.log(qid)

    //form.removeEventListener('submit')
    loadIntoTable("http://127.0.0.1:5000/question", document.querySelector("table"), country, qid);

});

const form_2 = document.getElementById('inputForm_2');

form_2.addEventListener('submit', (event) => {
    // handle the form data
    event.preventDefault();

    let country = form_2.elements['country_1'].value
    console.log(country)
    let qid_1 = form_2.elements['qid_1'].value
    let qid_2 = form_2.elements['qid_2'].value
    let qid = [qid_1, qid_2]
    console.log(qid)

    //form.removeEventListener('submit')
    loadIntoTable("http://127.0.0.1:5000/cross", document.querySelector("table"), country, qid);

});

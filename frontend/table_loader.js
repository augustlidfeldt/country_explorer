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
    const { headers, rows } = data
    console.log(headers)

    console.log("Came past Fetch")
    // Clear table data
    tableHead.innerHTML = "<tr></tr>";
    tableBody.innerHTML = "<tr></tr>";

    for (const headerText of headers) {
        const headerElement = document.createElement("th")

        headerElement.textContent = headerText;
        tableHead.querySelector("tr").appendChild(headerElement)
    }
    for (const cellText of rows) {
        const cellElement = document.createElement("td")
        cellElement.textContent = cellText;
        tableBody.querySelector("tr").appendChild(cellElement)
    }
    //tableBody.appendChild(cellElement)

}

const form = document.getElementById('inputForm');

form.addEventListener('submit', (event) => {
    // handle the form data
    //console.log(event)
    event.preventDefault();

    let country = form.elements['country'].value
    console.log(country)
    let qid = form.elements['qid'].value
    console.log(qid)

    //form.removeEventListener('submit')
    loadIntoTable("http://127.0.0.1:5000/question", document.querySelector("table"), country, qid);

});


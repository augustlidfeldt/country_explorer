async function loadIntoTable(url, table) {
    const tableHead = table.querySelector("thead");
    const tableBody = table.querySelector("tbody");
    console.log("Before Fetch")
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

loadIntoTable("http://127.0.0.1:5000/", document.querySelector("table"));  
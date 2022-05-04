import React, { Component } from "react";
import { render } from "react-dom";
import { Grid, Typography, Button } from "@mui/material";
import { Link } from 'react-router-dom';
import BasicTable from "./Table";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            message: 'Hello',
            switch: true
        }
        this.testingButton = this.testingButton.bind(this)

    }

    testingButton() {
        if (this.state.message == 'Hello') {
            this.setState({ message: 'Goodbye', })
        }
        else { this.setState({ message: 'Hello', }) }

    };

    flagLoad(country) {
        const path = `../../static/images/${country.toLowerCase()}.png`

        return (
            <div align='center'>
                {country == 'Japan' ?
                    <img className='shadow' id="flag" src={require("../../static/images/japan.png")} />
                    :
                    <img className='shadow' id="flag" src={require("../../static/images/iraq.png")} />
                }

            </div>
        );
    }

    countryStat(region, country) {
        return (
            <Grid id="maingrid" container spacing={1} align='center'>
                <Grid item className='shadow' id='id1' xs={12} align='center'>
                    <Typography id='region' variant="h6" compact="h6">{region}</Typography>
                    <Typography id='country' variant="h3" compact="h3">{country}</Typography>
                    {this.flagLoad(country)}
                    <BasicTable className='shadow' id='fact-table'></BasicTable>
                </Grid>
            </Grid>
        )
    }

    render() {
        return (
            <div className="App">
                <Typography id='main-title' variant="h1" compact="h1">COUNTRY VISUALIZER</Typography>
                <Typography id='sub-title' variant="h4" compact="h4">Understand the world</Typography>
                <div id='wrapper'>
                    {this.countryStat('Middle East', 'Iraq')}
                    {this.countryStat('East Asia', 'Japan')}
                </div>
            </div >
        );
    }
}

export default App;
render(<App />, document.getElementById("app"));
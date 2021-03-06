import React, { Component } from 'react';
import ViewPatients from "./components/ViewPatients";

import './App.css';
import AddPatientComponent from "./components/AddPatientComponent";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>ListLess</h1>
        </header>
        <Router>
          <div>
            <ul>
              <li>
                <Link to="/">View Patients</Link>
              </li>
              <li>
                <Link to="/addPatient">Add Patient</Link>
              </li>
            </ul>
            <Route exact path="/" component={ViewPatients}/>
            <Route path="/addPatient" component={AddPatientComponent}/>
          </div>
        </Router>
      </div>
    );
  }
}

export default App;

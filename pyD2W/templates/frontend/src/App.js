import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import LandingPage from './screens/LandingPage';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

const App = () => (
  <BrowserRouter>
    <Switch>
      <Route path='/' component={LandingPage} />
    </Switch>
  </BrowserRouter>

);

export default App;
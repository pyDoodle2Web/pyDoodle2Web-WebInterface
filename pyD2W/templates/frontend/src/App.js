import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import LandingPage from './screens/LandingPage';

const App = () => (
  <BrowserRouter>
    <Switch>
      <Route path='/' component={LandingPage} />
    </Switch>
  </BrowserRouter>

);

export default App;
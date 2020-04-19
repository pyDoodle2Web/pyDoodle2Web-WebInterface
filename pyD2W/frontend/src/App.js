import React, { useState } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import LandingPage from './screens/LandingPage';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import UploadPage from './screens/UploadPage';
import GeneratedPage from './screens/GeneratedPage';

const App = () => {
  const [ generatedHtml, setGeneratedHtml ] = useState('');
  
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/' component={LandingPage} exact={true} />
        <Route path='/upload' render={() => <UploadPage setHtml={setGeneratedHtml} /> } />
        <Route path='/generatedSite' render={() => <GeneratedPage html={generatedHtml} />} />
      </Switch>
    </BrowserRouter>

  )
};

export default App;
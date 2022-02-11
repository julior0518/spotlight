import axios from 'axios';
import { Route, Switch} from 'react-router-dom'
import Nav from './components/Nav';
import LogInOut from './components/LogInOut';
import Movies from './components/Movie';

function App() {
  return (
    <div className="App">
      < Nav />

      <Switch>
        <Route exact path="/" render={Movies} />
        <Route exact path="/logInOut" render={LogInOut} />
      </Switch>
    </div>
  );
}

export default App;

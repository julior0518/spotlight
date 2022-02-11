import axios from 'axios';
import { Route, Switch, useParams} from 'react-router-dom'
import Nav from './components/Nav';
import LogInOut from './components/LogInOut';
import Movies from './components/Movie';
import { BASE_URL } from './globals'
import { useEffect, useState } from 'react';


function App() {

  const [users, setUsers] =useState([])

  useEffect(()=> {
    async function allUsers() {
      const res = await axios.get(`${BASE_URL}`);
      console.log(res)
      // setUsers(res.data);
    }
    allUsers()
  },[])


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

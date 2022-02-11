
import { Link } from 'react-router-dom';

function Nav() {
return (
    <div className="Nav">
        <Link to="/" className="li">
            Movies
        </Link>
        <Link to="/logInOut" className="li">
            SignUp/LogIn
        </Link>
    </div>
);
}

export default Nav;
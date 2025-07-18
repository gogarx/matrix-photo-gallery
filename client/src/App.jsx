//import React from 'react';
import { BrowserRouter as Router, NavLink, Route } from 'react-router-dom';
// Importe outros componentes usados:
import Gallery from './Gallery';
import Clock from './Clock';
//import NavLinkItem from './NavLinkItem'; // ou ajuste o caminho conforme seu projeto
import './site.scss';

// Definição do Footer
const Footer = () => (
    <footer className="ui vertical footer segment">
        <div className="ui center aligned container">
            View on{' '}
            <a href="https://github.com/osteele/matrix-photo-gallery">GitHub</a>
        </div>
    </footer>
);

// (Opcional) Defina TIDE_APP_URL se usá-lo em outro arquivo, ou remova se não usar
// const TIDE_APP_URL = process.env.REACT_APP_TIDE_APP_URL;

const NavLinkItem = props => (
    <NavLink className="item" activeClassName="active" {...props}>
        {props.children}
    </NavLink>
);

//  Defina App uma única vez, com roteamento completo
const App = () => (
    <Router>
        <div className="app">
            <main className="ui container">
                <nav id="app-menu" className="ui tabular menu">
                    <NavLinkItem exact to="/">
                        Gallery
                    </NavLinkItem>
                    <NavLinkItem to="/clock">Sundial</NavLinkItem>
                    {/* Adicione outros menus se houver */}
                </nav>
                <Route exact path="/" component={Gallery} />
                <Route path="/clock" component={Clock} />
                {typeof TIDE_APP_URL !== 'undefined' && TIDE_APP_URL && (
                    <Route
                        path="/tides"
                        render={() => {
                            window.location.href = TIDE_APP_URL;
                            return null; // React exige retorno
                        }}
                    />
                )}
            </main>
            <Footer />
        </div>
    </Router>
);

// Exporte corretamente (padrão ou nomeado)
export default App;
// ou, se quiser nomeado:
// export { App };

import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar'
import Panel from './components/Panel';
import Content from './components/Content';

class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <MuiThemeProvider>
                    <div>
                        <AppBar title="UNIVER LAB C#" showMenuIconButton={false}/>
                        <div className="app-root">
                            <Panel/>
                            <Content/>
                        </div>
                    </div>
                </MuiThemeProvider>
            </BrowserRouter>
        );
    }
}

export default App;

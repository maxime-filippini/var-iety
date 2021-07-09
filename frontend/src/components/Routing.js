import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

export default function Routing(props) {
  return (
    <Router>
      {props.children}
      <Switch>
        {props.routeItems.map((item) => (
          <Route path={item.url} key={item.url}>
            {item.page}
          </Route>
        ))}
      </Switch>
    </Router>
  );
}

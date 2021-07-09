import React from "react";
import Navbar from "./Navbar";
import Footer from "./Footer";
import { Typography, Divider } from "@material-ui/core";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import pageIndex from "../data/PageIndex";

export default function Layout(props) {
  const barItems = [
    <Typography variant="h5" component="h5">
      VaR-iety
    </Typography>,
  ];

  return (
    <Router>
      <Switch>
        <Navbar withDrawer={true} drawerItems={pageIndex} barItems={barItems}>
          {pageIndex.map((item) =>
            item.url === "/" ? (
              <Route exact path={item.url} key={item.url}>
                {item.page}
              </Route>
            ) : (
              <Route path={item.url} key={item.url}>
                {item.page}
              </Route>
            )
          )}
        </Navbar>
        <Divider />
        <Footer />
      </Switch>
    </Router>
  );
}

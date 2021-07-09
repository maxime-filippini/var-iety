import React from "react";
import { Typography } from "@material-ui/core";
import { makeStyles, useTheme } from "@material-ui/core/styles";

const useStyles = makeStyles(() => ({
  footerText: {
    padding: "0.2rem 1rem",
  },
}));

export default function Footer() {
  const classes = useStyles();

  return (
    <Typography align="right" className={classes.footerText}>
      By Maxime Filippini
    </Typography>
  );
}

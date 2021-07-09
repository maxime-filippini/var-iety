import HomeIcon from "@material-ui/icons/Home";
import ListIcon from "@material-ui/icons/List";
import DashboardIcon from "@material-ui/icons/Dashboard";
import FunctionsIcon from "@material-ui/icons/Functions";

import Home from "../pages/Home";
import PortfolioBuilder from "../pages/PortfolioBuilder";
import ValueAtRisk from "../pages/ValueAtRisk";
import RiskDashboard from "../pages/RiskDashboard";

const pageIndex = [
  { label: "Home", icon: <HomeIcon />, url: "/", page: <Home /> },
  {
    label: "Portfolio Builder",
    icon: <ListIcon />,
    url: "/portfolio-builder",
    page: <PortfolioBuilder />,
  },
  {
    label: "Value-at-Risk",
    icon: <FunctionsIcon />,
    url: "/value-at-risk",
    page: <ValueAtRisk />,
  },
  {
    label: "Risk dashboard",
    icon: <DashboardIcon />,
    url: "/risk-dashboard",
    page: <RiskDashboard />,
  },
];

export default pageIndex;

import "./Root.scss";
import Predictor from "views/Predictor";
import Predictions from "views/Predictions";
import { BrowserRouter, Route, Routes, NavLink } from "react-router-dom";
import { routes } from "routes";

const Root = () => {
  return (
    <BrowserRouter>
      <div className="wrapper">
        <div className="header">Google Quest</div>
        <div className="top-panel">
          <NavLink to={routes.PREDICTOR} className="option">
            Make prediction
          </NavLink>
          <NavLink to={routes.PREDICTIONS} className="option">
            Check predictions
          </NavLink>
        </div>
        <div className="container">
          <Routes>
            <Route path={routes.PREDICTOR} element={<Predictor />} />
            <Route path={routes.PREDICTIONS} element={<Predictions />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default Root;

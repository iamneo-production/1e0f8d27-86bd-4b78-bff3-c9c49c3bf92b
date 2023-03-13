import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Workshoppage from "./Workshoppage";
import Eventdetails from "./Eventdetails";

function WorshopLandpage() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Workshoppage />} />
        <Route path="/eventdetails" element={<Eventdetails />} />
      </Routes>
    </BrowserRouter>
  );
}

export default WorshopLandpage;

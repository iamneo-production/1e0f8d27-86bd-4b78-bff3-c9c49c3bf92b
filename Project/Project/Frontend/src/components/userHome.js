import React, { Component, useEffect, useState } from "react";
import AppBar from "./AppBar";
import Main from "./Main";

export default function UserHome({ userData }) {
  
  return (
   <div>
    <AppBar/>
    <Main/>
   </div>
  );
}

import {
  Container,
  Button,
  Form,
  NavDropdown,
  Nav,
  Navbar
} from "react-bootstrap";
import React from "react";
import { DropdownButton, Dropdown } from "react-bootstrap";
import { BsFillPersonFill } from "react-icons/bs";
import "../App.css";
import { useNavigate } from "react-router-dom";

function AppBar() {
  const navigate = useNavigate();
  const logOut = () => {
    window.localStorage.clear();
    window.location.href = "/";
  };
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">She Hack</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              <Nav.Link href="#home" onClick={() => navigate("/")}>
                Home
              </Nav.Link>
              <Nav.Link onClick={() => navigate("/hackathon")}>
                Hackathon
              </Nav.Link>
              <NavDropdown title="Workshops" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Coding</NavDropdown.Item>
                <NavDropdown.Item
                  href="#action/3.2"
                  onClick={() => navigate("/appdevelopment")}
                >
                  App Development
                </NavDropdown.Item>
                <NavDropdown.Item
                  href="#action/3.3"
                  onClick={() => navigate("/webdesign")}
                >
                  Web Design
                </NavDropdown.Item>

                <NavDropdown.Item
                  href="#action/3.4"
                  onClick={() => navigate("/cybersecurity")}
                >
                  Cyber Security
                </NavDropdown.Item>
              </NavDropdown>
              <Nav.Link onClick={() => navigate("/course")}>Courses</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <div className="ov">
        <div class="dropdown">
          <a href="#">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135823.png" />
          </a>

          <div class="dropdown-content">
            <a onClick={() => navigate("/profile")}>
              My Profile
            </a>
            <a href="#">Notification</a>
            <hr />
            <a href="#" className="last" onClick={logOut}>
              SignOut
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AppBar;

import React from "react";
import { Carousel } from "react-bootstrap";
import { Container, Row, Col } from "react-bootstrap";

const Banner = () => {
  return (
    <div style={{ width: "80%", margin: "auto" }} className="my-4 ">
      <Carousel>
        <Carousel.Item interval={1000}>
          <img
            className="d-block w-100"
            src="https://media.istockphoto.com/id/1217882746/photo/diverse-team-of-electronics-development-engineers-standing-at-the-desk-working-with-documents.jpg?s=612x612&w=0&k=20&c=EvA0Gt_LKlGTHljVYZ6ha7QjDLY02_aUPJo_GcldWLc="
            alt="First slide"
            width="100"
            height="395"
          />
          <Carousel.Caption>
            <h3 style={{ fontWeight: "bold", letterSpacing: "1px" }}>
              Workshops
            </h3>
            <p>
              Live as if you were to die tomorrow.Learn as if you were to live
              forever
            </p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item interval={500}>
          <img
            className="d-block w-100"
            src="https://media.istockphoto.com/id/1200831834/photo/business-technology-internet-and-network-concept-coaching-mentoring-education-business.jpg?s=612x612&w=0&k=20&c=T-2VIWM5l1mfSJdYHB9GchmmRrmvCnKlsnAloyOq45I="
            alt="Second slide"
            width="100"
            height="395"
          />
          <Carousel.Caption>
            <h3 style={{ fontWeight: "bold", letterSpacing: "1px" }}>
              Hackathons
            </h3>
            <p>Hackathons are where your crazy idea becomes reality</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://media.istockphoto.com/id/1218431614/photo/e-learning-online-in-the-digital-age-knowledge-education.jpg?s=612x612&w=0&k=20&c=GItmLljpsInHInRxoN826XdRf3bUJ5KPvvqyU7URjdI="
            alt="Third slide"
            width="100"
            height="395"
          />
          <Carousel.Caption>
            <h3 style={{ fontWeight: "bold", letterSpacing: "1px" }}>
              Hands On Learning
            </h3>
            <p>Never stop learning because life never stop teaching</p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </div>
  );
};

export default Banner;
